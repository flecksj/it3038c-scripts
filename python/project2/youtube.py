from pytube import YouTube

# where to save
SAVE_PATH = "C:/Users/Sam Fleck/PycharmProjects/pythonProject"


link = input("Enter the link of YouTube video you want to download:  ")

from pytube import YouTube

youtube_video_url = link

try:
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    filters.get_highest_resolution().download()
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
