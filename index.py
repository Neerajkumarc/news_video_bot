import news
import requests
import videomaker
from gtts import gTTS
import os, time


print("Welcome To NewsVideoMaking Bot")
print("gathering news data...")
newsData = news.getNews()
numberOfVideos = int(input("Enter the number of videos you want to create (1-10): "))

for i in range(numberOfVideos):
    print(f"\nWorking on video {i+1}...")
    text = newsData[i]["content"]
    imageUrl = newsData[i]["imageUrl"]
    image = requests.get(imageUrl)  
    if (image.status_code == 200):
        with open("image.jpg", "wb") as f:
            f.write(image.content)

    myobj = gTTS(text=text, lang="en", slow=False, tld='co.in')
    myobj.save("news.mp3")
    videomaker.videoMaker("image.jpg", text, "news.mp3", f"output/output{i+1}.mp4")
    time.sleep(1)
    os.remove("image.jpg")
    os.remove("news.mp3")
    print(f"Completed video {i+1}.\n")






   




