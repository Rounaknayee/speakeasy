import boto3, json, base64, requests, datetime
from urllib.parse import unquote
s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    print("event",event) 
    result = ''
    try:
        result = clean_string(event['body'])
    except Exception as e:
        print('Exception in decoding url: ',str(e))
        return lambda_response("Error decoding url : "+str(e))
    
    if result['NumMedia'] == 0 and (result['Body'] in ['Hi','hi','hello','Hello']):
        return lambda_response("Hello " +result['ProfileName']+" ! \nWelcome to SpeakEasy ! \n\n" \
        +"You can input an Audio File either by directly recording here or sending it as a media attachment! ")
    
    if  result['NumMedia'] == 0 :
        return lambda_response("Hello " +result['ProfileName']+"! \n" +"Sorry! Media file required")
    elif result['NumMedia'] != 1:
        return lambda_response("Hello " +result['ProfileName']+"! \n" +"Sorry! Only one Media file allowed!")
        
    media_type0 = unquote(result['MediaContentType0'])
    media_url0  = unquote(result['MediaUrl0'])
    
    if media_type0 != 'audio/ogg':
        return lambda_response("Only Audio File Allowed")
        
    bucket_name = 'wa-audio-files'
    table_name  = 'wa-audio-database'
    file_name   = 'wa-audio-file-'+str(result['MessageSid'])
    file_key    = str(result['MessageSid'])+"/"+'wa-audio-file-'+str(result['MessageSid'])
    
    try:
        response = requests.get(media_url0)
        
        s3.put_object(Bucket = bucket_name, Key = file_key, Body = response.content)
        
        dynamodb.put_item(  TableName = table_name,
            Item = {
                'filename'  : { 'S' :  file_name   },  
                'file_type' : { 'S' :  media_type0 },
                's3_bucket' : { 'S' :  (bucket_name+'/'+str(result['MessageSid'])) },
                'twilio_url': { 'S' :  media_url0  }, 
                'timestamp' : { 'S' :  datetime.datetime.now().isoformat()},
                'wa_from'      : { 'S' :  result['WaId']   },
                'twilio_number': { 'S' :  result['To']     },
                'transcribed_text' : { 'S' :  '' } 
                })
    except Exception as e:
        print('Exception in uploading file to s3 and lambda : ',str(e))
        return lambda_response("Hello " +result['ProfileName']+"! \n" +"Error "+str(e))
        
    # return lambda_response("*Audio stored in AWS* \n"+str(media_type0)+"\n"+str(media_url0))
    return lambda_response("Thankyou! Your Transcribed text will be here shortly")
    

### Function to create appropriate XML Response
# ======================================================== 
def lambda_response(response_body):
    lambda_response = {
        "statusCode": 200,
        "body": '<?xml version="1.0" encoding="UTF-8"?><Response><Message>'+response_body+'</Message></Response>',
        "headers": {"Content-Type": "application/xml",}
    }
    return lambda_response
# ============================================================ 
    
### Function to clean the query string
# ====================================================================================  
def clean_string(input_string):
    decoded_string = base64.b64decode(input_string).decode("utf-8")
    key_value_pairs = decoded_string.split("&")
    result = {}
    for key_value in key_value_pairs:
        key, value = key_value.split("=")
        result[key] = value
    result['NumMedia']    = int(result['NumMedia'])
    result['To']          = unquote(result['To']).split(':')[-1]
    result['ProfileName'] = result['ProfileName'].replace('+', ' ')
    print(result)
    return result # Returns Cleaned String in Dictionary
# ====================================================================================    
    
#########################################################################

# print("Sender Name:",result['ProfileName'])
# print("Whtsapp Sender",result['WaId'])
# print("Message Body",result['Body'])
# print("NumMedia",result['NumMedia'])