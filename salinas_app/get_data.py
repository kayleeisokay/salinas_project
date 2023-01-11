import requests
import pandas as pd
import json

import warnings
warnings.filterwarnings('ignore')

datatset_id = "anonymized-crime-data"
limit = -1
offset = 0

url = "https://cityofsalinas.opendatasoft.com/api/v2/catalog/datasets/{dataset_id}/exports/json?limit={limit}&offset={offset}&timezone=UTC".format(dataset_id=datatset_id, limit=limit, offset=offset)
resp = requests.get(url)

resp_string = resp.content.decode("utf-8")
crime_df = pd.json_normalize(json.loads(resp_string ))

year, month, day = crime_df['occdate_on'].str.split('T').str[0].str.split('-').str

crime_df['year'] = pd.Series(year).astype(int)
crime_df['month'] = pd.Series(month).astype(int)
crime_df['day'] = pd.Series(day).astype(int)

cols = [
    'crime',
    'year',
    'month',
    'day',
]

crime_df[cols].to_csv('./seeds/crime_data.csv', index=False)