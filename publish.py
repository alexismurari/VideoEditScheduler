from operator import mod
import os
from os import listdir
from os.path import isfile, join
import sys
import argparse

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def schedule_video(path, video, month, day, hour, youtube):
    request = youtube.videos().insert(
        part="snippet,status",

        body=dict(
            snippet=dict(
                title=video + " #shorts",
                description="Best Gaming Clips!",
                tags="csgo, valorant, gaming, clips, memes, gameplay, gamer, pc, youtubegaming channel",
                categoryId="20"
            ),
            status=dict(
                privacyStatus="private",
                selfDeclaredMadeForKids = "false",
                publishAt="2022-" + month + "-" + day + "T" + str(hour) + ":0:00.000+00:00"
                #publishAt="2022-11-01T8:0:00.000+00:00"
            )
        ),
        media_body=MediaFileUpload(path + video)
    )
    response = request.execute()

    print(response)


def main(args):
    new_videos_path = args.src
    new_videos = [f for f in listdir(new_videos_path) if isfile(join(new_videos_path, f))]
    print(new_videos)

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


    month = "08"
    day = "01"
    hour = 0

    while int(day) < 31:
        for vid in new_videos:
            schedule_video(new_videos_path, vid, month, day, hour, youtube)
            hour += 1
            if hour == 24:
                day = str(int(day) + 1)
                if day <= str(9): day = "0" + day
            hour = mod(hour, 24)

            print(month, day, hour)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", action="store_true", help="archive mode", default=False)
    parser.add_argument("src", help="Source location")
    parser.add_argument("dest", help="Destination location")
    args = parser.parse_args()

    main(args)