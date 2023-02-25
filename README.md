# youtube_downloader
Download song or album using pytube library.

## Usage
```
python3 yt_downloader.py
Are you downloading a playlist (y/n)? <y or n>
Enter YouTube video URL: <music.youtube.com URL>
Where do you want to save the file? <destination_filepath>
```
### Example:
To download playlist/album and create a sub-directory in current location:
```
python3 yt_downloader.py
Are you downloading a playlist (y/n)? y
Enter YouTube video URL: <music.youtube.com URL>
Where do you want to save the file? ./<playlist_name>
```

## Notes
No validation check for filepath or URL. So be sure to provide correct inputs.

## Checklist:
- [x] Download only song
- [x] Download songs in playlist or album
- [] Create GUI
- [] Validate URL
- [] Validate filepath 
