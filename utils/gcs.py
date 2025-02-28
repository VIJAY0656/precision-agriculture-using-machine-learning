from google.cloud import storage

# Initialize Google Cloud Storage client
client = storage.Client.from_service_account_json('omega-strand-452308-a4-7c12af5094fe.json')

def upload_file(bucket_name, file_obj, destination_blob_name):
    """
    Uploads a file to the specified GCS bucket.
    
    :param bucket_name: Name of the GCS bucket.
    :param file_obj: File object to upload.
    :param destination_blob_name: Path in GCS where the file will be stored.
    """
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(file_obj)
    return f"File {destination_blob_name} uploaded to {bucket_name}."

def download_file(bucket_name, source_blob_name):
    """
    Downloads a file from GCS and returns its content.
    
    :param bucket_name: Name of the GCS bucket.
    :param source_blob_name: Path in GCS where the file is stored.
    :return: File content.
    """
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    return blob.download_as_bytes()

def list_files(bucket_name):
    """
    Lists all files in a GCS bucket.
    
    :param bucket_name: Name of the GCS bucket.
    :return: List of file names.
    """
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    return [blob.name for blob in blobs]