from flask import Flask
import os
import logging
from google.cloud import storage

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def serve_file():
    logging.info("Handling request to the root URL /")

    # We will hardcode the bucket name for simplicity and robustness
    bucket_name = "optimus-os-v2-constitution" 
    file_name = "constitution.txt"

    try:
        # In Cloud Run, storage.Client() automatically finds the credentials
        # from the service account the service is running as. No key file needed.
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)

        logging.info(f"Attempting to download gs://{bucket_name}/{file_name}")
        content = blob.download_as_text()

        logging.info("Successfully downloaded file.")
        return f"<pre>--- Optimus AI OS: Core Identity Protocol ---\n\n{content}</pre>"

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        logging.error(error_message)
        return error_message, 500
