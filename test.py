import pytest
import requests
url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
presidents = [" Washington", " Adams", " Jefferson", " Madison", " Monroe", " Adams", " Jackson", " Buren", " Harrison", " Tyler", " Polk", " Taylor", " Fillmore", " Pierce",  " Buchanan", " Lincoln", " Johnson", " Grant", " Hayes", " Garfield", " Arthur", " Cleveland", " Harrison", " Cleveland", " McKinley", " Roosevelt", " Taft",  " Wilson", " Harding", " Coolidge", " Hoover", " Roosevelt", " Truman", " Eisenhower", " Kennedy", " Johnson", " Nixon", " Ford", " Carter", " Reagan", " Bush",  " Clinton", " Obama", " Trump", " Biden"]

def test_DuckDuckGo():
  r = requests.get(url)
  resp_data = r.json()
  for x in presidentsList:
    assert x in str(resp_data)
