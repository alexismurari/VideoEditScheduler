import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",

        body=dict(
            snippet=dict(
                title="csgo",
                description="",
                tags="csgo",
                categoryId="20"
            ),
            status=dict(
                privacyStatus="private",
                publishAt="2022-11-01T8:20:00.000+00:00"
            )
        ),
        # body={
        #   "snippet": {
        #     "categoryId": "22",
        #     "description": "Description of uploaded video.",
        #     "title": "Test video upload."
        #   },
        #   "status": {
        #     "privacyStatus": "private"
        #   }
        # },
        
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("edit/csgo.mp4")
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()