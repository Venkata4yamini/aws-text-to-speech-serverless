import boto3
import os
import logging
import urllib.parse

# Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS clients
s3 = boto3.client('s3')
polly = boto3.client('polly')

def lambda_handler(event, context):

    source_bucket = os.environ['SOURCE_BUCKET']
    destination_bucket = os.environ['DESTINATION_BUCKET']

    logger.info(f"Listing files in bucket: {source_bucket}")

    # Get all objects from source bucket
    response = s3.list_objects_v2(Bucket=source_bucket)

    if 'Contents' not in response:
        logger.info("No files found.")
        return

    for obj in response['Contents']:

        key = obj['Key']

        # Process only text files
        if not key.endswith(".txt"):
            continue

        logger.info(f"Processing file: {key}")

        # Download text file
        file_obj = s3.get_object(Bucket=source_bucket, Key=key)
        text = file_obj['Body'].read().decode('utf-8')

        # Send text to Polly
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        audio_stream = response['AudioStream'].read()

        # Output file name
        output_key = key.replace(".txt", ".mp3")

        # Upload audio file
        s3.put_object(
            Bucket=destination_bucket,
            Key=output_key,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )

        logger.info(f"Converted {key} → {output_key}")

    return {
        "statusCode": 200,
        "body": "All files processed successfully"
    }
