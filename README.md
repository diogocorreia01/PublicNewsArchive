# ``PublicNewsArchive 0.1``

This module allows you to get and analyze news from <a href="https://arquivo.pt/" target="_blank">Arquivo.pt</a>

## **Main Features**

* Get Past Covers from Newspapers
* Get Past News from Newspapers
* Get Deep Data from the News (Title, Snippet, Link, Author, Date, Locations, Organizations, People and Keywords)
* News Analysis

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

## **Getting Font Pages**

To extract the covers of the news, we need to use the 'getCovers' function, which will extract the covers of the newspapers through the Arquivo.pt API.

*Function options:*

`years` - here you can indicate the year that you want to recover the covers.

`output_path` - here you must indicate the path where the json file with the covers will be saved.

`newspaper_url` - here you must indicate the link of the newspaper that you want to retrieve the covers.

```python
from publicnewsarchive import newsData

listOfFontPages = newsData.getFontPages(year='2022' , newspaper_url='https://www.publico.pt')

print(listOfFontPages)
```