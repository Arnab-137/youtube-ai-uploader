from googleapiclient.discovery import build

from auth.youtube_auth import authenticate


def get_youtube():

    credentials = authenticate()

    youtube = build(
        "youtube",
        "v3",
        credentials=credentials
    )

    return youtube
