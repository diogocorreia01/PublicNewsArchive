# ``PublicNewsArchive 0.1``

This module allows you to get and analyze news from <a href="https://arquivo.pt/" target="_blank">Arquivo.pt</a>

## **Main Features**

* Get Past URLs from specific media outlets
* Get Past News Articles from media outlets
* Get Detailed Information from each of the collected News Articles (Title, Snippet, Link, Author, Date, Locations, Organizations, People and Keywords)
* Get Insights from News Articles

## **Installation**
ArchiveNews is available through GitHub.
```bash
pip install git+https://github.com/diogocorreia01/PublicNewsArchive.git
```

## **Usage (Python)**

Now you just need to import the package

```python
import publicnewsarchive
```
or

```python
from publicnewsarchive import newsData
from publicnewsarchive import newsAnalysis
```

## **Get Past URL**

To get URLs from the past, we need to use the ‘getPastURLs’ method, which will extract the past URLs of the newspapers through the Arquivo.pt API.

*Function options:*

`years` - here you should indicate the year from which you want to collect past news articles.

`output_path` - here you must indicate the path where the json file with the past URLs will be saved.

`newspaper_url` - here you must specify the URL of the media outlet from which you want to collect past preserved URLs.

`startMonth` (optional) - here you can indicate the start month from wich you want to collect past news articles. (Default value is 1 (January))

`endMonth` (optional) - here you can indicate the end month from wich you want to collect past news articles. (Default value is 12 (December))

```python
from publicnewsarchive import newsData

listOfPastURLs = newsData.getPastURLs(year='2022' , newspaper_url='https://www.publico.pt')

print(listOfPastURLs)
```

## **Get News Articles**

Now that we have the covers of the newspaper, it is possible to extract the news that are on them. There are 2 ways to do this, the first one is to use the `getNewsArticles()` method present in the package, this function works correctly for most newspapers but in some cases it may not present good results, the another option is to do the web scraping manually.

*Function options:*

`input_file` - Here is placed the json file previously created by extracting the covers.

`newspaper_url` - here you must specify the URL of the media outlet from which you want to collect past preserved URLs.

`news_htmlTag` - HTML Tag for web scraping.

`news_htmlClass` - HTML Class for web scraping.

`titles_htmlTag` - HTML Tittle Tag for web scraping.

`titles_htmlClass` - HTML Tittle Class for web scraping.

`snippets_htmlTag` - HTML Snippet Tag for web scraping.

`snippets_htmlClass` - HTML Snippet Class for web scraping.

`links_htmlTag` - HTML Link Tag for web scraping.

`links_htmlClass` - HTML Link Class for web scraping.

`authors_htmlTag` - HTML Author Tag for web scraping.

`authors_htmlClass` - HTML Author Class for web scraping.

`output_path` - here you must indicate the path where the json file with the past URLs will be saved.

`debug` (optional) - Here you can indicate if you want to see the outputs of your webscraping or not. (Default value is False)

