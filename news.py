import requests
def getNews():
    url = "https://inshorts.vercel.app/news/all?offset=0&limit=10"
    response = requests.get(url)
    newsdata = response.json()["data"]["articles"]
    return newsdata
