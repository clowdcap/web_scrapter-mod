
import gmaps
import gmaps.datasets

GOOGLE_API_KEY='AIzaSyAwDLsERC_bzD1jupvSD-ke19v1VIttIKA'

gmaps.configure(api_key=GOOGLE_API_KEY)

earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()


