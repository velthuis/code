import pandas as pd
from urllib.request import urlopen
import json

# read website contents
url = "http://www.floatrates.com/daily/usd.json"
response = urlopen(url)

# read json 
data_json = json.loads(response.read())

# store in dataframe
df = pd.DataFrame.from_dict(data_json)
df = df.transpose()

# export to Excel
df.to_excel('C:/Users/rvelthui/Documents/My Python Files/USD.xlsx')