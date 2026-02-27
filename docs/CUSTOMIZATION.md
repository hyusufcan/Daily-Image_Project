# 🎨 Özelleştirme Rehberi

## 1. Flickr Koleksiyonunu Değiştir

### Adım 1: Yeni Flickr User ID Bul

1. https://www.flickr.com gidin
2. Beğendiğiniz koleksiyonu bulun
3. Profil resmini sağ tıklayın → "İncelemeyi Aç" → HTML'de `nsid` arayın
4. Veya URL'den: `flickr.com/photos/<user_id_here>/`

### Adım 2: Script'i Güncelle

**Dosya:** `scripts/fetch_image.py` (satır ~10)

```python
# British Library (varsayılan)
FLICKR_USER_ID = '12403504@N02'

# Başka örnekler:
# Library of Congress
FLICKR_USER_ID = '8623220@N02'

# Smithsonian Institution
FLICKR_USER_ID = '35591378@N03'

# National Archives
FLICKR_USER_ID = '79371075@N04'

# Kendi user'ınız
FLICKR_USER_ID = 'your_user_id@N02'
```

### Adım 3: Test Et
```bash
python scripts/fetch_image.py
```

---

## 2. AI Analizini Özelleştir

### Adım 1: Prompt'u Değiştir

**Dosya:** `scripts/fetch_image.py` (satır ~55)

```python
# Varsayılan prompt
prompt = """Analyze this historical image from the British Library collection. Provide:

1. **Visual Description**: What do you see in the image?
2. **Historical Context**: Estimate the time period and location.
3. **Artistic Elements**: Describe composition and technique.
4. **Cultural Significance**: What does this tell us about the era?
5. **Mood & Atmosphere**: What emotions does this evoke?

Provide a rich, scholarly analysis as if you were a Victorian-era librarian."""

# Özelleştirilmiş prompt örneği
prompt = """Analyze this archival photograph and provide:

1. **Technical Analysis**
   - Photography technique (wet plate, daguerreotype, etc.)
   - Film type and era estimation
   - Lighting and composition

2. **Subject Matter**
   - People, places, objects
   - Context and narrative
   
3. **Preservation Notes**
   - Current condition
   - Recommended restoration

Keep it concise and technical."""
```

### Adım 2: Daha Detaylı Analiz İçin

```python
# LLaVA modeli değiştir (daha güçlü)
# llava-1.5-7b-hf → llava-hf/llava-1.5-13b-hf (daha yavaş ama daha iyi)
LLAVA_API_URL = "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-13b-hf"

# veya çoklu analiz çıktısı al
def analyze_image_with_llava_multiple(image_url):
    prompts = [
        "What is this image about?",
        "When was this taken?",
        "What artifacts are visible?"
    ]
    
    results = []
    for prompt in prompts:
        result = analyze_image_with_llava(image_url, prompt)
        results.append(result)
    
    return results
```

---

## 3. Website Tasarımını Değiştir

### Adım 1: Renkleri Değiştir

**Dosya:** `public/index.html` (satır ~20-30)

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                // Varsayılan (Victorian Gold)
                "primary": "#d5b034",
                "background-light": "#f8f7f6",
                "background-dark": "#1a1614",
                
                // Modern Blue Theme
                "primary": "#0066ff",
                "background-light": "#f0f4f8",
                "background-dark": "#1a1f3a",
            },
        },
    },
}
```

### Adım 2: Yazı Tiplerini Değiştir

```html
<!-- Mevcut -->
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&display=swap" rel="stylesheet"/>

<!-- Modern alternatif -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet"/>

<!-- Tailwind'de güncelle -->
fontFamily: {
    "display": ["Poppins", "sans-serif"]  // serif'ten sans-serif'e
}
```

### Adım 3: Layout'u Değiştir

**Dosya:** `public/index.html` (satır ~130)

```html
<!-- Varsayılan: 2 sütunlu analiz -->
<div class="grid grid-cols-1 md:grid-cols-2 gap-12">
    <div id="analysis-col-1">...</div>
    <div id="analysis-col-2">...</div>
</div>

<!-- Tek sütun versiyonu -->
<div class="grid grid-cols-1 gap-12">
    <div id="analysis-full">...</div>
</div>

<!-- 3 sütunlu (masaüstü için) -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
    <div id="analysis-col-1">...</div>
    <div id="analysis-col-2">...</div>
    <div id="analysis-col-3">...</div>
</div>
```

### Adım 4: Animasyonları Değiştir

```css
/* Mevcut: Yavaş fade-in (1000ms) */
main {
    transition: opacity duration-1000;
}

/* Hızlı fade-in (300ms) */
main {
    transition: opacity duration-300;
}

