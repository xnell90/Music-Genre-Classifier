import os

from pydub import AudioSegment
from random import randrange
from tqdm import tqdm

playlist_dr = input("Enter Playlist Directory: ") #Star Wars Original Trilogy Soundtrack
playlist_dr += '/'
parent_working_dr = os.path.dirname(os.getcwd())

genre = input("Enter Genre: ") #soundtrack
mp4_files = os.listdir(playlist_dr)

k = 0
for file in tqdm(mp4_files, 'Loading Files: '):
    audio = AudioSegment.from_file(playlist_dr + file)

    i = randrange(len(audio) -  10000)
    j = i + 10000
    audio_sample = audio[i:j]

    i += 1
    new_file = "2_" + '{:06d}'.format(k) + "_0.wav"
    new_file_location = parent_working_dr + "/genres/" + genre + '/' + new_file

    audio_sample.export(new_file_location, format="wav")
