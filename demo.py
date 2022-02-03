
import urllib3

import requests

link = "https://youtube.com"
data = requests.request("GET", link)
url = data.url