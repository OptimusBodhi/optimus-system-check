import os
from google.cloud import storage

# Manually injected project ID fallback
project_id = os.environ.get("PROJECT_ID")
bucket_name = "optimus-os-v2-constitution"
file_name = "constitution.txt"

client = storage.Client(project=project_id)
bucket = client.bucket(bucket_name)
blob = bucket.blob(file_name)
content = blob.download_as_text()

print("✅ Successfully read file from Cloud Storage:")
print(content)
