# Free Music Archive

To extract data from the free music archive, you can go to this link (https://github.com/mdeff/fma), and download the following directories:
  * fma_small
  * fma_metadata

The fma_small is the small version of the entire free music archive dataset. It contains 8,000 mp3 music files, and each file falls into one of eight genre categories (by top most genre in the hierarchy):
  * Pop
  * Hip-Hop
  * International
  * Electronic
  * Instrumental
  * Experimental
  * Rock
  * Folk

Addtionally, the fma_small dataset is a balanced dataset so each genre category will have 1,000 files. Once you download the dataset, run the load_fma_metadata.py script so that you can extract the necessary information from the fma_metadata directory and save it as a csv file. Afterwards you can run the load_fma_music.py script with the provided parameters; --n_pop for the number of pop songs, and --n_rock for the number of rock songs to sample.
