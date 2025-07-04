import json
from os import getenv
 
import requests
from dotenv import load_dotenv

# .env faylidan muhit o'zgaruvchilarini yuklash
load_dotenv()

# API kalitini muhit o'zgaruvchilaridan olish
RAPID_KEY = getenv('RAPID_KEY')

# Instagramdan media yuklab olish funksiyasi
def download_instagram(link):
    url = "https://instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com/convert"

    querystring = {"url"
                   : link}

    headers = {
        "x-rapidapi-key": RAPID_KEY,
        "x-rapidapi-host": "instagram-downloader-download-instagram-stories-videos4.p.rapidapi.com"
    }

    # API ga so'rov yuborish
    response = requests.get(url, headers=headers, params=querystring)
    # JSON javobni tahlil qilish
    result = json.loads(response.text)
    return result