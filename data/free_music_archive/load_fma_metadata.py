import pandas as pd

fma_metadata = pd.read_csv(
    'fma_metadata/tracks.csv',
    index_col=0,
    header=[0, 1]
)
fma_small = fma_metadata['set', 'subset'] == 'small'
fma_small_metadata = fma_metadata[fma_small][[['track', 'genre_top']]]
fma_small_metadata.columns = fma_small_metadata.columns.get_level_values(1)
fma_small_metadata.reset_index(inplace=True)
fma_small_metadata.to_csv('fma_small_metadata.csv', index=False)
