# 🎙️ AWS Serverless Text-to-Speech Converter

A Serverless Cloud Application that automatically converts uploaded text files into speech audio using AWS Lambda, Amazon Polly, and Amazon S3.

This project demonstrates event-driven architecture, serverless computing, and cloud automation using AWS services.

---

## 🚀 Project Overview

This application automatically performs the following:

1. User uploads a `.txt` file to an S3 bucket.
2. Amazon S3 triggers an AWS Lambda function.
3. Lambda reads the text file.
4. Amazon Polly converts text into speech.
5. Generated audio file is stored in a destination S3 bucket.

No servers. No manual processing. Fully automated workflow.

---

## 🏗️ Architecture

User Upload  
↓  
Amazon S3 (Source Bucket)  
↓  
S3 Event Trigger  
↓  
AWS Lambda Function  
↓  
Amazon Polly (Text-to-Speech)  
↓  
Amazon S3 (Destination Bucket)

---

## ☁️ AWS Services Used

- Amazon S3 — File storage
- AWS Lambda — Serverless compute
- Amazon Polly — Text-to-Speech conversion
- AWS IAM — Access management
- Amazon CloudWatch — Logging and monitoring

---

## ⚙️ Features

- Fully Serverless Architecture
- Event Driven Processing
- Automatic Audio Generation
- Environment Variable Configuration
- Secure IAM Role Permissions
- Scalable Cloud Design

---

## 🧪 How It Works

1. Upload a text file:

oracle.txt

2. Lambda automatically executes.

3. Output generated:

oracle.mp3

The audio file will be stored inside the destination S3 bucket.

---

## 🌎 Environment Variables

| Variable | Description |
|----------|-------------|
| SOURCE_BUCKET | Input S3 bucket |
| DESTINATION_BUCKET | Output S3 bucket |
| VOICE_ID | Polly voice |
| OUTPUT_FORMAT | Audio format |

---

## 🔐 IAM Permissions Required

### S3 Permissions
- s3:GetObject
- s3:PutObject
- s3:ListBucket

### Amazon Polly Permission
- polly:SynthesizeSpeech

---

## ▶️ Deployment Guide

Follow detailed setup instructions in:

setup-guide.md

---

## 📊 Sample Use Cases

- Audio book generation
- Blog-to-audio automation
- Accessibility solutions
- Podcast automation
- Learning narration systems

---

## 🚀 Future Enhancements

- API Gateway integration
- Web interface for uploads
- Multi-language speech support
- Queue-based processing using SQS
- Batch document processing
- CI/CD pipeline deployment

---

## 🧠 Skills Demonstrated

- AWS Serverless Architecture
- Cloud Security using IAM
- Event Driven Systems
- Python Automation
- Cloud Monitoring & Debugging
- Infrastructure Design

---

## 👩‍💻 Author

Venkata Yamini  

Cloud Security Engineer | Serverless Developer | AWS Enthusiast

---

## ⭐ Project Goal

To build a production-style AWS serverless application demonstrating scalable cloud architecture and automation using managed AWS services.

---

## 📜 License

This project is created for educational and demonstration purposes.
