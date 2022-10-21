from publicnewsarchive import dataExtraction

#2022

listOfPastURLs = dataExtraction.getPastURLs(year='2022', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker',
                               snippets_htmlTag='h3', snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link',
                               authors_htmlTag='span', authors_htmlClass='byline__name', output_path='samples\\newsPublico2022', debug=True)

#2021

listOfPastURLs = dataExtraction.getPastURLs(year='2021', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker',
                               snippets_htmlTag='h3', snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link',
                               authors_htmlTag='span', authors_htmlClass='byline__name', output_path='samples\\newsPublico2021', debug=True)

#2020

listOfPastURLs = dataExtraction.getPastURLs(year='2020', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker',
                               snippets_htmlTag='h3', snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link',
                               authors_htmlTag='span', authors_htmlClass='byline__name', output_path='samples\\newsPublico2020', debug=True)

#2019

listOfPastURLs = dataExtraction.getPastURLs(year='2019', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker',
                               snippets_htmlTag='h3', snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link',
                               authors_htmlTag='span', authors_htmlClass='byline__name', output_path='samples\\newsPublico2019', debug=True)

#2018

listOfPastURLs = dataExtraction.getPastURLs(year='2018', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker',
                               snippets_htmlTag='h3', snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link',
                               authors_htmlTag='span', authors_htmlClass='byline__name', output_path='samples\\newsPublico2018', debug=True)

#2017

listOfPastURLs = dataExtraction.getPastURLs(year='2017', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='article', news_htmlClass='hentry', titles_htmlTag='h2', titles_htmlClass='entry-title',
                               snippets_htmlTag='p', snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='span', authors_htmlClass='fn', output_path='samples\\newsPublico2017', debug=True)

#2016

listOfPastURLs = dataExtraction.getPastURLs(year='2016', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='article', news_htmlClass='hentry', titles_htmlTag='h2', titles_htmlClass='entry-title',
                               snippets_htmlTag='p', snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='span', authors_htmlClass='fn', output_path='samples\\newsPublico2016', debug=True)

#2015

listOfPastURLs = dataExtraction.getPastURLs(year='2015', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='article', news_htmlClass='hentry', titles_htmlTag='h2', titles_htmlClass='entry-title',
                               snippets_htmlTag='p', snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='span', authors_htmlClass='fn', output_path='samples\\newsPublico2015', debug=True)

#2014

listOfPastURLs = dataExtraction.getPastURLs(year='2014', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='article', news_htmlClass='hentry', titles_htmlTag='h2', titles_htmlClass='entry-title',
                               snippets_htmlTag='p', snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='span', authors_htmlClass='fn', output_path='samples\\newsPublico2014', debug=True)

#2013

listOfPastURLs = dataExtraction.getPastURLs(year='2013', newspaper_url='https://publico.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='article', news_htmlClass='hentry', titles_htmlTag='h2', titles_htmlClass='entry-title',
                               snippets_htmlTag='p', snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                               authors_htmlTag='span', authors_htmlClass='fn', output_path='samples\\newsPublico2013', debug=True)

#2012

listOfPastURLs = dataExtraction.getPastURLs(year='2012', newspaper_url='https://publico.pt/')

#2011

listOfPastURLs = dataExtraction.getPastURLs(year='2011', newspaper_url='https://publico.pt/')

#2010

listOfPastURLs = dataExtraction.getPastURLs(year='2010', newspaper_url='https://publico.pt/')



