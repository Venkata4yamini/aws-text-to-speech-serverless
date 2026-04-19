# ⚙️ Setup Guide — AWS Text-to-Speech Serverless

This guide explains how to deploy and run the **Serverless Text-to-Speech** project using AWS services.

---

## 📋 Prerequisites

Before starting, ensure you have:

- AWS Account
- IAM permissions to create Lambda, S3, and Polly resources
- Python 3.10+
- Git installed
- AWS Management Console access

---

## 🪣 Step 1 — Create S3 Buckets

Create **two S3 buckets**.

### Source Bucket
Stores uploaded text files.

Example:
source-polly-audio-bucket

### Destination Bucket
Stores generated audio files.

Example:
destination-polly-audio-bucket

---

## 🔐 Step 2 — Create IAM Role

Create an IAM Role for Lambda execution.

### Required Permissions

#### S3 Permissions
- s3:GetObject
- s3:PutObject
- s3:ListBucket

#### Amazon Polly Permission
- polly:SynthesizeSpeech

Attach this IAM Role to the Lambda function.

---

## ⚡ Step 3 — Create Lambda Function

1. Open AWS Lambda Console
2. Click **Create Function**
3. Select **Author from scratch**
4. Runtime → Python 3.10
5. Attach created IAM Role

Function Name:
TextToSpeechFunction

---

## 🌎 Step 4 — Add Environment Variables

Go to:

Lambda → Configuration → Environment Variables

Add the following variables:

| Key | Value |
|-----|------|
| SOURCE_BUCKET | source-polly-audio-bucket |
| DESTINATION_BUCKET | destination-polly-audio-bucket |
| VOICE_ID | Joanna |
| OUTPUT_FORMAT | mp3 |

---

## 🔔 Step 5 — Configure S3 Trigger

1. Open Lambda Function
2. Click **Add Trigger**
3. Select **S3**
4. Choose Source Bucket
5. Event Type → Object Created (All)

Lambda will now automatically trigger when a text file is uploaded.

---

## 📂 Step 6 — Upload Text File

Upload a `.txt` file into the source bucket.

Example:
oracle.txt

---

## 🔊 Step 7 — Verify Output

After upload, check the destination bucket.

Expected Output:
oracle.mp3

Audio file generated using Amazon Polly.

---

## 📊 Architecture Flow

User Upload  
↓  
Amazon S3 (Source Bucket)  
↓  
AWS Lambda Trigger  
↓  
Amazon Polly Text-to-Speech  
↓  
Amazon S3 (Destination Bucket)

---

## 🧪 Testing

Upload sample text file:

Hello this is AWS Serverless Text to Speech Project.

Verify that the audio file is generated successfully.

---

## 🛠 Troubleshooting

### AccessDenied Error
- Verify IAM Role permissions
- Ensure S3 and Polly permissions are attached

### Lambda Not Triggering
- Check S3 Event Notification configuration

### No Audio Output
- Review CloudWatch Logs

---

## 🚀 Future Improvements

- API Gateway integration
- Batch processing
- Multi-language voice support
- Queue-based scalable processing using SQS
- Web upload interface

---

## 👩‍💻 Author

Venkata Yamini  
Cloud Security & Serverless Developer
