# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=T_sPdgJfhaM"

from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=T_sPdgJfhaM'

try:
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    filters.get_highest_resolution().download()
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)