from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def getFontPages(year, newspaper_url, startMonth='01', endMonth='12'):
    print('Searching for Font Pages...')
    fontPages = []
    fontPages_no_repeated = []
    req = Request(
        f"https://arquivo.pt/textsearch?versionHistory={newspaper_url}&prettyPrint=true&maxItems=5000&from={year}{startMonth}01000000&to={year}{endMonth}31235900")
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "html.parser")
    html_text = soup.text

    html_text = html_text.replace('","', '\n')

    for line in html_text.splitlines():
        if 'linkToNoFrame":' in line:
            fontPages.append(line)

    for i in range(len(fontPages)):
        fontPages[i] = fontPages[i].replace('linkToNoFrame":"', '')

    for i in fontPages:
        if i not in fontPages_no_repeated:
            fontPages_no_repeated.append(i)

    print(f'Font Pages Found for {year}: ' + str(len(fontPages_no_repeated)))

    return fontPages_no_repeated