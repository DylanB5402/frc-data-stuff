import requests_cache
import json
import auth_key

session = requests_cache.CachedSession("tba_data")

def get_data(data : str):
    header = { 'X-TBA-Auth-Key' : auth_key.key}
    tba_url = "https://www.thebluealliance.com/api/v3"
    response = session.get(tba_url + data, headers=header)
    tba_data = json.loads(response.content)
    return tba_data