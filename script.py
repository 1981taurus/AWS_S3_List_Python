import boto3

def list_s3_objects(bucket_name):
    """
    This function lists all objects in a specified S3 bucket.
    :param bucket_name: The name of the S3 bucket to list files from.
    """
    s3 = boto3.client('s3')  # Connect to S3 using boto3
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if the bucket has any files
    if 'Contents' in response:
        print(f"Files in {bucket_name}:")
        for obj in response['Contents']:
            print(obj['Key'])  # Print each file name
    else:
        print("No files found.")

# Main Program
bucket_name = input("Enter the S3 bucket name: ")
list_s3_objects(bucket_name)
