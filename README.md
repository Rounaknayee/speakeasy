# speakeasy

This is a Whatsapp application that takes a voice input from the user and translates the audio to text.

This is a terraform code for entire infrastructure spinup on AWS cloud platform and Twilio for Whatsapp Integrqation.

## Usage


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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- [Terraform](https://www.terraform.io/)
- [AWS](https://aws.amazon.com/)
- [Twilio](https://www.twilio.com/)

## Authors

- [ROUNAK]() - Initial work


