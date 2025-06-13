from flask import Flask
import os
import logging
from google.cloud import storage

# Enable logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def serve_file():
    logging.info("Handling request to /")

    project_id = os.environ.get("PROJECT_ID")
    bucket_name = "optimus-os-v2-constitution"
    file_name = "constitution.txt"

    try:
        client = storage.Client(project=project_id)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        content = blob.download_as_text()
        return f"<pre>{content}</pre>"
    except Exception as e:
        logging.error(f"Error: {e}")
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
