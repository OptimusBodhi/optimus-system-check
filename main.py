import functions_framework
from google.cloud import storage
import os

# The name of the bucket containing the Constitution.
# This is constructed from the project ID.
CONSTITUTION_BUCKET = os.environ.get('GCP_PROJECT') + '-constitution'

# The name of the file in the bucket.
# Please verify this is the exact filename you uploaded.
CONSTITUTION_FILE = "The Optimus Constitution.txt" 

@functions_framework.http
def optimus_core_handler(request):
    """The core identity function of the Optimus AI OS."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(CONSTITUTION_BUCKET)
        blob = bucket.blob(CONSTITUTION_FILE)

        print(f"Attempting to retrieve gs://{CONSTITUTION_BUCKET}/{CONSTITUTION_FILE}")
        constitution_content = blob.download_as_text()
        print("Successfully retrieved the Constitution.")

        return (f"--- Optimus AI OS: Core Identity Protocol ---\n\n{constitution_content}", 200)

    except Exception as e:
        print(f"CRITICAL ERROR: Could not retrieve the Constitution. - {e}")
        error_message = f"ERROR: The core governing document could not be retrieved. Ensure the bucket '{CONSTITUTION_BUCKET}' and file '{CONSTITUTION_FILE}' exist and that this service has the correct permissions. Details: {e}"
        return (error_message, 500)
