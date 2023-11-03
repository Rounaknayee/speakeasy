import boto3, os, requests, time, json
from twilio.rest import Client

transcribe = boto3.client('transcribe')
s3 = boto3.client('s3')
dynamodb = boto3.client("dynamodb")

def lambda_handler(event, context):
    # print("Dynamo DB Trigger event",event)
    if event['Records'][0]['eventName'] == 'MODIFY':
        return
    
    dynamo_fields =  clean_input_event(event)
    
    audio_url = str("s3://"+dynamo_fields['s3_bucket']+"/"+dynamo_fields['filename'])
    job_name  = str('wa-transcription-'+dynamo_fields['filename'])
    bucket_name , key_name = dynamo_fields['s3_bucket'].split('/')
    file_key = str(key_name+'/transcription-'+key_name)
    
    try:
        
        start_transcription = transcribe.start_transcription_job(
            TranscriptionJobName = job_name,
            Media                = {'MediaFileUri': audio_url },
            # IdentifyMultipleLanguages = True,
            # LanguageOptions      = ['en-IN'],
            LanguageCode         = 'en-US' ,
            # OutputBucketName     = bucket_name, | 'en-US' | 'hi-IN' # Specify the S3 bucket for storing the result
            # OutputKey            = file_key
        )
        
        print(str(start_transcription))
    except Exception as e:
        print(f'Error sending transcription job: {str(e)}')
        
    try:
        while True:
            response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
            job_status = response['TranscriptionJob']['TranscriptionJobStatus']
            if job_status in ['COMPLETED', 'FAILED']:
                break
            time.sleep(3)
        print("Response :",response)
        transcribed_url = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
        
        transcribed_text_json = json.loads(requests.get(transcribed_url).content.decode('utf-8'))
        
        transcribed_text = transcribed_text_json['results']['transcripts'][0]['transcript']
        print(f'Transcribed text: {transcribed_text}')

    except Exception as e:
        print(f'Error getting transcription result: {str(e)}')
    
    try:
        response = dynamodb.update_item(
            TableName="wa-audio-database",
            Key={"filename": {"S": dynamo_fields['filename']}},
            UpdateExpression="SET transcribed_text = :transcript",
            ExpressionAttributeValues={":transcript": {"S": transcribed_text}}
        )
            
    except Exception as e:
        print(f'Error saving to Dynamo DB: {str(e)}')
        
    send_twilio_message(str("*Your Transcribed Text is :*\n\n"+transcribed_text),dynamo_fields)
    
    return 
    




##################################################################################################

def clean_input_event(event):
    new_image = event['Records'][0]['dynamodb']['NewImage']
    key_value_pairs = {}
    for key, value in new_image.items():
        key_value_pairs[key] = list(value.values())[0]
    return key_value_pairs
    
def send_twilio_message(message,dynamo_fields):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token  = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    
    response = client.messages.create(
        body = message,
        from_= ('whatsapp:'+dynamo_fields['twilio_number']),
        to   = ("whatsapp:+"+dynamo_fields['wa_from'])
    )
    
    print("Sending Message Response : ",response)
    print("Succcessfully Transcribed")
    
    return
    
    
    
    




















































def start_transcription(job_name, media_uri, language_code, output_bucket, output_key):
    try:
        # Start the transcription job
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': media_uri},
            MediaFormat='mp3',  # Replace with the format of your media file
            LanguageCode=language_code,
            OutputBucketName=output_bucket,  # Specify the S3 bucket for storing the result
            OutputKey=output_key  # Specify the S3 key for storing the result
        )
        print(f'Transcription job "{job_name}" started successfully.')
    except Exception as e:
        print(f'Error starting transcription job: {str(e)}')

def get_transcription_result(job_name, output_bucket, output_key):
    try:
        # Wait for the transcription job to complete
        transcribe.get_waiter('transcription_job_completed').wait(
            TranscriptionJobName=job_name
        )

        # Get the transcription job result
        response = transcribe.get_transcription_job(
            TranscriptionJobName=job_name
        )

        # Extract the transcribed text from the response
        transcribed_text = response['TranscriptionJob']['Transcript']['Text']
        print(f'Transcribed text: {transcribed_text}')

        # Store the transcribed text in the specified S3 bucket and key
        s3.put_object(Body=transcribed_text.encode(), Bucket=output_bucket, Key=output_key)
        print(f'Transcription result stored in S3 bucket: {output_bucket}, key: {output_key}')

    except Exception as e:
        print(f'Error getting transcription result: {str(e)}')

# # Call the start_transcription function with the job name, media URI, language code, output S3 bucket, and output S3 key
# start_transcription('example-job', 's3://bucket-name/media.mp3', 'en-US', 'output-bucket', 'output-key')

# # Call the get_transcription_result function with the job name, output S3 bucket, and output S3 key to retrieve the transcribed text and store it in S3
# get_transcription_result('example-job', 'output-bucket', 'output-key')


