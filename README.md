📦 S3 Bucket File Lister
This Python script uses boto3 to connect to Amazon S3 and list all objects inside a specified bucket.
🔧 Features
- Connects to AWS S3 using the boto3 SDK
- Lists all files stored in a given bucket
- Handles empty buckets gracefully with an informative message

📋 Requirements
Make sure you have the following installed:
- Python 3.x
- Boto3 (pip install boto3)
- AWS credentials configured (~/.aws/credentials) or environment variables set

🚀 How to Run
python s3_lister.py

You’ll be prompted to enter an S3 bucket name:
Enter the S3 bucket name: my-awesome-bucket
Files in my-awesome-bucket:
data.json
report.pdf
images/photo.jpg

🧠 How It Works
def list_s3_objects(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No files found.")


📁 File Structure
s3_lister.py
README.md


🛡️ Disclaimer
This script assumes that you have proper permissions to access the specified bucket. Make sure your IAM roles and credentials are correctly configured.
