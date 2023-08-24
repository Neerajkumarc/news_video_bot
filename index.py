import news
import requests
import videomaker
import dateConversion
from gtts import gTTS
import os, time

print("\n",45*"-","\n \tWelcome To NewsVideoMaking Bot","\n",45*"-")
print("gathering news data...")
n_timeStart = time.time()
newsData = news.getNews()
n_timeEnd = time.time()
print(f"news data gathered. (finished in {(n_timeEnd-n_timeStart):.2f}s)")
while True:
    numberOfVideos = int(input("Enter the number of videos you want to create (1-10): "))
    if numberOfVideos >= 1 and numberOfVideos <= 10:
        break
    else:
        print("Invalid input. Please enter a value between 1 and 10.")


v_timeStart = time.time()
for i in range(numberOfVideos):
    print(f"\nWorking on video {i+1}...")
    text = newsData[i]["content"]
    imageUrl = newsData[i]["imageUrl"]
    image = requests.get(imageUrl)  
    newsSource = newsData[i]["sourceName"]
    newsDate = dateConversion.getDate(newsData[i]["createdAt"])
    if (image.status_code == 200):
        with open("image.jpg", "wb") as f:
            f.write(image.content)

    myobj = gTTS(text=text, lang="en", slow=False, tld='co.in')
    myobj.save("news.mp3")
    videomaker.videoMaker("image.jpg", text, newsSource, newsDate, "news.mp3", f"output/output{i+1}.mp4")
    os.remove("image.jpg")
    os.remove("news.mp3")
    print(f"Completed video {i+1}.\n")
v_timeEnd = time.time()
v_timeTotal =v_timeEnd-v_timeStart
print(f"{numberOfVideos} videos created successfully (finished in {(v_timeTotal):.2f}s)")




   




