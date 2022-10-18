from publicnewsarchive import newsData

#2022

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2022', debug=True)

#2021

listOfPastURLs = newsData.getPastURLs(year='2021', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2021', debug=True)

#2020

listOfPastURLs = newsData.getPastURLs(year='2020', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2020', debug=True)

#2019

listOfPastURLs = newsData.getPastURLs(year='2019', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2019', debug=True)

#2018

listOfPastURLs = newsData.getPastURLs(year='2018', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2028', debug=True)

#2017

listOfPastURLs = newsData.getPastURLs(year='2017', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2017', debug=True)

#2016

listOfPastURLs = newsData.getPastURLs(year='2016', newspaper_url='https://www.jn.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='', titles_htmlTag='h3', titles_htmlClass='',
                         snippets_htmlTag='h2',snippets_htmlClass='', links_htmlTag='a', links_htmlClass='',
                         authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2016', debug=True)