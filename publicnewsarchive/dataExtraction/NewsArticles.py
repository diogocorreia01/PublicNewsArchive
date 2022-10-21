import requests
from bs4 import BeautifulSoup
import json
import os
def getNewsArticles(pastURLs, news_htmlTag, news_htmlClass, titles_htmlTag, titles_htmlClass, snippets_htmlTag, snippets_htmlClass,
             links_htmlTag, links_htmlClass, authors_htmlTag, authors_htmlClass, filename, debug=False):

    dictOfTags = {'Title': [titles_htmlTag, titles_htmlClass],
                  'Snippet': [snippets_htmlTag, snippets_htmlClass],
                  'Link': [links_htmlTag, links_htmlClass],
                  'Author': [authors_htmlTag, authors_htmlClass]}

    ListOfContents = []
    ListOfProcessedLinks = []

    for i in range(len(pastURLs)):
        page = requests.get(pastURLs[i])
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="UTF-8")
        ListOfTagContents = soup.find_all(news_htmlTag, class_=news_htmlClass)
        for content in ListOfTagContents:
            dictOfFeatures = {}
            for key in dictOfTags:
                try:
                    if key == "Link":
                        link = content.find(dictOfTags[key][0], class_=dictOfTags[key][1]).get("href").strip()
                        if link.startswith('/noFrame/replay/'):
                            link = link.replace('/noFrame/replay/', 'https://arquivo.pt/wayback/')
                        dictOfFeatures[key] = link
                    else:
                        dictOfFeatures[key] = content.find(dictOfTags[key][0], class_=dictOfTags[key][1]).get_text().strip()
                except:
                    dictOfFeatures[key] = ' '
            if link not in ListOfProcessedLinks:
                ListOfProcessedLinks.append(link)
                ListOfContents.append(dictOfFeatures)

        if debug == True:
            if i != 0 and i % 1 == 0:
                print(f"\r{100 * i / len(pastURLs):.2f}%", end='')
                if i == len(pastURLs) - 1:
                    print(f"\r100.00%", end='')
    path = "data/"

    if not os.path.exists(path):
        os.makedirs(path)

    with open(f'{path + filename}', 'w', encoding='utf-8') as fp:
        json.dump(ListOfContents, fp, indent=4, ensure_ascii=False)