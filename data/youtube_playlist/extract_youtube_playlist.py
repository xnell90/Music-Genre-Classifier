import os

from pytube import Playlist
from tqdm import tqdm

#https://www.youtube.com/playlist?list=PLAk_fNQ79F8nVlhNHW1VAsiRIvf9knAKt
url = input("Enter the URL for the playlist: ")
playlist = Playlist(url)
playlist_dr = playlist.title + '/'

for video in tqdm(playlist.videos, desc='Downloading: ' + playlist.title):
    video.streams[0].download(playlist_dr)

mp4_files = os.listdir(playlist_dr)

print('Download Complete ...')
for file in mp4_files:
    print(file)

print("File Count: ", len(mp4_files))
