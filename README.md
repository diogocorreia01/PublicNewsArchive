# ``PublicNewsArchive 0.1``

This module allows you to get and analyze news from <a href="https://arquivo.pt/" target="_blank">Arquivo.pt</a>

* Newspapers that were tested during the package development:
    * <a href="https://www.publico.pt/" target="_blank">Público</a>
    * <a href="https://omirante.pt/" target="_blank">O Mirante</a>
    * <a href="https://www.jn.pt/" target="_blank">Jornal de Notícias</a>
    * <a href="https://www.dn.pt/" target="_blank">Diário de Notícias</a>
    * <a href="https://www.cmjornal.pt/" target="_blank">Correio da Manhã</a>


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

## **Get Past URLs**

To get URLs from the past, we need to use the ‘getPastURLs’ method, which will extract the past URLs of the newspapers through the Arquivo.pt API.

*Function options:*

`years` - here you should indicate the year from which you want to collect past news articles.

`output_path` - here you must indicate the path where the json file with the past URLs will be saved.

`newspaper_url` - here you must specify the URL of the media outlet from which you want to collect past preserved URLs.

`startMonth` (optional) - here you can indicate the start month from wich you want to collect past news articles. (Default value is 1 (January))

`endMonth` (optional) - here you can indicate the end month from wich you want to collect past news articles. (Default value is 12 (December))

```python
from publicnewsarchive import newsData

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://publico.pt/', startMonth='06', endMonth='07')

print(listOfPastURLs)
```

## **Get Past News Articles**

Now that we have the Past URLs of the newspaper, we are able to extract the news articles that are on them. By using the `getNewsArticles()` method it's possible to do Webscraping in an easy way, that allow us to easily get the news articles.

*Function options:*

`input_file` - Here is placed the json file previously created by extracting the Past URLs.

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

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://publico.pt/', startMonth='06', endMonth='07')

newsData.getNewsArticles(pastURLs=listOfPastURLs, newspaper_url='https://publico.pt/', news_htmlTag='div',
                 news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker', snippets_htmlTag='h3',
                 snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link', authors_htmlTag='span',
                 authors_htmlClass='byline__name', output_path='samples\\newsPublico2022', debug=True)
```

### **Contribute to the package with your Webscraping**

You can access the 'Scraping' folder in this package, where you will Webscraping made for some Newspapers.

You can also contribute with your own Webscraping, by adding it to that 'Scraping' folder.

## **Get News Data**

After extracting every possible news article from the Past URLs, we can now use the `getNewsData()` method to extract the dates, locations, organizations, people and keywords in each one of the news articles. At the moment it only works in Portuguese language texts but we are working on to make it possible to use this function in several languages.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news articles.

`lang` - here you must choose the language in which the news text is. (only `pt` available)

`output_path` - here you must indicate the path where the json file with the news data will be saved.

```python
from publicnewsarchive import newsData

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://publico.pt/', startMonth='06', endMonth='07')

newsData.getNewsArticles(pastURLs=listOfPastURLs, newspaper_url='https://publico.pt/', news_htmlTag='div',
                 news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker', snippets_htmlTag='h3',
                 snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link', authors_htmlTag='span',
                 authors_htmlClass='byline__name', output_path='samples\\newsPublico2022', debug=True)

newsData.getNewsData(json_news='samples\\newsPublico2022.json', output_path='samples\\newsPublicoData2022')
```

## **Get Insights from News Articles**

With all the news data extracted, we now have the possibility to easily analyze it, by using the `newsAnalysis` module of the package.

### **News Data per Year**

Using the `dataPerYear()` method we can easily find out which locations, organizations and people were most talked about in the news articles that are in the json file.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news data.

`output_path` - here you must indicate the path where the json file with the news data per year will be saved.

```python
from publicnewsarchive import newsAnalysis

newsAnalysis.dataPerYear(json_news='samples\\newsPublicoData2022.json', output_path='samples\\newsDataPerYearPublico2022')
```

### **Wordcloud**

Using the `newsWordcloud()` method we can easily create a Wordcloud with the most important keywords found on the news articles.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news data.

`output_path` - here you must indicate the path where the png file with the Wordcloud will be saved.

```python
from publicnewsarchive import newsAnalysis

newsAnalysis.newsWordcloud(json_news='samples\\newsPublicoData2022.json', output_path='samples\\wordcloudPublico2022')
```

### **Create an interactive map with the locations**

Using the `newsMap()` method we can easily create an interactive map with all the locations mentioned on the news articles.

*Function options:*

`json_news` - Here is placed the json file previously created by extracting the news data.

`output_path` - here you must indicate the path where the html file with the interactive map will be saved.

`api_key` - here you must indicate the api key from Google Maps.

```python
from publicnewsarchive import newsAnalysis

newsAnalysis.newsMap(json_news='samples\\newsPublicoData2022.json', output_path='samples\\mapPublico2022', api_key='AIzaSyDoygTYvzCb_NTl51WNoWI57y5TZ6e15u4')
```

## **Related projects**

``Arquivo Publico`` - <a href="https://arquivopublico.ipt.pt/" target="_blank">Arquivo Publico</a> is the first usage of this module, the module was used to get the last 10 years News from Publico newspaper and analise them.