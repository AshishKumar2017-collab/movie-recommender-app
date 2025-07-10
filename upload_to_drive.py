from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Path to your file
file_to_upload = "similarity.pkl"

if not os.path.exists(file_to_upload):
    raise FileNotFoundError(f"❌ File not found: {file_to_upload}")

# Upload it to Google Drive
gfile = drive.CreateFile({'title': file_to_upload})
gfile.SetContentFile(file_to_upload)
gfile.Upload()

print(f"✅ Uploaded '{file_to_upload}' to Google Drive.")
print(f"🔗 File link: https://drive.google.com/file/d/{gfile['id']}/view")
