import requests
import os

API_KEY = "p5kVDtufCtK4g1rg9q5bKxAoF7vDVta9EaqXjtEy0GJEmgKtf00OipI0"   # 🔥 put your key here
headers = {"Authorization": API_KEY}

topic = "fast-food"
per_page = 30

url = f"https://api.pexels.com/v1/search?query={topic}&per_page={per_page}"

res = requests.get(url, headers=headers)

if res.status_code != 200:
    print("❌ API Error:", res.text)
    exit()

data = res.json()
startNumber=150

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
