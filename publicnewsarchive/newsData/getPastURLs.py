from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def getPastURLs(year, newspaper_url, startMonth='01', endMonth='12'):
    print('Searching for Past URLs...')
    pastURLs = []
    pastURLs_no_repeated = []
    req = Request(
        f"https://arquivo.pt/textsearch?versionHistory={newspaper_url}&prettyPrint=true&maxItems=5000&from={year}{startMonth}01000000&to={year}{endMonth}31235900")
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "html.parser")
    html_text = soup.text

    html_text = html_text.replace('","', '\n')

    for line in html_text.splitlines():
        if 'linkToNoFrame":' in line:
            pastURLs.append(line)

    for i in range(len(pastURLs)):
        pastURLs[i] = pastURLs[i].replace('linkToNoFrame":"', '')

    for i in pastURLs:
        if i not in pastURLs_no_repeated:
            pastURLs_no_repeated.append(i)

    print(f'Past URLs Found for {year}: ' + str(len(pastURLs_no_repeated)))

    return pastURLs_no_repeated