import requests
from requests.exceptions import Timeout
def getPastURLs(year, newspaper_url, startMonth='01', endMonth='12'):

    url_api = 'https://arquivo.pt/textsearch'

    versionHistory = newspaper_url
    maxItems = '5000'
    fromDate = f'{year}{startMonth}01000000'
    toDate = f'{year}{endMonth}31235959'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0 "}
    payload = {'versionHistory': versionHistory, 'maxItems': maxItems, 'from': fromDate, 'to': toDate}

    try:
        r = requests.get(url_api, params=payload, headers=headers, timeout=60)
    except Timeout:
        print('Timeout has been raised.')

    content = r.json()

    pastURLs = []

    for item in content['response_items']:
        pastURLs.append(item['linkToNoFrame'])

    return list(set(pastURLs))