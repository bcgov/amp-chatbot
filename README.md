## QUICK START 

### Env Set up (Automated)

Run `./setup.sh`, this will set up a python virtual environment and install the neccesarry packages

### Env Set up (Manual)

For a quick manual set up:
1. Set up venv and install the packages in `./requirements.txt`
1. Ensure the AWS cli is installed locally: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### Authentication

Set up the necessary configuration and credentials files the AWS cli utilizes for authentication: https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html

TLDR: 

1. COPY your AWS access and AWS secret access key from the login console (or [parameter store](https://ca-central-1.console.aws.amazon.com/systems-manager/parameters/%252Fiam_users%252Famp-chatbot_keys/description?region=ca-central-1&tab=Table#list_parameter_filters=Name:Contains:amp) once a role is defined): 
1. Create a config file at: `~/.aws/config`

```ini
[default]
region = ca-central-1
output=json
```

1. Create a credentials file at: `~/.aws/credentials`

```ini
[default]
aws_access_key_id = *YOUR access Key*
aws_secret_access_key = * YOUR secret access key*
```
1. Set the AWS_CONFIG_FILE and AWS_SHARED_CREDENTIALS_FILE to the locations of the respective config / credentials files


### Test agent

Run the code in `./chatbot/boto_ex.py` or `chatbot/bedrock.py` to verify connection / authentication





# FUTURE WORK

## AWS Cli

The `setup.sh` script installed the necessary tools to use the AWS Cli. 
Verify this tool installed correctly by checking the aws cli version number (NOTE: as awscli was installed as a pip package the path must be provided if you do not activate your venv)
```bash
./env/scripts/python ./env/lib/site-packages/awscli --version
# example output: aws-cli/1.33.26 Python/3.11.9 Windows/10 botocore/1.34.144
```

### Authentication

With the AWS cli installed, it must be configured with your AWS credentials. Note a configureation file is also supported: https://pypi.org/project/awscli/.

These credentials can be copied at the time of log in to the AWS console:

#### IAM USER

Set up an IAM user: https://developer.gov.bc.ca/docs/default/component/public-cloud-techdocs/design-build-and-deploy-an-application/iam-user-service/


##### CLI
With your credentials ready run the following command:

```bash
./env/scripts/python ./env/lib/site-packages/awscli configure
```
This command will prompt you for credentials, enter them as required


##### Config File 

https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html

#### Test authentication

Test the authentication with any relevant command. For example, execute the following command to list all of your amazon s3 buckets

```bash
aws s3 ls
```
If installed correctly, it should output a list of your buckets



### Further Reading

The AWS documentaion: https://docs.aws.amazon.com/cli/

### AWS cdk

https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_bedrock-readme.html

## Boto Library

The boto library is used to handle AWS operations via a Python API

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

### Authentication
The aws `configure` command will sync with boto, and calls to AWS s3 and can be made within Python modules as shown below:

```python 
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
```

### BOTO with Bedrock

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html




https://github.com/aws-samples/amazon-bedrock-serverless-prompt-chaining
## License
Copyright 2019 Province of British Columbia

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


