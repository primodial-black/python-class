


import requests

api_key="63b79167f79043a29a1b83f3b5b7f944"

def news():
    main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news=requests.get(main_url).json()
    # print(news)
    article=news["articles"]
    # print(article)

    news_article=[]
    for arti in article:
        news_article+=[(f"TITLE : {arti['title']}\n====NEWS=== : {arti['content']}\n")]
        # print(news_article)

    for i in range(len(news_article)):
        print(i+1,news_article[i])





news()
















    