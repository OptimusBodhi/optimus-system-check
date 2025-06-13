print("--- SCRIPT START: main.py is being executed. ---")
import functions_framework
from google.cloud import storage
import os

CONSTITUTION_BUCKET = os.environ.get('GOOGLE_CLOUD_PROJECT') + '-constitution'
CONSTITUTION_FILE = "constitution.txt"

@functions_framework.http
def optimus_core_handler(request):
    """A diagnostic function to check for a file's existence and metadata."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(CONSTITUTION_BUCKET)
        blob = bucket.blob(CONSTITUTION_FILE)

        # Instead of reading the file, just check if it exists
        if blob.exists():
            # Reload metadata to get size, etc.
            blob.reload() 
            file_size = blob.size
            message = f"--- DIAGNOSTIC SUCCESS ---\n\nFile '{CONSTITUTION_FILE}' exists in bucket '{CONSTITUTION_BUCKET}'.\nFile size: {file_size} bytes."
            print(message)
            return (message, 200)
        else:
            error_message = f"--- DIAGNOSTIC FAILURE ---\n\nFile '{CONSTITUTION_FILE}' was NOT FOUND in bucket '{CONSTITUTION_BUCKET}'."
            print(error_message)
            return (error_message, 404)

    except Exception as e:
        print(f"CRITICAL ERROR during diagnostic. - {e}")
        error_message = f"CRITICAL ERROR: An unexpected exception occurred. Details: {e}"
        return (error_message, 500)


