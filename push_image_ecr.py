import boto3
import docker
import base64

# Push docker image to ECR.  Make sure you already created ECR repo in AWS console.

# IAM user needs ""AmazonEC2ContainerRegistryFullAccess" " and "AmazonECS_FullAccess"
ecr_client = boto3.client(
    'ecr',
    region_name='ap-northeast-1',
    aws_access_key_id='xxxxx',
    aws_secret_access_key='yyyy'
    )

docker_client = docker.from_env()
auth_token = ecr_client.get_authorization_token()

encoded_token = auth_token['authorizationData'][0]['authorizationToken']
decoded_token = base64.b64decode(encoded_token).decode('utf-8')
username, password = decoded_token.split(':')

ecr_url = auth_token['authorizationData'][0]['proxyEndpoint']
docker_client.login(username=username, password=password, registry=ecr_url)

# Tag the local Docker image
local_image = docker_client.images.get('test-s3:latest')
ecr_image_tag = f"111111.dkr.ecr.ap-northeast-1.amazonaws.com/test-s3:latest"
local_image.tag(ecr_image_tag)

# Push the image to ECR
push_result = docker_client.images.push(ecr_image_tag)
print(push_result)
