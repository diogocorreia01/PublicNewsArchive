from publicnewsarchive import dataExtraction

#2022

listOfPastURLs = dataExtraction.getPastURLs(year='2022', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='article', news_htmlClass='posts-entry', titles_htmlTag='h2', titles_htmlClass='entry-title',
                               snippets_htmlTag='div', snippets_htmlClass='lead', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='span', authors_htmlClass='author vcard', output_path='samples\\newsOMirante2022', debug=True)

#2021

listOfPastURLs = dataExtraction.getPastURLs(year='2021', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='news', titles_htmlTag='h1', titles_htmlClass='',
                               snippets_htmlTag='div', snippets_htmlClass='body', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsOMirante2021', debug=True)

#2020

listOfPastURLs = dataExtraction.getPastURLs(year='2020', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='news', titles_htmlTag='h1', titles_htmlClass='',
                               snippets_htmlTag='div', snippets_htmlClass='body', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsOMirante2020', debug=True)

#2019

listOfPastURLs = dataExtraction.getPastURLs(year='2019', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='news', titles_htmlTag='h1', titles_htmlClass='',
                               snippets_htmlTag='div', snippets_htmlClass='body', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsOMirante2019', debug=True)

#2018

listOfPastURLs = dataExtraction.getPastURLs(year='2018', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='news', titles_htmlTag='h1', titles_htmlClass='',
                               snippets_htmlTag='div', snippets_htmlClass='body', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsOMirante2018', debug=True)

#2017

listOfPastURLs = dataExtraction.getPastURLs(year='2017', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='news', titles_htmlTag='h1', titles_htmlClass='',
                               snippets_htmlTag='div', snippets_htmlClass='body', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsOMirante2017', debug=True)

#2016

listOfPastURLs = dataExtraction.getPastURLs(year='2016', newspaper_url='https://omirante.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='news', titles_htmlTag='div', titles_htmlClass='title',
                               snippets_htmlTag='div', snippets_htmlClass='body', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsOMirante2016', debug=True)


