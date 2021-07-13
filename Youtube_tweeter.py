import time
import tweepy
import re
import urllib.request
from apiclient.discovery import build
api_key = "YOUR API KEY"

channel_id = "YOUTUBE CHANNEL ID"

# Twitter_bits

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET_KEY'
ACCESS_KEY = 'YOUR_ACCESS_KEY'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET_KEY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

youtube = build('youtube', 'v3', developerKey=api_key)


def get_channel_videos(channel_id):

    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    for i in range(0, 1):
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=1,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos


videos = get_channel_videos(channel_id)
len(videos)
last_vid = " "
up = False

for video in videos:
    video['snippet']['title']
    html = urllib.request.urlopen(
        "https://www.youtube.com/channel/"+channel_id+"/videos?view=0&sort=dd&shelf_id=1")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    last_vid = "https://www.youtube.com/watch?v=" + video_ids[0]
    last_vid

FILE_NAME = 'last_vid.txt'


def get_last_vid(FILE_NAME):
    f_read = open(FILE_NAME, 'r')
    last_vid = str(f_read.read().strip())
    f_read.close()
    return last_vid


def save_last_vid(last_vid, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_vid))
    f_write.close()
    return


def video_link():
    if(get_last_vid(FILE_NAME) != last_vid):
        save_last_vid(last_vid, FILE_NAME)
        up = True
    else:
        up = False
    return up


def tweet_vid():
    if(video_link() == True):
        video_link()
        title = str(video['snippet']['title'])
        link = last_vid
        api.update_status(title+'   '+link)
        print(title+''+link)
    else:
        print("false")


while True:
    tweet_vid()
    time.sleep(15)
