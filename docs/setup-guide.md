⚙️ Setup Guide — AWS Text-to-Speech Serverless

This guide explains how to deploy and run the Serverless Text-to-Speech project using AWS services.

**Prerequisites**

Before starting, make sure you have:

1.AWS Account
2IAM permissions to create Lambda, S3, and Polly resources
3.Python 3.10+
4.Git installed
5.AWS Console access

**🪣 Step 1 — Create S3 Buckets**

Create two S3 buckets:

Source Bucket

Stores uploaded text files.

Example:

source-polly-audio-bucket
Destination Bucket

Stores generated audio files.

Example:

destination-polly-audio-bucket

**🔐 Step 2 — Create IAM Role**

Create an IAM Role for Lambda with the following permissions:

S3 Permissions
s3
s3
s3
Polly Permission
polly

Attach policy to Lambda execution role.

**⚡ Step 3 — Create Lambda Function**

Open AWS Lambda Console
Click Create Function
Runtime → Python 3.10
Attach created IAM Role

Function name:

TextToSpeechFunction

**🌎 Step 4 — Add Environment Variables**

Go to:

Lambda → Configuration → Environment Variables

Add:

Key	Value
SOURCE_BUCKET	source-polly-audio-bucket
DESTINATION_BUCKET	destination-polly-audio-bucket
VOICE_ID	Joanna
OUTPUT_FORMAT	mp3

**🔔 Step 5 — Configure S3 Trigger**

Open Lambda
Add Trigger
Select S3
Choose Source Bucket
Event Type → Object Created (All)

Now Lambda triggers automatically when a text file is uploaded.

**📂 Step 6 — Upload Text File**

Upload a .txt file into source bucket.

Example:

oracle.txt

**🔊 Step 7 — Verify Output
**
After upload:

Destination bucket will contain:

oracle.mp3

Audio generated using Amazon Polly.

**📊 Architecture Flow**
User Upload
      ↓
Amazon S3 (Source Bucket)
      ↓
AWS Lambda Trigger
      ↓
Amazon Polly Text-to-Speech
      ↓
Amazon S3 (Destination Bucket)

**🧪 Testing**

Upload sample file:

Hello this is AWS Serverless Text to Speech Project.

Verify audio generation.

**🛠 Troubleshooting**
AccessDenied Error

Check IAM role permissions.

Lambda Not Triggering

Verify S3 event notification configuration.

No Audio Output

Check CloudWatch Logs.

**🚀 Future Improvements**
API Gateway integration
Batch processing
Multi-language voice support
Queue-based scalable processing
Web upload interface

**👩‍💻 Author**
Venkata Yamini

Cloud Security & Serverless Developer