```python
# Using the function

from publicnewsarchive import newsData 

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://publico.pt/') 

newsData.getNewsArticles(fontPages=listOfPastURLs, newspaper_url='https://publico.pt/', news_htmlTag='div',
                 news_htmlClass='entry-text-content', titles_htmlTag='h2', titles_htmlClass='entry-title', snippets_htmlTag='p',
                 snippets_htmlClass='', links_htmlTag='a', links_htmlClass='', authors_htmlTag='',
                 authors_htmlClass='', output_path='samples\\newsPublico2022', debug=True)
```
or
```python
# Manual Web Scrapping

import requests
from bs4 import BeautifulSoup
import json

# Load the Json file with the Past URLs
jsonFile = open(f'Samples\\CoverSample.json', 'r')
urls = json.load(jsonFile)

# Lists for the values
titles = []
snippets = []
links = []
authors = []

# List for the values (with no repeated news)
links_no_reps = []
titles_no_reps = []
snippets_no_reps = []
authors_no_reps = []

for i in range(len(urls)): 
    page = requests.get(urls[i])
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding="UTF-8")
    ListOfTagContents = soup.find_all('news_htmlTag', class_='news_htmlClass')

    for content in ListOfTagContents:
        try:
            titles.append(content.find('titles_htmlTag', class_='titles_htmlClass').get_text())
        except:
            titles.append(' ')

    for content in ListOfTagContents:
        try:
            snippets.append(content.find('snippets_htmlTag', class_='snippets_htmlClass').get_text())
        except:
            snippets.append(' ')

    for content in ListOfTagContents:
        try:
            links.append(content.find('links_htmlTag', 'links_htmlClass').get("href"))
        except:
            links.append(' ')

    for content in ListOfTagContents:
        try:
            authors.append(content.find('authors_htmlTag', class_='authors_htmlClass').get_text())
        except:
            authors.append(' ')

    # For Loop to remove all of the repetead news 
    for link in links:
        if link not in links_no_reps:
            links_no_reps.append(link)
            titles_no_reps.append(titles[links.index(link)])
            snippets_no_reps.append(snippets[links.index(link)])
            authors_no_reps.append(authors[links.index(link)])

    # Remove some of the spaces that can be found on the Titles, Snippets, Links and Authors
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
    
    # Create Json File 
    news = []
    for i in range(len(titles_no_reps)):
        news.append({
            'Title': titles_no_reps[i],
            'Snippet': snippets_no_reps[i],
            'Link': links_no_reps[i],
            'Author': authors_no_reps[i],
        })

    with open(f'Output File', 'w') as fp:
        json.dump(news, fp, indent=4)

    print('Total News Found: ' + str(len(titles_no_reps)))
```

## **Get News Data**

After extracting all possible news, we can use the `getNewsData()` method to extract the dates, locations, organizations, people and keywords in each one of the news. At the moment it only works in Portuguese language texts but we are working on to make it possible to use this function in several languages.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news.

`lang` - here you must choose the language in which the news text is. (only `pt` available)

`output_path` - here you must indicate the path where the json file with the news data will be saved.

```python
from publicnewsarchive import newsData

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://publico.pt/') 

newsData.getNewsArticles(fontPages=listOfPastURLs, newspaper_url='https://publico.pt/', news_htmlTag='div',
                 news_htmlClass='entry-text-content', titles_htmlTag='h2', titles_htmlClass='entry-title', snippets_htmlTag='p',
                 snippets_htmlClass='', links_htmlTag='a', links_htmlClass='', authors_htmlTag='',
                 authors_htmlClass='', output_path='samples\\newsPublico2022', debug=True)

newsData.getNewsData(json_news='samples\\newsPublico2022.json', output_path='samples\\newsPublicoData2022')
```

## **Get Insights from News Articles**

With all of the news data extracted, we now have the possibility to easily analyze this data using the `newsAnalysis` module of the package.

### **News Data per Year**

Using the `dataPerYear()` method we can easily find out which places, organizations and people were most talked about in the news during that year.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news data.

`output_path` - here you must indicate the path where the json file with the news data per year will be saved.

```python
from publicnewsarchive import newsAnalysis

newsAnalysis.dataPerYear(json_news='samples\\newsPublicoData2022.json', output_path='samples\\newsDataPerYearPublico2022')
```

### **Wordcloud**

Using the `newsWordcloud()` method we can easily create a Wordcloud with the most important keywords found on the news.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news data.

`output_path` - here you must indicate the path where the png file with the Wordcloud will be saved.

```python
from publicnewsarchive import newsAnalysis

newsAnalysis.newsWordcloud(json_news='samples\\newsPublicoData2022.json', output_path='samples\\newsWordcloudPublico2022')
```

### **Create an interactive map with the locations**

Using the `newsMap()` method we can easily create an interactive map with all the locations mentioned on the news.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news data.

`output_path` - here you must indicate the path where the html file with the interactive map will be saved.

`api_key` - here you must indicate the api key from Google Maps.

```python
from publicnewsarchive import newsAnalysis

newsAnalysis.newsMap(json_news='samples\\newsPublicoData2022.json', output_path='samples\\newsWordcloudPublico2022', api_key='GOOGLE_MAPS_API_KEY_HERE')
```

## **Related projects**

``Arquivo Publico`` - <a href="https://arquivopublico.ipt.pt/" target="_blank">Arquivo Publico</a> is the first usage of this module, the module was used to get the last 10 years News from Publico newspaper and analise them.