# 🚀 Deployment Rehberi

Lokal testinden production ortamına geçiş adımları.

---

## 1️⃣ Production Checklist

Deployment öncesi kontrol et:

- [ ] Tüm API key'ler geçerli mi?
- [ ] JSON veri geçerli mi? (`python -m json.tool public/data/daily-image.json`)
- [ ] HTML responsive mi? (Chrome DevTools)
- [ ] Fetch script'i local'de çalışıyor mu?
- [ ] GitHub Actions workflow etkinleştirilmiş mi?
- [ ] Netlify deployment hazır mı?

---

## 2️⃣ GitHub Setup

### Fork & Secrets

```bash
# 1. Repository'yi fork et
# GitHub → "Fork" butonuna tıkla

# 2. Secrets ekle
# Settings → Secrets and variables → Actions
# Add these:
FLICKR_API_KEY = your_flickr_key
HF_API_KEY = your_hugging_face_token
```

### Repository Settings

```bash
# 1. Actions workflow'u enable et
# Actions tab → Enable workflows

# 2. Commit permissions
# Settings → Actions → General
# "Read and write permissions" seç
```

---

## 3️⃣ Netlify Deployment

### Seçenek A: Automatic Deployment

```
1. https://app.netlify.com aç
2. "Add new site" → "Import an existing project"
3. GitHub seç → Repository seç
4. Build settings:
   - Build command: echo 'Static site'
   - Publish directory: public
5. Deploy
```

### Seçenek B: Netlify CLI

```bash
npm install -g netlify-cli
netlify login
netlify init
netlify deploy --prod
```

### Netlify Environment Variables

```
Settings → Build & deploy → Environment
Add:
FLICKR_API_KEY = [from GitHub Secrets]
HF_API_KEY = [from GitHub Secrets]
```

---

## 4️⃣ GitHub Actions Workflow Doğrulama

**Dosya:** `.github/workflows/daily-image.yml`

```yaml
name: Daily British Library Image

on:
  schedule:
    - cron: '0 9 * * *'  # 09:00 UTC her gün
  workflow_dispatch:     # Manual tetikle

jobs:
  fetch-and-analyze:
    runs-on: ubuntu-latest
    
    steps:
      # ... tüm steps başarılı mı kontrol et
```

**Test et:**
1. Actions tab → "Daily British Library Image"
2. "Run workflow" → "Run workflow"
3. Çalıştığını kontrol et

---

## 5️⃣ Monitoring & Maintenance

### GitHub Actions Notifications

```
Settings → Notifications → Actions
- Enable: "On workflow job failure"
```

### Netlify Monitoring

```
https://app.netlify.com
→ your-site → Analytics
→ Deploy history kontrol et
```

### Manual Backup

```bash
# Her ay bir kez backup al
git clone your-repo backup-[date]
cd backup-[date]

# Data klasörünü sakla
cp -r public/data backup-data/
```

---

## 6️⃣ Troubleshooting Deployment

### "Workflow başlamıyor"

```
1. .github/workflows/ klasörü var mı?
2. Workflow YAML sözdizimi doğru mu?
3. Secrets ayarlanmış mı?
```

### "API error 401"

```
1. GitHub Secrets'teki key'ler geçerli mi?
2. Flickr/HF key'leri süresi doldu mu?
3. Yeni key'lerle güncelle
```

### "Netlify deploy başarısız"

```
1. Deploy logs kontrol et
2. Build command çıktısını gözle
3. Publish directory doğru mu?
```

---

## 7️⃣ Performance Optimization

### Image Optimization

```python
# fetch_image.py'da ekle:
from PIL import Image

def optimize_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((1200, 900), Image.Resampling.LANCZOS)
    img.save(image_path, quality=85, optimize=True)
```

### Cache Strategy

**Netlify.toml:**
```toml
[[headers]]
  for = "/data/*"
  [headers.values]
    Cache-Control = "max-age=3600"  # 1 hour

[[headers]]
  for = "/images/*"
  [headers.values]
    Cache-Control = "max-age=604800"  # 1 week
```

---

## 8️⃣ Scaling (Opsiyonel)

### Multiple Collections

```python
# Çoklu Flickr koleksiyonları kullan
collections = [
    {'user_id': '12403504@N02', 'name': 'British Library'},
    {'user_id': '8623220@N02', 'name': 'Library of Congress'},
]

for collection in collections:
    photo = get_random_photo(collection['user_id'])
```

### Caching Layer

```python
# Redis kullan (expensive ama hızlı)
import redis
cache = redis.Redis(host='localhost', port=6379)

def get_photo_with_cache():
    cached = cache.get('daily_photo')
    if cached:
        return json.loads(cached)
    # ... fetch
```

---

## 9️⃣ Custom Domain

### Netlify Domain Setup

```
1. Netlify Dashboard → Site settings
2. Domain management → Add custom domain
3. DNS records güncelleştir
4. SSL otomatik etkinleşir
```

---

## 🔟 Disaster Recovery

### Rollback to Previous Version

```bash
git log --oneline
git revert <commit-hash>
git push
# Netlify otomatik redeploy eder
```

### Data Recovery

```bash
# Archive'den restore
cp public/data/archive.json public/data/daily-image.json
git add public/data/daily-image.json
git commit -m "Data recovery: $(date)"
git push
```

---

## Security Best Practices

### API Keys

- ✅ GitHub Secrets kullan (nunca commit et)
- ✅ Key'leri 90 günde bir rotate et
- ✅ Exposed key'i hemen değiştir

### Rate Limiting

```python
# GitHub Actions'ı bir kez/gün çalıştır (cron)
# LLaVA API 100 req/min limit (ok)
# Flickr API 1 req/sec (ok)
```

### CORS & CSP

```
Netlify Headers:
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: ...
```

---

## 📞 Support

| Sorun | Çözüm | Dosya |
|-------|-------|-------|
| Deployment fails | Check logs | `docs/TROUBLESHOOTING.md` |
| API errors | Refresh keys | `docs/API.md` |
| Performance | Optimize | `docs/DEPLOYMENT.md` |

---

**Production'a hazır!** 🚀

