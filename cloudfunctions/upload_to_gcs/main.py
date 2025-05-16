import os
from google.cloud import storage

def upload_files_to_gcs(bucket_name, local_folder):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for filename in os.listdir(local_folder):
        if filename.endswith(".csv"):
            local_path = os.path.join(local_folder, filename)
            blob = bucket.blob(f"raw/{filename}")
            blob.upload_from_filename(local_path)
            print(f"✅ {filename} cargado a gs://{bucket_name}/raw/{filename}")

if __name__ == "__main__":
    bucket = "bucket-procurement-analytics"  # Reemplaza por tu bucket real
    folder = "../../data"
    upload_files_to_gcs(bucket, folder)
