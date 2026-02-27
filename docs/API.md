# 🔗 API Referansı

## Flickr API

### Konfigürasyon
```
- Endpoint: https://api.flickr.com/services/rest/
- Method: GET
- Format: JSON
```

### Rate Limits
- **Limit:** 3,600 requests/hour (1 request/second)
- **User ID:** 12403504@N02 (British Library)
- **Collection Size:** 1M+ photos

### Parametreler
| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| `method` | flickr.people.getPublicPhotos | Halkla açık fotoğrafları getir |
| `user_id` | 12403504@N02 | British Library ID |
| `per_page` | 500 | Sayfada 500 foto (max) |
| `format` | json | JSON formatında cevap |
| `extras` | url_o,url_l,description,date_taken,tags | İlişkili bilgiler |

### Yanıt Örneği
```json
{
  "photos": {
    "photo": [
      {
        "id": "123456789",
        "title": "Historical Image",
        "description": {"_content": "Description text"},
        "url_o": "https://live.staticflickr.com/...",
        "url_l": "https://live.staticflickr.com/...",
        "datetaken": "2020-05-15 12:00:00",
        "tags": "history archive london"
      }
    ]
  }
}
```

### Hata Yönetimi
```python
# Success: status_code == 200
# Timeout: 30 seconds default
# Retry: 3x exponential backoff
# Fallback: Generic message if all retries fail
```

---

## Hugging Face LLaVA API

### Konfigürasyon
```
- Model: llava-hf/llava-1.5-7b-hf
- Endpoint: https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf
- Method: POST
- Content-Type: application/json
```

### Authentication
```python
headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}
```

### Rate Limits
- **Limit:** 100 requests/minute (community tier)
- **Timeout:** 30 seconds
- **Max Input:** ~500KB image

### Request Payload
```json
{
  "inputs": {
    "image": "https://image_url_here.jpg",
    "text": "Analyze this historical image..."
  }
}
```

### Response Format
```json
{
  "generated_text": "Detailed analysis of the image..."
}
```

### Error Codes
| Code | Anlam | Çözüm |
|------|-------|-------|
| 401 | Unauthorized | Token geçerli mi? |
| 429 | Too Many Requests | Rate limit aşıldı, bekle |
| 500 | Server Error | HF sisteminde sorun, retry et |
| 504 | Gateway Timeout | Timeout, manual retry yapılabilir |

### Fallback Strategy
Eğer LLaVA başarısız olursa:
```python
{
  'analysis': 'A fascinating glimpse into history from the British Library archives.',
  'model': 'fallback',
  'error_reason': 'API timeout or error'
}
```

---

## Data API (Internal)

### JSON Data Structure

**File:** `public/data/daily-image.json`

```json
{
  "date": "2026-02-27",
  "photo": {
    "id": "123456789",
    "title": "Image Title",
    "description": "Original Flickr description",
    "flickr_url": "https://www.flickr.com/photos/12403504@N02/123456789/",
    "date_taken": "2020-05-15 12:00:00",
    "tags": "history archive london culture",
    "local_image": "images/daily-2026-02-27.jpg"
  },
  "ai_analysis": {
    "analysis": "Scholarly analysis of the image...",
    "model": "llava-1.5-7b-hf",
    "analyzed_at": "2026-02-27T10:30:45.123456"
  },
  "generated_at": "2026-02-27T10:30:45.123456"
}
```

**Usage:** Frontend loads this file and renders the daily image display.

---

### Archive Data Structure

**File:** `public/data/archive.json`

```json
[
  { /* Today's entry */ },
  { /* Yesterday's entry */ },
  { /* 2 days ago */ },
  ...
  { /* 30 days ago */ }
]
```

- **Limit:** Son 30 gün
- **Order:** Yeni tarihler başta
- **Total Size:** ~30-50MB (images dahil değil)

---

## Örnek İstekler

### Manual Flickr API Call
```bash
curl "https://api.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key=YOUR_KEY&user_id=12403504@N02&per_page=500&format=json&nojsoncallback=1&extras=url_o,url_l,description,date_taken,tags"
```

### Manual LLaVA API Call
```bash
curl -X POST \
  https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf \
  -H "Authorization: Bearer YOUR_HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {
      "image": "https://image_url.jpg",
      "text": "Analyze this image"
    }
  }'
```

---

## API Değişiklik Günlüğü

| Tarih | Değişiklik | Etki |
|-------|-----------|------|
| 2026-02-27 | İlk dokümantasyon | N/A |
| - | Henüz value API güncelleme yok | - |

