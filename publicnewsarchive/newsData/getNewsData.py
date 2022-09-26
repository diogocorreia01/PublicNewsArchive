import spacy
import json
from date_guesser_rc import guess_date
from yake import KeywordExtractor as YakeKW


def getNewsData(json_news, output_path):
    print('Opening Your Json File...')
    jsonFile = open(json_news, encoding="utf8")
    data = json.load(jsonFile)

    titles = []
    snippets = []
    links = []
    authors = []
    for i in data:
        titles.append(i['Title'])
        snippets.append(i['Snippet'])
        links.append(i['Link'])
        authors.append(i['Author'])

    # Extração das Localidades, Organizações e Pessoas
    locations = []
    organizations = []
    people = []
    for _ in range(len(titles)):
        locations.append(' ')
        organizations.append(' ')
        people.append(' ')

    print('Done')

    print('Getting the Locations, Organizations and People...')
    model = 'pt_core_news_lg'
    nlp = spacy.load(model, disable=['tagger', 'parser'])

    x = 0
    for i in data:
        doc = nlp(i['Snippet'])
        for ent in doc.ents:
            if ent.label_ == 'LOC':
                if locations[x] == ' ':
                    locations[x] = ent.text
                else:
                    locations[x] = locations[x] + ', ' + ent.text
        for ent in doc.ents:
            if ent.label_ == 'ORG':
                if organizations[x] == ' ':
                    organizations[x] = ent.text
                else:
                    organizations[x] = organizations[x] + ', ' + ent.text
        for ent in doc.ents:
            if ent.label_ == 'PER':
                if people[x] == ' ':
                    people[x] = ent.text
                else:
                    people[x] = people[x] + ', ' + ent.text
        x = x + 1
    print('Done')

    # Dates Extraction
    dates = []
    print('Getting the dates...')
    for i in links:
        guess = guess_date(url=i)
        date_new = guess.date
        date_new = str(date_new)[:10]
        dates.append(date_new)
    print('Done')

    print('Getting the Keywords...')
    # Keywords Extraction
    keywords = []
    for i in data:
        sample = YakeKW(lan="pt")
        text = i['Snippet']
        keywords.append(sample.extract_keywords(text))
    print('Done')

    '''#Images Extraction (Fixing Bugs)
    images_links = []
    for i in range(len(titles)):
        word_search = locations[i]
        try:
            req = Request(f"https://arquivo.pt/imagesearch?q={word_search}&offset=50&maxItems=1&prettyPrint=true")
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "html.parser")
            html_text = soup.text

            for line in html_text.splitlines():
                if '      "imgLinkToArchive": ' in line:
                    images_links.append(line)
                elif '"imgLinkToArchive": ' in line:
                    images_links.append(line)

            for i in range(len(images_links)):
                if images_links[i] == '      "imgLinkToArchive": ':
                    images_links[i] = images_links[i].replace('      "imgLinkToArchive": ', '')
                elif images_links[i] == '"imgLinkToArchive": ':
                    images_links[i] = images_links[i].replace('"imgLinkToArchive": ', '')

        except:
            images_links.append(' ')

    print(images_links)'''

    print('Creating the Json File...')
    # Dictionary with all Data from the News
    news = []
    for i in range(len(titles)):
        news.append({
            'Title': titles[i],
            'Snippet': snippets[i],
            'Link': links[i],
            'Author': authors[i],
            'Date': dates[i],
            'Locations': locations[i],
            'Organizations': organizations[i],
            'People': people[i],
            'Keywords': keywords[i]
            # 'Image': images_links[i]
        })

    # Output Json File
    with open(f'{output_path}.json', 'w', encoding='utf-8') as fp:
        json.dump(news, fp, indent=4, ensure_ascii=False)
    print('Your Json File is Ready!')








