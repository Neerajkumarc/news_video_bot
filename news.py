import requests
def getNews():
    url = "https://inshorts-news.vercel.app/all"
    response = requests.get(url)
    newsdata = response.json()["data"]
    return newsdata
