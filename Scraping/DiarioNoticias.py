from publicnewsarchive import dataExtraction

#2022

listOfPastURLs = dataExtraction.getPastURLs(year='2022', newspaper_url='https://www.dn.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='t-am-head', titles_htmlTag='h3', titles_htmlClass='t-am-categ',
                               snippets_htmlTag='h2', snippets_htmlClass='t-am-title', links_htmlTag='a', links_htmlClass='t-am-text',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2022', debug=True)

#2021

listOfPastURLs = dataExtraction.getPastURLs(year='2021', newspaper_url='https://www.dn.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='t-am-head', titles_htmlTag='h3', titles_htmlClass='t-am-categ',
                               snippets_htmlTag='h2', snippets_htmlClass='t-am-title', links_htmlTag='a', links_htmlClass='t-am-text',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2021', debug=True)

#2020

listOfPastURLs = dataExtraction.getPastURLs(year='2020', newspaper_url='https://www.dn.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='header', news_htmlClass='t-am-head', titles_htmlTag='h3', titles_htmlClass='t-am-categ',
                               snippets_htmlTag='h2', snippets_htmlClass='t-am-title', links_htmlTag='a', links_htmlClass='t-am-text',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2020', debug=True)