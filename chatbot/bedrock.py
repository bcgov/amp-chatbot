import boto3


INPUT_PROMPT = 'What data sources does the SDPR Corporate Data Warehouse use?'

client = boto3.client(service_name='bedrock-agent-runtime'
    )

response=client.invoke_agent(
    agentAliasId='3P0LT0MYR6',  
    agentId='OFAMSWWUPH',
    inputText=INPUT_PROMPT,
    sessionId='11'  # Modify this to resume sessions
)


completion = ""

for event in response.get("completion"):
    chunk = event["chunk"]
    completion += chunk["bytes"].decode()

print(completion)