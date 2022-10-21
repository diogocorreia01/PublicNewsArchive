import spacy
import json
from date_guesser_rc import guess_date
from yake import KeywordExtractor as YakeKW
import requests
import os
from requests.exceptions import Timeout
def getNewsData(input_filename, output_filename):

    path = "data/"
    jsonFile = open(path + input_filename, encoding="utf8")
    data = json.load(jsonFile)

    model = 'pt_core_news_lg'
    nlp = spacy.load(model, disable=['tagger', 'parser'])

    sample = YakeKW(lan="pt")

    for newsarticle in data:

        # Get date of publication
        guess = guess_date(newsarticle['Link'])
        date = str(guess.date)[:10]
        newsarticle['Date'] = date

        # Get Keywords
        text = newsarticle['Title'] + ". " + newsarticle['Snippet']
        keywords = sample.extract_keywords(text)
        newsarticle['Keywords'] = keywords

        # Get Locations, Organizations and People
        doc = nlp(newsarticle['Title'] + " " + newsarticle['Snippet'])
        Locations = []
        Organizations = []
        People = []

        for ent in doc.ents:
            if ent.label_ == 'LOC':
                Locations.append(ent.text)
            elif ent.label_ == 'ORG':
                Organizations.append(ent.text)
            elif ent.label_ == 'PER':
                People.append(ent.text)

        newsarticle['Locations'] = Locations
        newsarticle['Organizations'] = Organizations
        newsarticle['People'] = People

        # Get Image
        searchItem = ""
        if len(Organizations) > 0:
            searchItem = Organizations[0]
        elif len(People) > 0:
            searchItem = People[0]
        elif len(Locations) > 0:
            searchItem = Locations[0]
        elif len(keywords) > 0:
            searchItem = keywords[0][0]

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0 "}
        url_api = 'https://arquivo.pt/imagesearch'

        if len(date) > 0:
            fromDate = f'{date[:4]}0101000000'
            toDate = f'{date[:4]}1231235959'
            payload = {'q': searchItem, 'from': fromDate, 'to': toDate}
        else:
            payload = {'q': searchItem}
        try:
            r = requests.get(url_api, params=payload, headers=headers, timeout=60)
        except Timeout:
            print('Timeout has been raised.')

        content = r.json()

        try:
            img = content['responseItems'][0]['imgLinkToArchive']
            newsarticle['Image'] = img
        except:
            newsarticle['Image'] = ''

    # Output Json File
    if not os.path.exists(path):
        os.makedirs(path)

    with open(f'{path + output_filename}', 'w', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)








