"""A simple YouTube Music download script.

This script downloads song or album from Youtube Music.

Dependency:
    pip install pytube
"""
from pytube import YouTube, Playlist
import os
import sys


def download_playlist(link, filename):
    """
    Download songs in playlist.

    Args:
        link: Playlist URL.
        filename: Destination for downloaded files.
    """
    try:
        playlist = list(Playlist(link))
        for i in range(len(playlist)):
            song = YouTube(playlist[i], use_oauth=True, allow_oauth_cache=True)
            downloader(song, filename)

    except:
        print("Error: Please check the filepath or URL [album]")


def download_single(link, filename):
    """
    Download a single song

    Args:
        link: URL of the song.
        filename: Destination for downloaded file.
    """
    print(link)
    try:
        song = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        downloader(song, filename)
    except:
        print("Error: Please check the filepath or URL [singles]")


def downloader(song, filename):
    """
    Download audio from YouTube Music and convert output file extension from .mp4 to .mp3.

    Args:
        link: URL of YouTube video
        filename: Destination for downloaded file.
    """
    # Download the audio from the URL
    try:
        print(f"Downloading: {song.title}")
        out_file = song.streams.get_audio_only().download(output_path=filename)
    except:
        print("An error has occurred during download [downloader]")
        sys.exit(1)

    # Change the file extension from .mp4 to .mp3
    # Files are corrupted .mp3 that can only be play on computer
    # Use VLC media player to convert to .mp3 
    # try:
    #     print(f"Converting {song.title} to .mp3")
    #     base, ext = os.path.splitext(out_file)
    #     new_file = base + ".mp3"
    #     # os.rename(out_file, new_file)
    # except:
    #     print("An error has occurred during filename convertion")
    #     sys.exit(1)

    print(f"{song.title} completed!\n{'=' * 50}")


def change_url(url):
    """
    Convert "music.youtube.com" to "youtu.be"

    Args:
        url: YouTube Music URL

    Returns:
        Updated url string with "youtu.be".
    """

    addr = "youtube.com"
    new_url = url.replace("music.youtube.com", addr)
    if not addr in new_url:
        print("Error: Invalid URL")
        sys.exit(1)
    return new_url

def run():
    is_playlist = input("Are you downloading a playlist (y/n)? ").lower() == "y"
    url = input("Enter YouTube Music URL: ")
    filename = input("Where do you want to save the file? ")

    if is_playlist:
        download_playlist(url, filename)
    else:
        download_single(url, filename)

if __name__ == "__main__":
    run()