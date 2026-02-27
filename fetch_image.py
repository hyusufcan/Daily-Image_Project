#!/usr/bin/env python3
"""
Fetch a random historical image from Wikimedia Commons
and analyze it using HuggingFace's LLaVA model.

Wikimedia Commons provides FREE access to millions of historical images
including the British Library collection - perfect for Victorian-era imagery.
NO API KEY NEEDED for Wikimedia!
"""

import os
import json
import requests
import random
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Only HuggingFace API key needed
HF_API_KEY = os.getenv('HF_API_KEY')
LLAVA_API_URL = "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf"


def get_random_photo():
    """
    Fetch a random historical image from Wikimedia Commons.
    Completely FREE - no API key needed!
    """
    
    try:
        url = "https://commons.wikimedia.org/w/api.php"
        
        # Step 1: Get random files from Wikimedia Commons
        params = {
            'action': 'query',
            'list': 'random',
            'rnnamespace': '6',  # File namespace (images)
            'rnlimit': '500',
            'format': 'json'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        random_files = response.json()['query']['random']
        if not random_files:
            raise Exception("No files found in Wikimedia Commons")
        
        # Step 2: Get detailed file information
        file_titles = [f['title'] for f in random_files[:100]]
        
        file_info_params = {
            'action': 'query',
            'titles': '|'.join(file_titles),
            'prop': 'imageinfo|pageterms|descriptions',
            'iiprop': 'url|timestamp|user|extmetadata',
            'format': 'json'
        }
        
        info_response = requests.get(url, params=file_info_params, timeout=10)
        info_response.raise_for_status()
        
        pages = info_response.json()['query']['pages']
        
        # Filter for valid images
        valid_images = [
            p for p in pages.values() 
            if 'imageinfo' in p and p['imageinfo'][0]['url'].lower().endswith(
                ('.jpg', '.jpeg', '.png', '.gif')
            )
        ]
        
        if not valid_images:
            raise Exception("No valid images found")
        
        selected = random.choice(valid_images)
        img_info = selected['imageinfo'][0]
        
        # Extract metadata
        title = selected['title'].replace('File:', '').replace('_', ' ')
        description = selected.get('pageterms', {}).get('description', ['No description available'])[0]
        
        return {
            'id': selected.get('pageid'),
            'title': title,
            'description': description,
            'url': img_info['url'],  # Direct image URL
            'source_url': f"https://commons.wikimedia.org/wiki/{selected['title'].replace(' ', '_')}",
            'date_taken': img_info.get('timestamp', 'Unknown'),
            'uploader': img_info.get('user', 'Unknown'),
            'source': 'Wikimedia Commons',
            'tags': 'historical,public-domain'
        }
        
    except Exception as e:
        print(f"❌ Error fetching from Wikimedia Commons: {e}")
        return None

def analyze_image_with_llava(image_url):
    """Analyze image with HuggingFace LLaVA AI"""
    
    if not HF_API_KEY:
        print("⚠️ Warning: HF_API_KEY not set! Using fallback analysis...")
        return {
            'analysis': 'A fascinating glimpse into history from public domain archives.',
            'model': 'fallback',
            'analyzed_at': datetime.now().isoformat()
        }
    
    prompt = """Analyze this historical image from Wikimedia Commons archives. Provide:

1. **Visual Description**: What do you see? Describe the scene, people, objects, and setting in detail.

2. **Historical Context**: Based on visual clues (clothing, architecture, objects, style), estimate the time period and location.

3. **Artistic Elements**: Describe the composition, technique, and artistic style.

4. **Cultural Significance**: What does this image tell us about the society, culture, or technology of its time?

5. **Mood & Atmosphere**: What emotions or atmosphere does this image evoke?

Provide a scholarly, Victorian-era librarian analysis."""

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    
    payload = {
        "inputs": {
            "image": image_url,
            "text": prompt
        }
    }
    
    try:
        response = requests.post(LLAVA_API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return {
                'analysis': result[0].get('generated_text', 'Analysis completed'),
                'model': 'llava-1.5-7b-hf',
                'analyzed_at': datetime.now().isoformat()
            }
        else:
            print(f"⚠️ API returned status {response.status_code}")
            return {
                'analysis': 'Image analysis temporarily unavailable.',
                'model': 'fallback',
                'analyzed_at': datetime.now().isoformat()
            }
            
    except Exception as e:
        print(f"❌ Error in AI analysis: {e}")
        return {
            'analysis': 'A remarkable historical image worthy of scholarly study.',
            'model': 'fallback',
            'analyzed_at': datetime.now().isoformat()
        }

def save_daily_data(photo_data, analysis_data):
    """Save daily image data to JSON"""
    
    # Create directories
    Path('public/data').mkdir(parents=True, exist_ok=True)
    
    # Download and save image
    try:
        img_response = requests.get(photo_data['url'], timeout=10)
        img_response.raise_for_status()
        
        image_filename = f"daily-{datetime.now().strftime('%Y-%m-%d')}.jpg"
        Path('public/images').mkdir(parents=True, exist_ok=True)
        
        with open(f'public/images/{image_filename}', 'wb') as f:
            f.write(img_response.content)
            
        local_image = f'images/{image_filename}'
        
    except Exception as e:
        print(f"⚠️ Could not download image: {e}")
        local_image = None
    
    # Prepare daily data
    daily_data = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'photo': {
            'id': photo_data['id'],
            'title': photo_data['title'],
            'description': photo_data['description'],
            'source_url': photo_data['source_url'],
            'date_taken': photo_data['date_taken'],
            'uploader': photo_data['uploader'],
            'source': photo_data['source'],
            'local_image': local_image
        },
        'ai_analysis': analysis_data,
        'generated_at': datetime.now().isoformat()
    }
    
    # Save current day's data
    json_path = Path('public/data/daily-image.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(daily_data, f, indent=2, ensure_ascii=False)
    
    # Update archive (last 30 days)
    archive_file = Path('public/data/archive.json')
    archive = []
    
    if archive_file.exists():
        with open(archive_file, 'r', encoding='utf-8') as f:
            archive = json.load(f)
    
    archive.insert(0, daily_data)  # Newest first
    archive = archive[:30]  # Keep only last 30 days
    
    with open(archive_file, 'w', encoding='utf-8') as f:
        json.dump(archive, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Daily image saved: {photo_data['title']}")

def main():
    """Main execution"""
    try:
        print("🔍 Fetching random historical image from Wikimedia Commons...")
        photo = get_random_photo()
        
        if not photo:
            print("❌ Failed to fetch image")
            return
        
        print(f"📸 Found: {photo['title']}")
        
        print("🤖 Analyzing with LLaVA AI...")
        analysis = analyze_image_with_llava(photo['url'])
        print("✨ Analysis complete!")
        
        print("💾 Saving data...")
        save_daily_data(photo, analysis)
        print("🎉 Done! Website updated.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()
