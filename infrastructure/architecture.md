**Project Overview**
This project implements a serverless Text-to-Speech pipeline using AWS services. 
Whenever a text file is uploaded to an S3 bucket, an AWS Lambda function is automatically triggered. 
The Lambda function reads the text file, converts the content into speech using Amazon Polly, 
and stores the generated audio file into a destination S3 bucket.

**Architecture Components**
1.AWS Lambda — Serverless compute service to process files.
2.Amazon S3 (Source Bucket) — Stores uploaded text files.
3.Amazon Polly — Converts text to speech.
4.Amazon S3 (Destination Bucket) — Stores generated audio files.
5.IAM Role — Provides permissions to Lambda.

**High-Level Architecture Flow**
1. User uploads a .txt file to Source S3 bucket.
2. S3 Event Notification triggers Lambda function.
3. Lambda reads text file content.
4. Lambda sends text to Amazon Polly.
5. Polly generates speech audio.
6. Lambda saves MP3 file into Destination S3 bucket.

**Architecture Diagram**
User
  │
  ▼
S3 Source Bucket
  │ (Event Trigger)
  ▼
AWS Lambda Function
  │
  ▼
Amazon Polly
  │
  ▼
S3 Destination Bucket (MP3 Audio)

**Security Architecture**
- IAM role with least privilege access
- S3 bucket access controlled using policies
- No hardcoded credentials
- Environment variables used for configuration

**Scalability Design**
- Lambda auto-scales automatically.
- Serverless architecture removes infrastructure management.
- Supports large number of file uploads concurrently.

**Error Handling Strategy**
- CloudWatch Logs used for monitoring.
- Try/Except blocks implemented in Lambda.
- Failed executions visible via Lambda monitoring.

**Future Improvements**
- Add SQS queue for buffering uploads.
- Add Step Functions workflow.
- Support multiple languages.
- API Gateway integration.
- Web frontend dashboard.
