import boto3

# Initialize the ECS client
ecs_client = boto3.client(
    'ecs',
    region_name='ap-northeast-1',
    aws_access_key_id='xxxx',
    aws_secret_access_key='yyyy'
    )

# Task definition name and cluster name
task_definition_name = 'test-s3-task2'
cluster_name = 'my-cluster2'

# Run the task in ECS
response = ecs_client.run_task(
    cluster=cluster_name,
    taskDefinition=task_definition_name,
    launchType='FARGATE',  # EC2 or 'FARGATE' for a serverless deployment
    count=1,  # Number of containers to run
    networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': ['subnet-0000'],
            'assignPublicIp': 'ENABLED'
        }
    }
)

print(response)
breakpoint()

# replace the container ID name from the print(response) and replace below
container_id = "xxxx"
response = ecs_client.describe_tasks(cluster='my-cluster2', tasks=[f'arn:aws:ecs:ap-northeast-1:111111111:task/my-cluster2/{container_id}'])
print(response['tasks'][0]['lastStatus'])
print(response)




