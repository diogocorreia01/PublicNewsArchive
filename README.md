# ``Arquivo Público (Public News Archive)``

`Public News Archive` allows users to get and analyze a large scale of past news articles from the <a href="https://arquivo.pt/" target="_blank">Arquivo.pt</a>, the Portuguese web archiving infra-structure.

Try Public News Archive on Google Colab:

[<img src="https://i.imgur.com/6xSa3Zu.png" alt="MarineGEO circle logo" width="150px"/>](https://drive.google.com/file/d/1vTxP3_ZNCQd38VXOF0BIiK5muWiCI6ou/edit)

## Main Features

- Get past preserved URLs from specific media outlets;
- Get past news articles from specific media outlets;
- Get detailed information from each and for all the collected news articles, in particular their Title, Snippet, Link, Author, Date, referred Locations, Organizations, People and important Keywords.
- News Article Analysis: Compute top-frequency locations, organizations and people, plot word cloud and create interactive map with the locations.

## Supported Media Outlets

We have developed a generic method that works for a diverse set of newspapers, requiring users to only indicate the tags and the HTML classes of the base data (title, snippet, link and author). As for now, our package supports getting information from the following media outlets:

- [Público](https://www.publico.pt/)
- [Jornal de Notícias](https://www.jn.pt/)
- [Diário de Notícias](https://www.dn.pt/)
- [Correio da Manhã](https://www.cmjornal.pt/)
- [O Mirante](https://omirante.pt/)

Scripts required to extract information from this media outlets can be found in the `scraping` folder. Users of the package are also challenged to test and to contribute with scripts that allow getting information from other local or national newspapers. Those scripts will be added to the `scraping` folder upon Pull Request.

## Installation
`Public News Archive` is available through GitHub.
```bash
pip install git+https://github.com/diogocorreia01/PublicNewsArchive
```

## Usage (Python)

To start with, begin by importing `publicnewsarchive` as follows:

```python
from publicnewsarchive import dataExtraction
```

## <u>Data Extraction</u>

### Get Past Preserved URLs

To get URLs from the past, users of the package should resort to the `getPastURLs` method, which will build upon the Arquivo.pt [URL Search API](https://github.com/arquivo/pwa-technologies/wiki/Arquivo.pt-API) to extract past preserved URLs of a given newspaper. The following, exemplifies this process for the [Jornal Público](https://publico.pt/). Beyond the `newspaper_url`, users will also need to provide information concerning the `year` from which to get past URLs, the `startMonth` (default value is 1 - January) and the `endMonth` (default value is 12 - December) parameters.

```python
pastURLs = dataExtraction.getPastURLs(year='2021', newspaper_url='https://publico.pt/', startMonth='06', endMonth='07')

print(len(pastURLs))
```

### Get Past News Articles

Now that we have the list of `Past URLs` for the specified newspaper, we are able to extract the news articles that can be found in each of the referred URLs. For this purpose, we have developed a generic method, `getNewsArticles()`, which allows users of the package to perform this web scraping process in an easy way, requiring them to only provide some sort of HTML tag information that is necessary to get the news articles features, that is the title, snippets, links and authors. Such information can be easily obtained by inspecting the corresponding newspaper webpage. 

A list of the required parameters is given below with the corresponding description:

- `pastURLs`: a list with the past preserved urls collected from the Arquivo.pt infrastructure
- `news_htmlTag`: main news HTML tag
- `news_htmlClass`: main news HTML class
- `titles_htmlTag`: HTML Title tag
- `titles_htmlClass`: HTML Title class
- `snippets_htmlTag`: HTML Snippet tag
- `snippets_htmlClass`: HTML Snippet class
- `links_htmlTag`: HTML Link tag
- `links_htmlClass`: HTML Link class
- `authors_htmlTag`: HTML Author tag
- `authors_htmlClass`: HTML Author class
- `filename`: json filename where the information collected will be saved. Be aware that files are saved under a data folder.
- `debug (optional)`: in case you want to follow up the webscraping progress. Default value is `False`.

The following image illustrates the inspection process for the snippet feature. As can been seen from the figure, the snippets tag is a `snippets_htmlTag='h3'`, while the html class is a `snippets_htmlClass='card__title headline'` (highlighted with blue color in the inspection panel).

<img src="http://www.ccc.ipt.pt/~ricardo/images/PublicNewsArchive_1.jpg" alt="MarineGEO circle logo"/>

The following code exemplifies the `Get Past News Articles` process for the `Jornal Público` interface in the year 2021. For illustrative purposes, we are only passing the first URL collected in pastURLs parameter (`pastURLs[:1]`). Passing the full list will consume a considerable amount of time. Also note that the obtained news articles will be saved in the following filename `newsPublico2021.json` within the `data` folder (which will be automatically created by the program in the user's computer).

```python
dataExtraction.getNewsArticles(pastURLs=pastURLs[:1], news_htmlTag='div',
                 news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker', snippets_htmlTag='h3',
                 snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link', authors_htmlTag='span',
                 authors_htmlClass='byline__name', filename='newsPublico2021.json', debug=True)
```

### Information Extraction

After extracting all the news articles from past preserved URLs, we can now use the `getNewsData()` method to extract further info from them. At the moment, we are collecting the date of publication of the news article, together with the most important [YAKE!](http://yake.inesctec.pt) keywords of every text and spacy named entities, such as locations, organizations, people and an image link of the most representative element of the text (image links are obtained from the Arquivo.pt [Image Search API](https://github.com/arquivo/pwa-technologies/wiki/ImageSearch-API-v1.1-(beta))). The following code illustrates this process. As can be observed, users are required to specify the input filename, where the colleted news articles were saved before (`newsPublico2021.json`), and the output, where the new information will be saved.

```python
dataExtraction.getNewsData(input_filename='newsPublico2021.json', output_filename='newsPublico2021_v1.json')
```

## <u>Data Acquisition</u>

### News Article Analysis

With all the information extracted, we now have the chance to perform some data analysis. Please start by importing the following module:

```python
from publicnewsarchive import dataAnalysis
```

#### Compute top-locations, organizations and people

Using the `computeTopNERs()` method, we can easily find out which locations, organizations and people were most talked about in the news articles. The following code illustrates this process. The `input_filename` is the name of the file (that can be found in the `data` folder) with all the information obtained from the news articles. `output_filename` is the basename of the file that is going to be used as a basis for creating three files in the `data` folder: `output_filename_Locations.json`; `output_filename_Organizations.json`; `output_filename_People.json`. Each of these files will contain the occurrences of locations, organizations and people.

```python
dataAnalysis.computeTopNERs(input_filename = 'newsPublico2021_v1.json', output_filename = 'newsPublico2021')
```

```python
import json
from collections import Counter

def computeTopNERs(input_filename, output_filename):
    path = "data/"
    
    jsonFile = open(path + input_filename, encoding="utf8")
    data = json.load(jsonFile)
    
    
    Locations = []
    Organizations = []
    People = []
    
    for newsarticle in data:
        for location in newsarticle['Locations']:
            Locations.append(location.lower())
        
        for organization in newsarticle['Organizations']:
            Organizations.append(organization.lower())
        
        for people in newsarticle['People']:
            People.append(people.lower())
    
    #Count
    counter_locations = Counter(Locations)
    counter_locations_sorted = sorted(counter_locations.items(), key=lambda pair: pair[1], reverse=True)
    
    counter_organizations = Counter(Organizations)
    counter_organizations_sorted = sorted(counter_organizations.items(), key=lambda pair: pair[1], reverse=True)
    
    counter_people = Counter(People)
    counter_people_sorted = sorted(counter_people.items(), key=lambda pair: pair[1], reverse=True)
        
    # Output Locations Json File
    with open(f'{path + output_filename}_Locations.json', 'w', encoding='utf8') as fp:
        json.dump(counter_locations_sorted, fp, ensure_ascii=False)
    
    with open(f'{path + output_filename}_Organizations.json', 'w', encoding='utf8') as fp:
        json.dump(counter_organizations_sorted, fp, indent=4, ensure_ascii=False)
    
    with open(f'{path + output_filename}_People.json', 'w', encoding='utf8') as fp:
        json.dump(counter_people_sorted, fp, indent=4, ensure_ascii=False)
    
computeTopNERs(input_filename = 'newsPublico2021_v1.json', output_filename = 'newsPublico2021')
```

#### Word Cloud

Using the `newsWordcloud()` method, we can easily create a Wordcloud with the most important keywords found in the news articles. The `input_filename` is the name of the file (that can be found in the `data` folder) with all the information obtained from the news articles. `output_filename` is the name of the file where the wordcloud will be saved.

```python
dataAnalysis.newsWordcloud(input_filename='newsPublico2021_v1.json', output_filename='newsPublico2021_wordcloud.png')
```

#### Interactive Map

Using the `newsMap()` method, we can easily create an interactive map with all the locations mentioned on the news articles. The `input_filename` is the name of the file (that can be found in the `data` folder) with all the information obtained from the news articles. `output_filename` is the name of the html file that will keep the Google Map with all the locations. Please be aware that such feature requires having access to an api_key. More information about it here: https://pypi.org/project/gmplot/

The following code exemplifies how to create a map for the locations found in the 2021 news articles. Don't forget to specify your api_key.

```python
api_key = "SPECIFY KEY"
dataAnalysis.newsMap(input_filename='newsPublico2021_v1.json', output_filename='mapPublico2021.html', api_key= api_key)
```

## Awards

Third Place of the [Arquivo.pt Award 2022](https://sobre.arquivo.pt/en/meet-the-winners-of-the-arquivo-pt-award-2022/).

[Arquivo.pt Award 2022 Presentation](https://www.youtube.com/watch?v=8f4HBTsjLsE)

## References

Please cite the following works when using Public News Archive:

## Media

- [PÚBLICO ao longo do tempo](https://www.publico.pt/2022/07/22/ciencia/noticia/arquivo-parlamento-repositorio-quer-dar-visibilidade-narrativas-vida-politica-portuguesa-2013730)
- [FCCN](https://www.fccn.pt/noticias/premio-arquivopt-2022-vencedores/)