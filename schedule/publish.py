from operator import mod
import os
from os import listdir
from os.path import isfile, join
import argparse
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def schedule_video(path, video, month, day, hour, youtube):
    request = youtube.videos().insert(
        part="snippet,status",

        body=dict(
            snippet=dict(
                title=video[:-4] + " #shorts",
                description="Best Gaming Clips! #shorts #shortsvideo #shortsfeed #shortsyoutube #comedy #news",
                tags="csgo, valorant, gaming, clips, memes, gameplay, gamer, pc, youtubegaming channel",
                categoryId="20"
            ),
            status=dict(
                privacyStatus="private",
                selfDeclaredMadeForKids = "false",
                publishAt="2022-" + month + "-" + day + "T" + str(hour) + ":0:00.000-04:00"
            )
        ),
        media_body=MediaFileUpload(path + "/" + video)
    )
    response = request.execute()

    print(response)


def get_creds(credentials):
    client_secrets_file = "schedule/client_secret.json"

    if os.path.exists('schedule/token.pickle'):
        with open('schedule/token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)

            flow.run_local_server(port=8080, prompt="consent", authorization_prompt_message="")

            credentials = flow.credentials

            with open('schedule/token.pickle', 'wb') as f:
                pickle.dump(credentials, f)

    print(credentials)

    return credentials



def schedule(new_videos_path, date = (0,0,0)):
    print("Opened: ", new_videos_path)
    credentials = None
    
    new_videos = [f for f in listdir(new_videos_path) if isfile(join(new_videos_path, f))]
    print(new_videos)

    credentials = get_creds(credentials)


    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

    month = str(date[1])
    day = str(date[2])
    hour = 0

    for vid in new_videos:
        schedule_video(new_videos_path, vid, month, day, hour, youtube)
        hour += 3
        if hour == 24:
            day = str(int(day) + 1)
            if day <= str(9): day = "0" + day
        hour = mod(hour, 24)

        print(month, day, hour)


def parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", action="store_true", help="archive mode", default=False)
    parser.add_argument("src", help="Source location")
    args = parser.parse_args()

    return args

def main():
    args = parser_args()
    new_videos_path = args.src
    schedule(new_videos_path)


if __name__ == "__main__":
    main()