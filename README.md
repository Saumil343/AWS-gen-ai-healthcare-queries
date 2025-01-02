This repository contains a Python implementation that integrates AWS Kendra and AWS Bedrock to provide contextually enhanced answers for healthcare queries.

**Overview**

In the healthcare industry, quick access to accurate and contextually relevant information is critical. This solution leverages AWS Kendra for intelligent search and AWS Bedrock for generative AI, enabling healthcare professionals and patients to receive precise, enhanced responses.

The solution retrieves medical information using AWS Kendra, processes the query, and then enhances the response with AWS Bedrock’s generative capabilities.

**Key Features** 

- **AWS Kendra:** Search engine to retrieve relevant, high-precision medical information.
- **AWS Bedrock (Gen-AI):** Enhances Kendra’s responses, adding context and tailored insights for healthcare professionals and patients.
- **Python Integration:** Smooth communication between Kendra and Bedrock using Python.

**Requirements**

- AWS Account
- AWS SDK for Python (Boto3)
- Access to AWS Kendra and AWS Bedrock
- An S3 bucket for storing medical documents

**Setup**

1. Clone the repository.
2. Ensure you have the required AWS credentials configured for accessing Kendra and Bedrock.
3. Update the Kendra index ID in the code.
4. Run the Python script to start querying and enhancing responses.

**Technical Details**

For more information on how this solution works, check out the full blog post https://dev.to/saumil343/gen-ai-powered-healthcare-queries-with-aws-kendra-bedrock-gpd.

**Usage**
Run the Python script to query AWS Kendra and retrieve enhanced responses using AWS Bedrock.
