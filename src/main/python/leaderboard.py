#!/home/bin/python

from urllib.request import urlopen
import json

url = "https://www.hackerrank.com/rest/contests/daybyday/leaderboard?offset=0&limit=100&_=1538404999096"
response = urlopen(url)
data = json.loads(response.read())

for model in data["models"] :
    id = model["hacker_id"]
    name = model["hacker"]
    score = model["score"]
    rank = model["rank"]

