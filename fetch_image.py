import os
import json
import requests
import random
from datetime import datetime
from pathlib import Path

# Flickr API yapılandırması
FLICKR_API_KEY = os.getenv('FLICKR_API_KEY')
FLICKR_USER_ID = '12403504@N02'  # British Library Flickr ID
HF_API_KEY = os.getenv('HF_API_KEY')

# Hugging Face LLaVA API
LLAVA_API_URL = "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf"

def get_random_photo():
    """Flickr'dan rastgele bir fotoğraf çek"""
    
    # British Library koleksiyonundan fotoğrafları al
    url = "https://api.flickr.com/services/rest/"
    params = {
        'method': 'flickr.people.getPublicPhotos',
        'api_key': FLICKR_API_KEY,
        'user_id': FLICKR_USER_ID,
        'per_page': 500,  # Fazla sayıda çek ki rastgele seçim yapabiliriz
        'format': 'json',
        'nojsoncallback': 1,
        'extras': 'url_o,url_l,description,date_taken,tags'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'photos' not in data or not data['photos']['photo']:
        raise Exception("Fotoğraf bulunamadı")
    
    # Rastgele bir fotoğraf seç
    photos = data['photos']['photo']
    photo = random.choice(photos)
    
    # En yüksek kaliteli URL'yi al
    image_url = photo.get('url_o') or photo.get('url_l')
    
    return {
        'id': photo['id'],
        'title': photo.get('title', 'Untitled'),
        'description': photo.get('description', {}).get('_content', ''),
        'url': image_url,
        'flickr_url': f"https://www.flickr.com/photos/{FLICKR_USER_ID}/{photo['id']}",
        'date_taken': photo.get('datetaken', ''),
        'tags': photo.get('tags', '')
    }

def analyze_image_with_llava(image_url):
    """LLaVA ile görüntü analizi yap"""
    
    # Analiz için prompt
    prompt = """Analyze this historical image from the British Library collection. Provide:

1. **Visual Description**: What do you see in the image? Describe the scene, people, objects, and setting in detail.

2. **Historical Context**: Based on visual clues (clothing, architecture, objects, style), estimate the time period and geographical location.

3. **Artistic Elements**: Describe the composition, technique (engraving, photograph, illustration), and artistic style.

4. **Cultural Significance**: What might this image tell us about the society, culture, or technology of its time?

5. **Mood & Atmosphere**: What emotions or atmosphere does this image evoke?

Provide a rich, scholarly analysis as if you were a Victorian-era librarian cataloging this treasure."""

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    
    # Görüntüyü indir
    img_response = requests.get(image_url)
    
    # LLaVA API'ye gönder
    payload = {
        "inputs": {
            "image": image_url,
            "text": prompt
        }
    }
    
    response = requests.post(LLAVA_API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        # Fallback: Basit bir analiz
        return {
            'analysis': 'A fascinating glimpse into history from the British Library archives.',
            'model': 'fallback'
        }
    
    result = response.json()
    
    return {
        'analysis': result.get('generated_text', result),
        'model': 'llava-1.5-7b-hf',
        'analyzed_at': datetime.now().isoformat()
    }

def save_daily_data(photo_data, analysis_data):
    """Günlük veriyi JSON olarak kaydet"""
    
    # Dizinleri oluştur (public altına)
    Path('public/data').mkdir(parents=True, exist_ok=True)
    Path('public/images').mkdir(parents=True, exist_ok=True)
    
    # Görüntüyü indir ve kaydet
    img_response = requests.get(photo_data['url'])
    image_filename = f"daily-{datetime.now().strftime('%Y-%m-%d')}.jpg"
    
    with open(f'public/images/{image_filename}', 'wb') as f:
        f.write(img_response.content)
    
    # JSON verisi
    daily_data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'photo': {
            'id': photo_data['id'],
            'title': photo_data['title'],
            'description': photo_data['description'],
            'flickr_url': photo_data['flickr_url'],
            'date_taken': photo_data['date_taken'],
            'tags': photo_data['tags'],
            'local_image': f'images/{image_filename}'
        },
        'ai_analysis': analysis_data,
        'generated_at': datetime.now().isoformat()
    }
    
    # Güncel veriyi kaydet (public/data altına)
    with open('public/data/daily-image.json', 'w', encoding='utf-8') as f:
        json.dump(daily_data, f, indent=2, ensure_ascii=False)
    
    # Arşive ekle (public/data altına)
    archive_file = 'public/data/archive.json'
    archive = []
    
    if os.path.exists(archive_file):
        with open(archive_file, 'r', encoding='utf-8') as f:
            archive = json.load(f)
    
    archive.insert(0, daily_data)  # En yeni başta
    archive = archive[:30]  # Son 30 günü tut
    
    with open(archive_file, 'w', encoding='utf-8') as f:
        json.dump(archive, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Daily image saved: {photo_data['title']}")

def main():
    try:
        if not FLICKR_API_KEY:
            # Fallback for manual run without API key (only if we wanted to test, but let's encourage setting it)
            # For now just print warning
            print("⚠️ Warning: FLICKR_API_KEY not set!")
            
        print("🔍 Fetching random image from British Library...")
        photo = get_random_photo()
        print(f"📸 Found: {photo['title']}")
        
        print("🤖 Analyzing with LLaVA AI...")
        analysis = analyze_image_with_llava(photo['url'])
        print("✨ Analysis complete!")
        
        print("💾 Saving data...")
        save_daily_data(photo, analysis)
        print("🎉 Done!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

if __name__ == "__main__":
    main()
