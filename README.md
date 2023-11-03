# SpeakEasy

SpeakEasy is a WhatsApp application designed to convert voice as well as graphical image inputs from users into text. This application leverages AWS cloud infrastructure and Twilio's WhatsApp integration to provide seamless voice-to-text translation within WhatsApp and the entire cloud infrastructure has been spinned up using Terraform.

## Architecture

![Alt text](./Speak%20Easy%20Architecture.png)


## Access the Project

The live project can be accessed at the following URL:

[Whatsapp URL](https://api.whatsapp.com/send?phone=14155238886&text=join%20wild-useful)

Send the default code already the message box to get started. Happy Speaking !

## Prerequisites

- Terraform
- AWS account
- AWS CLI
- AWS IAM user with programmatic access
- Twilio account
- Twilio Whatsapp sandbox

## Setup

- Clone the repository
- Create a terraform.tfvars file in the root directory and add the following variables

```
AWS KEY=
AWS SECRET=
AWS REGION=
TWILIO ACCOUNT SID=
```


## Deployment

- Run `terraform init` to initialize the terraform
- Run `terraform plan` to see the changes that will be made
- Run `terraform apply` to apply the changes

## Destroy

- Run `terraform destroy` to destroy the infrastructure

## Acknowledgments

- [Terraform](https://www.terraform.io/)
- [AWS](https://aws.amazon.com/)
- [Twilio](https://www.twilio.com/)

## Authors

- [ROUNAK](https://www.rounaknayee.github.io/)


