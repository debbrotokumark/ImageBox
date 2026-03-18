import requests
import os

API_KEY = ""   # 🔥 put your key here
headers = {"Authorization": API_KEY}

topic = "cat"
per_page = 10

url = f"https://api.pexels.com/v1/search?query={topic}&per_page={per_page}"

res = requests.get(url, headers=headers)

if res.status_code != 200:
    print("❌ API Error:", res.text)
    exit()

data = res.json()
startNumber=0

os.makedirs(topic, exist_ok=True)

for i, photo in enumerate(data["photos"]):
    img_url = photo["src"]["large"]  # smaller than original (faster)

    try:
        img_data = requests.get(img_url).content
        with open(f"{topic}/{topic}-{i+1+startNumber}.jpg", "wb") as f:
            f.write(img_data)
        print(f"✅ Downloaded {topic}-{i+1+startNumber}.jpg")
    except:
        print(f"⚠ Failed to download image {i+1+startNumber}")

print("🎉 All done!")
