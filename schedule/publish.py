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

from  datetime import datetime, timezone

scopes = ["https://www.googleapis.com/auth/youtube.upload"]


def convert_time(date, time):
    
    year, month, day = date
    hour, minute = time
    isoTime = datetime(year,month,day,hour,minute,0, 0)
    isoTime = isoTime.astimezone()

    return isoTime.isoformat()

def schedule_video(path, video, time, youtube):

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
                publishAt=time
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

    return credentials



def schedule(new_videos_path, date, time):
    print("Opened: ", new_videos_path)
    credentials = None
    
    new_videos = [f for f in listdir(new_videos_path) if isfile(join(new_videos_path, f))]
    print(new_videos)

    credentials = get_creds(credentials)
    
    publishTime = convert_time(date, time)

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

    for vid in new_videos:
        publishTime = convert_time(date, time)
        date[2] += 1
        schedule_video(new_videos_path, vid, publishTime, youtube)
        print(date, time)


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