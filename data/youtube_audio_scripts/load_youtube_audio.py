import os

from pydub import AudioSegment
from random import randrange
from tqdm import tqdm

playlist_dr = input("Enter Playlist Directory: ") #Star Wars Original Trilogy Soundtrack
genre = input("Enter Genre: ") #soundtrack

playlist_dr += '/'
parent_working_dr = os.path.dirname(os.getcwd())
mp4_files= os.listdir(playlist_dr)

i = 0
for file in tqdm(mp4_files, 'Loading Files: '):
    audio = AudioSegment.from_file(playlist_dr + file)

    start = randrange(len(audio) -  10000)
    end = start + 10000
    audio_sample = audio[start:end]

    i += 1
    new_filename = "2_" + '{:06d}'.format(i) + "_0" + ".wav"
    folder_location = parent_working_dr + "/genres/" + genre + '/'

    audio_sample.export(folder_location + new_filename, format="wav")
