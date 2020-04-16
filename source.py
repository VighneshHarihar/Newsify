from newsapi import NewsApiClient


def supreme(s, test):
    newsapi = NewsApiClient(api_key='bb0f664df41346a38b42d10e3682c915')
    universe = []
    newsl = []
    urls = []
    title=[]

    for i in s.split():
        all_news = newsapi.get_everything(q=i)
        temp = all_news.get('articles')
        for j in temp:
            universe.append(j)

    print(len(universe))
    for i in universe:
        if i.get('content'):
            newsl.append(i.get('content'))
            urls.append(i.get('url'))
            title.append(i.get('title'))
    l1 = []
    l2 = []

    for i in newsl:
        for j in i.split():
            l1.append(j.lower())

    for j in test.split():
        l2.append(j.lower())

    intersection = list(set([value for value in l1 if value in l2 and len(value) > 3]))
    truthfulness = True if len(intersection) > 2 else False
    links = {title[i]: urls[i] for i in range(len(title))}
    d = {"truthfulness": truthfulness, "links":links}
    return d


"""
Input: Maharashtra lockdown extend till 30 april
Tag words: trump US open
"""

"""news = "Donald Trump says he is 'very close' to completing a plan to reopen US"
tags = "trump US open"
supreme(tags.lower(), news)"""

