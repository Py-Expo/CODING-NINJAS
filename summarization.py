from newspaper import Article
from newsscraper import *
from translator import *

lang=''

CategDict={'World':'https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Home':'https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Local':'https://news.google.com/rss/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNREU1Wm1NMGVnc0tDUzl0THpBeE9XWmpOQ2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNREU1Wm1NMEtBQVABUAE?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Business':'https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Technology':'https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Entertainment':'https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Sports':'https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Science':'https://news.google.com/rss/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen',
           'Health':'https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'}

Content=[]

Index=0

def getCateg(categ):
    if categ:
        return CategDict[categ]
    else:
        return 'Home'
    

def get_articles(language,categ=None):
    global lang
    lang = language
    articles=[]
    url=scrape_google_news_rss(getCateg(categ))
    for article_url in url:
        articles.append(article_url['link'])
    return getContent(articles)

def translate(content):
    return translate_the_content(content,lang)

def getContent(articles):
    global Index
    Content=[]
    articles=articles[Index:]
    print(len(articles))
    for url in articles:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            news={'Link':url,'Title': translate(article.title),'Authors':article.authors,'Date':article.publish_date,'Summary':translate(article.summary),'Image':article.top_image}
            Content.append(news)
            if len(Content)>20:
                Index+=20
                break
        except:
            continue
    print(Content)

    return Content

        
        



    



