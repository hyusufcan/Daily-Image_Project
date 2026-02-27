# 🖼️ FLICKR ALTERNATIFLERI - ÜCRETSİZ API'LER

Flickr API bedava değil → Diğer seçenekler:

---

## ✅ OPTION 1: WIKIMEDIA COMMONS API (✨ RECOMMENDED)

**Avantaj:**
- ✅ Tamamen FREE
- ✅ Tarihi fotoğraflar çok
- ✅ Public domain
- ✅ Victorian-era images perfect

**British Library Commons:**
- URL: https://commons.wikimedia.org/wiki/Category:British_Library
- API: https://commons.wikimedia.org/w/api.php
- Rate limit: 50 requests/second

**Örnek Code:**
```python
import requests
import random

def get_random_historical_image():
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'allimages',
        'aisort': 'timestamp',
        'aidir': 'descending',
        'ailimit': 500,
        'aiprop': 'url|timestamp|user',
        'format': 'json',
        'aicontinue': '0'
    }
    
    response = requests.get(url, params=params)
    images = response.json()['query']['allimages']
    selected = random.choice(images)
    
    return {
        'title': selected['name'],
        'url': f"https://commons.wikimedia.org/wiki/File:{selected['name']}",
        'date_taken': selected['timestamp'],
        'uploader': selected['user']
    }
```

---

## ✅ OPTION 2: RIJKSMUSEUM API

**Amsterdam Museum (Rembrandt, Dutch Masters)**
- URL: https://data.rijksmuseum.nl/object-metadata/api/
- FREE tier: 100.000 requests/month
- Key gerekli ama bedava

**Örnek:**
```python
def get_rijksmuseum_image():
    api_key = os.getenv('RIJKSMUSEUM_API_KEY')
    url = "https://data.rijksmuseum.nl/object-metadata/api/"
    
    params = {
        'imgonly': 'true',
        'ps': 500,
        'format': 'json',
        'apiKey': api_key
    }
    
    response = requests.get(url, params=params)
    objects = response.json()['artObjects']
    return random.choice(objects)
```

**API Key:** https://data.rijksmuseum.nl/object-metadata/api/ (free registration)

---

## ✅ OPTION 3: PUBLIC DOMAIN ARCHIVE

**Archive.org Metadata API**
- URL: https://archive.org/advancedsearch.php
- Collections: Books, images, audio
- NO key needed
- FREE

**Örnek:**
```python
def get_archive_image():
    url = "https://archive.org/advancedsearch.php"
    
    params = {
        'q': 'historical photographs 1800s',
        'fl': 'identifier,title,date',
        'output': 'json',
        'rows': 500
    }
    
    response = requests.get(url, params=params)
    docs = response.json()['response']['docs']
    return random.choice(docs)
```

---

## ✅ OPTION 4: EUROPEANA API

**European Cultural Heritage**
- URL: https://www.europeana.eu/api/
- 20 milyon + item
- FREE tier: 2 requests/second
- Key gerekli (free)

**Örnek:**
```python
def get_europeana_image():
    api_key = os.getenv('EUROPEANA_API_KEY')
    url = "https://api.europeana.eu/record/v2/search"
    
    params = {
        'query': 'british history 1800',
        'wskey': api_key,
        'format': 'json',
        'rows': 500,
        'media': 'true'
    }
    
    response = requests.get(url, params=params)
    items = response.json()['items']
    return random.choice(items)
```

**API Key:** https://pro.europeana.eu/page/apis (free registration)

---

## ✅ OPTION 5: LIBRARY OF CONGRESS API

**American Historical Photos**
- URL: https://www.loc.gov/apis/
- NO authentication needed
- FREE
- 16+ milyon items

**Örnek:**
```python
def get_loc_image():
    url = "https://www.loc.gov/collections/selected-collections/?fo=json"
    
    params = {
        'q': 'victorian era photographs',
        'fo': 'json',
        'at': 'results'
    }
    
    response = requests.get(url, params=params)
    results = response.json()['results']
    return random.choice(results)
```

---

## 🏆 MY RECOMMENDATION: WIKIMEDIA COMMONS

