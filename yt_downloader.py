"""
pip install pytube
"""
from pytube import YouTube
import os
import sys

def downloader(link, filename):
    """
    Download audio from YouTube video and convert it from .mp4 to .mp3.

    Args:
        link: URL of YouTube video
        filename: Filename for the downloaded audio
    """
    # Download the audio from the URL
    try:
        yt = YouTube(link)
        audio = yt.streams.get_audio_only()
        out_file = audio.download(output_path=filename)
    except:
        print("An error has occurred")
        sys.exit(1)

    # Change the file extension from .mp4 to .mp3
    try:
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except:
        print("An error has occurred during filename convertion")
        sys.exit(1)

    print("Title: ", yt.title)
    print("Download is completed successfully")

link = input("Enter YouTube video URL: ")
filename = input("Where do you want to save the file? ")
downloader(link, filename)

