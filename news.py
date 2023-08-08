import requests
def getNews():
    url = "https://inshorts.me/news/all?offset=0&limit=10"
    response = requests.get(url)
    newsdata = response.json()["data"]["articles"]
    return newsdata
