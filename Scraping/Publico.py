from publicnewsarchive import newsData

#2022

listOfPastURLs = newsData.getPastURLs(year='2022', newspaper_url='https://publico.pt/')

newsData.getNewsArticles(pastURLs=listOfPastURLs, news_htmlTag='div', news_htmlClass='card__inner', titles_htmlTag='h4', titles_htmlClass='kicker',
                         snippets_htmlTag='h3',snippets_htmlClass='card__title headline', links_htmlTag='a', links_htmlClass='card__faux-block-link',
                         authors_htmlTag='span', authors_htmlClass='byline__name', output_path='samples\\newsPublico2022', debug=True)

