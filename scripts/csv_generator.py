import pandas as pd
popular_times_1 = pd.read_csv('../data/popular_times_1.csv')
popular_times_2 = pd.read_csv('../data/popular_times_2.csv')
places = pd.read_csv('../data/places.csv')
data = pd.merge(pd.concat([popular_times_1, popular_times_2]), places)
data.to_pickle("../data/data.pkl")