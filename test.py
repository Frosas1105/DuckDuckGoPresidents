import pytest
import requests
url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
def test_DuckDuckGo():
  r = requests.get(url)
  resp_data = resp.json()
  for x in presidentsList:
    assert x in str(resp_data)
