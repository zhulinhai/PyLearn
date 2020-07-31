
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)

data = resp.json()

print(data[0].avatar_url)
