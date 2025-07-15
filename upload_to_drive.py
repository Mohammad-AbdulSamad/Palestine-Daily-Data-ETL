import os
import json
import glob
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

FOLDER_ID = os.getenv("GDRIVE_FOLDER_ID")

def upload_to_drive(filename, creds_json):
    creds_dict = json.loads(creds_json)
    creds = service_account.Credentials.from_service_account_info(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": os.path.basename(filename),
        "parents": [FOLDER_ID]
    }
    media = MediaFileUpload(filename, resumable=True)

    # Check if file already exists in Drive (by name)
    results = service.files().list(q=f"name='{os.path.basename(filename)}' and '{FOLDER_ID}' in parents",
                                   fields="files(id)").execute()
    files = results.get("files", [])
    if files:
        # Update existing file
        file_id = files[0]["id"]
        service.files().update(fileId=file_id, media_body=media).execute()
        print(f"🔁 Updated file: {filename}")
    else:
        # Upload new file
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        print(f"✅ Uploaded new file: {filename}")


if __name__ == "__main__":
    creds_json = os.getenv("GDRIVE_CREDENTIALS_JSON")
    for file in glob.glob("data/*.csv"):
        upload_to_drive(file, creds_json)
