from publicnewsarchive import dataExtraction

#2022

listOfPastURLs = dataExtraction.getPastURLs(year='2022', newspaper_url='https://www.cmjornal.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='text_container', titles_htmlTag='a', titles_htmlClass='eventAnalytics',
                               snippets_htmlTag='p', snippets_htmlClass='destaques_lead', links_htmlTag='a', links_htmlClass='eventAnalytics',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2022', debug=True)

#2021

listOfPastURLs = dataExtraction.getPastURLs(year='2021', newspaper_url='https://www.cmjornal.pt/')

dataExtraction.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='text_container', titles_htmlTag='a', titles_htmlClass='eventAnalytics',
                               snippets_htmlTag='p', snippets_htmlClass='destaques_lead', links_htmlTag='a', links_htmlClass='eventAnalytics',
                               authors_htmlTag='', authors_htmlClass='', output_path='samples\\newsJornalNoticias2021', debug=True)