/* Veya özel animasyon */
@keyframes slideInUp {
    from {
        transform: translateY(30px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

main {
    animation: slideInUp 0.6s ease-out;
}
```

---

## 4. Veri Modeli Değişiklikleri

### Adım 1: JSON Yapısını Genişlet

**Dosya:** `scripts/fetch_image.py` (satır ~110)

```python
# Varsayılan veri
daily_data = {
    'date': datetime.now().strftime('%Y-%m-%d'),
    'photo': {...},
    'ai_analysis': {...},
    'generated_at': datetime.now().isoformat()
}

# Genişletilmiş veri
daily_data = {
    'date': datetime.now().strftime('%Y-%m-%d'),
    'photo': {...},
    'ai_analysis': {...},
    'metadata': {
        'region': 'London',  # Yeni
        'collection': 'British Library',  # Yeni
        'keywords': ['history', 'archive'],  # Yeni
        'quality_score': 0.85,  # Yeni (1-1.0 scale)
    },
    'statistics': {
        'view_count': 0,  # Analytics için
        'favorite_count': 0,
    },
    'generated_at': datetime.now().isoformat()
}
```

### Adım 2: Frontend'de Yeni Veriyi Göster

**Dosya:** `public/index.html` (satır ~300)

```html
<!-- Varsayılan: Footer'da basit bilgi -->
<div id="footer-tags">...</div>

<!-- Genişletilmiş: Metadata paneli -->
<div class="metadata-panel">
    <div>Region: <span id="region">Loading...</span></div>
    <div>Collection: <span id="collection">Loading...</span></div>
    <div>Quality: <span id="quality">Loading...</span></div>
    <div>Views: <span id="views">0</span></div>
</div>

<!-- JavaScript'te ekle -->
<script>
function displayContent(data) {
    // ...
    document.getElementById('region').textContent = data.metadata?.region || 'Unknown';
    document.getElementById('collection').textContent = data.metadata?.collection || 'British Library';
    document.getElementById('quality').textContent = (data.metadata?.quality_score * 100).toFixed(0) + '%';
}
</script>
```

---

## 5. Zaman Dilimi Değişiklikleri

### Cron Zamanını Değiştir

**Dosya:** `.github/workflows/daily-image.yml` (satır ~5)

```yaml
# Varsayılan: Her gün saat 09:00 UTC
- cron: '0 9 * * *'

# Saat 12:00 UTC (13:00 CET, 15:00 EET)
- cron: '0 12 * * *'

# Haftada bir (Pazartesi 09:00 UTC)
- cron: '0 9 * * 1'

# 6 saatte bir
- cron: '0 */6 * * *'

# Her 30 dakikada bir (development/test için)
- cron: '*/30 * * * *'
```

---

## 6. Netlify Hostname Özelleştirmesi

### Custom Domain Ayarla

1. Netlify Dashboard → Site settings
2. Domain management → Add custom domain
3. DNS kaydını güncelleştir
4. SSL sertifikasını aktifleştir (otomatik)

**Örnek:**
```
Varsayılan: https://abc123xyz.netlify.app
Özel: https://dailyantiquarian.com
```

---

## 7. GitHub Actions Parallelization

### Multiple Analyses Çalıştır

```python
# Birden fazla model ile analiz et
def analyze_image_multimodal(image_url):
    analyses = {
        'llava': analyze_with_llava(image_url),
        'clip': analyze_with_clip(image_url),
        'ocr': extract_text_with_ocr(image_url)
    }
    return analyses
```

---

## 8. Yedekleme & Arşivleme

### S3'e Backup Al

```python
import boto3

def backup_to_s3(daily_data):
    s3 = boto3.client('s3')
    date = daily_data['date']
    
    # JSON verisi
    s3.put_object(
        Bucket='my-backup-bucket',
        Key=f'data/{date}.json',
        Body=json.dumps(daily_data)
    )
    
    # Görüntü
    with open(f"public/images/daily-{date}.jpg", 'rb') as f:
        s3.put_object(
            Bucket='my-backup-bucket',
            Key=f'images/{date}.jpg',
            Body=f
        )
```

---

## 9. Hızlı Özelleştirme Cheatsheet

| Öğe | Dosya | Satır | Değişiklik |
|-----|-------|-------|-----------|
| Flickr User | `scripts/fetch_image.py` | ~10 | FLICKR_USER_ID |
| AI Prompt | `scripts/fetch_image.py` | ~55 | prompt string |
| Renk Paleti | `public/index.html` | ~24 | colors object |
| Yazı Tipi | `public/index.html` | ~7 | fonts.googleapis.com |
| Cron Time | `.github/workflows/daily-image.yml` | ~5 | cron expression |
| Layout | `public/index.html` | ~130 | grid-cols-{N} |
| Archive Boyutu | `scripts/fetch_image.py` | ~125 | archive[:30] |

---

## 10. Test Before Deploy

```bash
# Local test
python scripts/fetch_image.py

# JSON validation
python -m json.tool public/data/daily-image.json

# HTML validation
# Online tool: https://validator.w3.org/

# Website preview
python -m http.server 8000
# http://localhost:8000/public/ ziyaret et
```