**Neden?**
1. ✅ 100% FREE
2. ✅ No authentication
3. ✅ British Library collection çok
4. ✅ Victorian-era perfect
5. ✅ Public domain
6. ✅ High quality images
7. ✅ API stable ve güvenilir

---

## 🔄 FETCH_IMAGE.PY UPDATE

Wikimedia Commons ile update etmeli:

```python
import requests
import json
import random
from datetime import datetime
from pathlib import Path
import os

def get_random_historical_image():
    """Wikimedia Commons'tan random historical image al"""
    try:
        url = "https://commons.wikimedia.org/w/api.php"
        
        # Search for historical British photographs
        params = {
            'action': 'query',
            'list': 'random',
            'rnnamespace': '6',  # File namespace
            'rnlimit': '500',
            'format': 'json'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        random_files = response.json()['query']['random']
        
        # Get file info
        file_info_params = {
            'action': 'query',
            'titles': '|'.join([f['title'] for f in random_files]),
            'prop': 'imageinfo|pageterms',
            'iiprop': 'url|timestamp|user',
            'format': 'json'
        }
        
        info_response = requests.get(url, params=file_info_params, timeout=10)
        info_response.raise_for_status()
        
        pages = info_response.json()['query']['pages']
        valid_images = [p for p in pages.values() if 'imageinfo' in p]
        
        if not valid_images:
            return None
            
        selected = random.choice(valid_images)
        img_info = selected['imageinfo'][0]
        
        return {
            'title': selected['title'],
            'url': img_info['url'],
            'description': selected.get('title', 'Historical Image'),
            'date_taken': img_info['timestamp'],
            'source': 'Wikimedia Commons',
            'uploader': img_info['user']
        }
        
    except Exception as e:
        print(f"Error fetching from Wikimedia: {e}")
        return None

def analyze_image_with_llava(image_url):
    """LLaVA ile AI analysis"""
    try:
        api_key = os.getenv('HF_API_KEY')
        
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "inputs": image_url
        }
        
        response = requests.post(
            "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        else:
            return "Unable to analyze image at this time."
            
    except Exception as e:
        print(f"Error in AI analysis: {e}")
        return "Analysis unavailable."

def save_daily_data(photo_info, ai_analysis):
    """JSON'a kaydet"""
    daily_data = {
        'date': datetime.now().isoformat(),
        'photo': photo_info,
        'ai_analysis': {
            'analysis': ai_analysis,
            'model': 'LLaVA 1.5 7B',
            'analyzed_at': datetime.now().isoformat()
        },
        'generated_at': datetime.now().isoformat()
    }
    
    json_path = Path('public/data/daily-image.json')
    json_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(json_path, 'w') as f:
        json.dump(daily_data, f, indent=2)

def main():
    print("Fetching random historical image...")
    
    photo = get_random_historical_image()
    
    if photo:
        print(f"✅ Image: {photo['title']}")
        
        analysis = analyze_image_with_llava(photo['url'])
        print(f"✅ Analysis: {analysis[:100]}...")
        
        save_daily_data(photo, analysis)
        print("✅ Saved to public/data/daily-image.json")
    else:
        print("❌ Failed to fetch image")

if __name__ == "__main__":
    main()
```

---

## 📋 .ENV UPDATE

```env
# Wikimedia Commons - NO KEY NEEDED
# Just use free API

# HuggingFace Token
HF_API_KEY=your_huggingface_token

# Optional: Alternative APIs
# EUROPEANA_API_KEY=your_key
# RIJKSMUSEUM_API_KEY=your_key
```

---

## ✅ HANGISINI SEÇMELİYİZ?

**WIKIMEDIA COMMONS** ← En iyi

Neden?
- 100% free
- No authentication
- British Library collection
- Victorian era perfect
- API reliable

---

## 📝 SONRAKI ADIMLAR

1. **fetch_image.py** update et → Wikimedia API
2. **GitHub push** et
3. **Workflow trigger** et (manual)
4. **Netlify deploy** otomatik yapacak
5. **https://dailyimage.netlify.app/** kontrol et

**HuggingFace token'ı sadece HF_API_KEY'e ekleyecek!**

---

## 🎯 READY?

Wikimedia API ile fetch_image.py update edelim! ✅

