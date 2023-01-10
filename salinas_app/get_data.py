import requests
import pandas as pd

datatset_id = "anonymized-crime-data"
url = "https://cityofsalinas.opendatasoft.com/api/v2/catalog/exports/json?limit=-1&offset=0&timezone=UTC"


resp = requests.get(url)

#%%

