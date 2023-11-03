provider "aws" {
    region = "us-east-1"
}

# data "aws_iam_policy" "AccessAnalyzerServiceRolePolicy" {
#     arn = "arn:aws:iam::aws:policy/aws-service-role/AccessAnalyzerServiceRolePolicy"
# }

# resource "aws_iam_role_policy_attachment" "AWSServiceRoleForAccessAnalyzer-role-policy-attach" {
#   role       = "${aws_iam_role.AWSServiceRoleForAccessAnalyzer.name}"
#   policy_arn = "${data.aws_iam_policy.AccessAnalyzerServiceRolePolicy.arn}"
# }

# resource "aws_iam_service_linked_role" "AWSServiceRoleForAccessAnalyzer" {
#     aws_service_name = "AWSServiceRoleForAccessAnalyzer"
# }

resource "aws_s3_bucket" "tf_wa_audio_files" {
    bucket = "tf-wa-audio-files"
    acl    = "private"

    tags = {
        Name        = "WA Audio Files"
        Environment = "Dev"
    }
}

resource "aws_dynamodb_table" "tf_wa_audio_database" {
    name = "tf-wa-audio-database"
    billing_mode = "PROVISIONED"
    read_capacity = 1
    write_capacity = 1
    stream_enabled   = true
    hash_key = "filename"
    stream_view_type = "NEW_AND_OLD_IMAGES"
    
    attribute {
        name = "filename"
        type = "S"
    }
}


data "archive_file" "lambda_transcribe" {
  type        = "zip"
  source_file = "./lambdas/transcribe.py"
  output_path = "./lambdas/transcribe.zip"
}

data "archive_file" "lambda_inbound_message" {
  type        = "zip"
  source_file = "./lambdas/inboundMessage.py"
  output_path = "./lambdas/inbound_message.zip"
}

resource "aws_lambda_function" "tf_lambda_transcribe" {
    filename = "./lambdas/transcribe.zip"
    function_name = "tf-transcribe"
    role = aws_iam_role.tf_transcribe_role.arn
    handler = "tf-transcribe.lambda_handler"

    source_code_hash = data.archive_file.lambda_transcribe.output_base64sha256
    runtime = "python3.10"
    architectures = ["arm64"]
    layers = [aws_lambda_layer_version.tf_twilio_requests_layer.arn]
}

resource "aws_lambda_function" "tf_lambda_inbound_message" {
    filename = "./lambdas/inbound_message.zip"
    function_name = "tf-inbound-message"
    role = aws_iam_role.tf_transcribe_role.arn
    handler = "tf-inbound-message.lambda_handler"

    source_code_hash = data.archive_file.lambda_inbound_message.output_base64sha256
    runtime = "python3.10"
    architectures = ["arm64"]
    layers = [aws_lambda_layer_version.tf_twilio_requests_layer.arn]
}

resource "aws_lambda_layer_version" "tf_twilio_requests_layer" {
    filename = "./lambdas/twilio_requests_layer.zip"
    layer_name = "tf-twilio-requests-layer"

    compatible_runtimes = [
        "python3.10"
    ]
}

resource "aws_iam_role" "tf_transcribe_role" {
    name               = "lambda-dynamodb-role"
    assume_role_policy = jsonencode({
        "Version": "2012-10-17",
        "Statement": [
            {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": "LambdaAssumeRole"
            }
        ]
    })
}

resource "aws_iam_role_policy" "dynamodb_read_log_policy" {
    name   = "lambda-dynamodb-log-policy"
    role   = aws_iam_role.tf_transcribe_role.id
    policy = jsonencode({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [ "logs:*" ],
                "Effect": "Allow",
                "Resource": [ "arn:aws:logs:*:*:*" ]
            },
            {
                "Action": [ "dynamodb:BatchGetItem",
                            "dynamodb:GetItem",
                            "dynamodb:GetRecords",
                            "dynamodb:Scan",
                            "dynamodb:Query",
                            "dynamodb:GetShardIterator",
                            "dynamodb:DescribeStream",
                            "dynamodb:ListStreams" ],
                "Effect": "Allow",
                "Resource": [
                "${aws_dynamodb_table.tf_wa_audio_database.arn}",
                "${aws_dynamodb_table.tf_wa_audio_database.arn}/*"
                ]
            }
        ]
    })
}

resource "aws_lambda_event_source_mapping" "tf_lambda_event_source_mapping" {
    event_source_arn  = aws_dynamodb_table.tf_wa_audio_database.stream_arn
    function_name     = aws_lambda_function.tf_lambda_transcribe.arn
    starting_position = "LATEST"
}

resource "aws_api_gateway_rest_api" "tf_speakeasy_api_gateway" {
    name = "tf-speakeasy-api-gateway"
    description = "API Gateway for Speakeasy"
}

resource "aws_api_gateway_resource" "tf_speakeasy_api_gateway_resource" {
    rest_api_id = aws_api_gateway_rest_api.tf_speakeasy_api_gateway.id
    parent_id = aws_api_gateway_rest_api.tf_speakeasy_api_gateway.root_resource_id
    path_part = "inboundmessage"
}

resource "aws_api_gateway_method" "tf_speakeasy_post" {
    rest_api_id = aws_api_gateway_rest_api.tf_speakeasy_api_gateway.id
    resource_id = aws_api_gateway_resource.tf_speakeasy_api_gateway_resource.id
    http_method = "POST"
    authorization = "NONE"

    request_parameters = {
        "method.request.path.proxy": true
    }
}

resource "aws_api_gateway_integration" "tf_speakeasy_integration" {
    rest_api_id             = aws_api_gateway_rest_api.tf_speakeasy_api_gateway.id
    resource_id             = aws_api_gateway_resource.tf_speakeasy_api_gateway_resource.id
    http_method             = aws_api_gateway_method.tf_speakeasy_post.http_method
    integration_http_method = "POST"
    type                    = "AWS_PROXY"
    uri                     = aws_lambda_function.tf_lambda_inbound_message.invoke_arn
}