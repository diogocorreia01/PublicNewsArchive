import requests
from bs4 import BeautifulSoup
import json

def getNewsArticles(pastURLs, newspaper_url, news_htmlTag, news_htmlClass, titles_htmlTag, titles_htmlClass, snippets_htmlTag, snippets_htmlClass,
             links_htmlTag, links_htmlClass, authors_htmlTag, authors_htmlClass, output_path, debug=False):
    urls = pastURLs
    print('Total of Past URLs: ' + str(len(urls)))

    if newspaper_url.startswith('https://') or newspaper_url.startswith('http://'):
        newspaper_url = newspaper_url.replace('https://', '')

    titles = []
    snippets = []
    links = []
    authors = []

    links_no_reps = []
    titles_no_reps = []
    snippets_no_reps = []
    authors_no_reps = []

    x = 1
    print('Getting the News...')
    for i in range(len(urls)):
        page = requests.get(urls[i])
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="UTF-8")
        ListOfTagContents = soup.find_all(news_htmlTag, class_=news_htmlClass)

        for content in ListOfTagContents:
            try:
                titles.append(content.find(titles_htmlTag, class_=titles_htmlClass).get_text())
            except:
                titles.append(' ')

        for content in ListOfTagContents:
            try:
                snippets.append(content.find(snippets_htmlTag, class_=snippets_htmlClass).get_text())
            except:
                snippets.append(' ')

        for content in ListOfTagContents:
            try:
                links.append(content.find(links_htmlTag, links_htmlClass).get("href"))
            except:
                links.append(' ')

        for content in ListOfTagContents:
            try:
                authors.append(content.find(authors_htmlTag, class_=authors_htmlClass).get_text())
            except:
                authors.append(' ')

        for link in links:
            if link not in links_no_reps:
                links_no_reps.append(link)
                titles_no_reps.append(titles[links.index(link)])
                snippets_no_reps.append(snippets[links.index(link)])
                authors_no_reps.append(authors[links.index(link)])

        for i in range(len(links_no_reps)):
            try:
                titles_no_reps[i] = titles_no_reps[i].replace('\n', '')
                titles_no_reps[i] = titles_no_reps[i].replace('\r', '')
                titles_no_reps[i] = titles_no_reps[i].replace('\r\n', '')
                titles_no_reps[i] = titles_no_reps[i].replace('\n\r', '')
                titles_no_reps[i] = titles_no_reps[i].replace('    ', '')
            except:
                pass

            try:
                snippets_no_reps[i] = snippets_no_reps[i].replace('\n', '')
                snippets_no_reps[i] = snippets_no_reps[i].replace('\r', '')
                snippets_no_reps[i] = snippets_no_reps[i].replace('\r\n', '')
                snippets_no_reps[i] = snippets_no_reps[i].replace('\n\r', '')
                snippets_no_reps[i] = snippets_no_reps[i].replace('    ', '')
            except:
                pass

            try:
                links_no_reps[i] = links_no_reps[i].replace('\n', '')
                links_no_reps[i] = links_no_reps[i].replace('\r', '')
                links_no_reps[i] = links_no_reps[i].replace('\r\n', '')
                links_no_reps[i] = links_no_reps[i].replace('\n\r', '')
                links_no_reps[i] = links_no_reps[i].replace('    ', '')
            except:
                pass

            try:
                authors_no_reps[i] = authors_no_reps[i].replace('\n', '')
                authors_no_reps[i] = authors_no_reps[i].replace('\r', '')
                authors_no_reps[i] = authors_no_reps[i].replace('\r\n', '')
                authors_no_reps[i] = authors_no_reps[i].replace('\n\r', '')
                authors_no_reps[i] = authors_no_reps[i].replace('    ', '')
            except:
                pass

        if debug == True:
            print(titles_no_reps)
            print(snippets_no_reps)
            print(links_no_reps)
            print(authors_no_reps)
            print('\n')

        print(f'{x} out of {str(len(urls))}')
        x = x + 1

    news = []

    for i in range(len(links_no_reps)):
        if links_no_reps[i].startswith('/noFrame/replay/'):
            links_no_reps[i] = links_no_reps[i].replace('/noFrame/replay/', 'https://arquivo.pt/wayback/')

    for i in range(len(titles_no_reps)):
        news.append({
            'Title': titles_no_reps[i],
            'Snippet': snippets_no_reps[i],
            'Link': links_no_reps[i],
            'Author': authors_no_reps[i],
        })

    with open(f'{output_path}.json', 'w', encoding='utf-8') as fp:
        json.dump(news, fp, indent=4, ensure_ascii=False)

    print('Total News Found: ' + str(len(titles_no_reps)))