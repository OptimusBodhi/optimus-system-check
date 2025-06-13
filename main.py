from flask import Flask
import os
from google.cloud import storage

app = Flask(__name__)

@app.route("/")
def serve_file():
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
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
