import boto3
import json

# AWS region setup
region_name = 'us-east-1'

# Initialize Kendra client
kendra = boto3.client('kendra', region_name=region_name)
index_id = 'kendra-index-id-here'
query = "what are the warning signs for DKA? "

# Initialize Bedrock client
boto3_bedrock = boto3.client('bedrock-runtime', region_name=region_name)

# Function to invoke Bedrock for enhanced response
def get_bedrock_enhanced_response(human_input, context_string):
    prompt_data = f"Here is some context:\n\n{context_string}\n\nHuman: {human_input}\nAssistant:"

    body_part = json.dumps({
        'inputText': prompt_data,
        'textGenerationConfig': {
            'maxTokenCount': 4096,  # Corrected maxTokenCount to be within the allowed range
            'stopSequences': [],
            'temperature': 0.7,  # Adjust as needed
            'topP': 1.0
        }
    })

    # Invoke Bedrock model
    response = boto3_bedrock.invoke_model(
        body=body_part,
        contentType="application/json",
        accept="application/json",
        modelId='amazon.titan-text-lite-v1'  # Bedrock model ID
    )

    # Read and decode the StreamingBody before parsing
    response_body = response['body'].read().decode('utf-8')
    output_text = json.loads(response_body)['results'][0]['outputText']
    return output_text

# Kendra query processing
response = kendra.query(QueryText=query, IndexId=index_id)

# Process Kendra query results
for query_result in response['ResultItems']:
    begin = 0
    end = 0
    if query_result['Type'] == 'ANSWER':
        answer = query_result['AdditionalAttributes'][0]['Value']['TextWithHighlightsValue']
        highlight = answer['Highlights']
        for obj in highlight:
            if obj['TopAnswer'] is True:
                begin = obj['BeginOffset']
                end = obj['EndOffset']

        # Get the answer text
        if end == 0:
            answer_text = answer['Text']
        else:
            answer_text = answer['Text'][begin:end]

        print("Kendra Answer: ", answer_text)

        # Now pass the Kendra response to Bedrock for enhancement
        enhanced_response = get_bedrock_enhanced_response(query, answer_text)
        print("\nEnhanced response from Bedrock:\n")
        print(enhanced_response)
