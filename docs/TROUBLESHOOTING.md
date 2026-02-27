# 🔧 Sorun Giderme Rehberi

## Kurulum Sorunları

### "ModuleNotFoundError: No module named 'requests'"
**Sebep:** Python bağımlılıkları yüklü değil

**Çözüm:**
```bash
pip install -r requirements.txt
```

---

### "FLICKR_API_KEY ortam değişkeni bulunamadı"
**Sebep:** API key GitHub Secrets'te ayarlanmamış veya lokal ortamda .env dosyası yok

**Çözüm:**
```bash
# 1. Local testing için:
cp .env.example .env
# 2. .env dosyasını düzenle ve API key'leri ekle

# 3. GitHub'da workflow çalışması için:
# Settings → Secrets and variables → Actions
# - FLICKR_API_KEY ekle
# - HF_API_KEY ekle
```

---

## Workflow Sorunları

### "Workflow doesn't run at 9 AM"

**Kontrol Listesi:**
- [ ] GitHub Actions etkinleştirilmiş mi? (Actions sekmesine git)
- [ ] `daily-image.yml` dosyası `.github/workflows/` içinde mi?
- [ ] Repository secrets ayarlanmış mı?
- [ ] Cron time UTC'de ayarlanmış mı?

**Bilgi:** GitHub Actions'taki cron zamanlaması her zaman UTC'dir!

**Çözüm Adımları:**
1. Settings → Actions sekmesine git
2. "Enable Actions" butonuna tıkla
3. Secrets doğru ayarlanmış mı kontrol et
4. Manual test: Actions tab → "Daily British Library Image" → "Run workflow"

---

### "Workflow başladı ama başarısız oldu"

**Log'u kontrol et:**
1. Actions tab → "Daily British Library Image" → Son run
2. "fetch-and-analyze" job'ını aç
3. "Fetch and analyze image" step'ini kontrol et
4. Hata mesajını ara

**Yaygın Hatalar:**

#### ❌ "401 Unauthorized"
```
Error: API returned 401 - Invalid API key
```
**Çözüm:** Flickr API key'i yenile ve GitHub Secrets'te güncelle

#### ❌ "429 Too Many Requests"
```
Error: Rate limit exceeded
```
**Çözüm:** 1 saat bekle, API otomatik olarak sıfırlanır

#### ❌ "504 Gateway Timeout (LLaVA)"
```
Error: Hugging Face API timeout
```
**Çözüm:** 
- 5 dakika bekle
- Manual trigger: Actions → "Run workflow"
- Hala başarısızsa, HF sistem durumunu kontrol et: https://status.huggingface.co

#### ❌ "Network connection failed"
```
Error: HTTPConnectionError
```
**Çözüm:**
- GitHub Actions'ın internet bağlantısı kesik olabilir
- Manuel tetikle ve hemen sonra kontrol et
- Sorun devam ederse, workflow'u yeniden çalıştır

---

## Website Sorunları

### "Website'de görüntü gösterilmiyor"

**Kontrol Listesi:**
- [ ] `public/data/daily-image.json` dosyası var mı?
- [ ] JSON format geçerli mi? (https://jsonlint.com ile kontrol et)
- [ ] `public/images/daily-*.jpg` dosyası indirildi mi?
- [ ] Netlify build başarılı mı?

**Çözüm:**

**1. JSON dosyası kontrol:**
```bash
# JSON valid mi test et
python -m json.tool public/data/daily-image.json
```

**2. Netlify logs kontrol:**
- Netlify dashboard → Deploys → Latest deploy
- Build logs'u aç ve hata ara

**3. Browser console kontrol:**
- Website'de F12 (DevTools) aç
- Console tab'ını kontrol et
- CORS veya fetch hataları var mı?

**4. Local test:**
```bash
# Simple HTTP server çalıştır
python -m http.server 8000
# http://localhost:8000/public/ ziyaret et
```

---

### "Netlify'da "Build failed" gösteriliyor"

**Sebepleri:**
- Deploy command hatalı
- Publish directory yanlış
- File permissions sorunu

**Çözüm:**
1. Netlify dashboard → Deploys → Failed deploy
2. Deploy log'u aç
3. Hata mesajını bul
4. Netlify.toml kontrol et:
```toml
[build]
command = "echo 'Static site'"
publish = "public"
```

---

## Veri Sorunları

### "archive.json çok büyük hale geldi"

**Sebep:** Her gün yeni görüntü ekleniyor, 30 günden fazla tutuluyor

**Çözüm:** fetch_image.py'deki arşiv sınırını kontrol et
```python
archive = archive[:30]  # Son 30 günü tut
```

**Manuel temizlik:**
```bash
# archive.json'ı temizle (en son 10 gün tut)
python -c "
import json
with open('public/data/archive.json') as f:
    data = json.load(f)
with open('public/data/archive.json', 'w') as f:
    json.dump(data[:10], f, indent=2)
"
```

---

### "Görüntü kalitesi düşük"

**Sebep:** Flickr'da düşük kalite versiyon kullanılıyor

**Çözüm:** fetch_image.py'da URL önceliğini değiştir
```python
# Mevcut (3. en iyi kalite)
image_url = photo.get('url_o') or photo.get('url_l')

# Tüm seçenekler (kalite sırasına göre):
# url_o = Original (en iyi)
# url_l = Large (2.)
# url_m = Medium (3.)
# url_s = Small (en kötü)
```

---

## Performance Sorunları

### "GitHub Actions 5 dakikadan fazla sürüyor"

**Olası Nedenler:**
- LLaVA API yavaş yanıt veriyor
- Flickr API rate limit'e yakın
- Network gecikmeleri

**Çözüm:**
- Timeout'u artır: fetch_image.py timeout parametresi
- LLaVA daha hafif model kullan
- Parallelization ekle

```python
# Timeout'u 60 saniyeye çıkar
response = requests.post(
    LLAVA_API_URL, 
    headers=headers, 
    json=payload,
    timeout=60  # 30 saniyeden 60 saniyeye
)
```

---

### "Netlify deploy çok yavaş"

**Çözümler:**
1. Büyük image dosyalarını optimize et:
```bash
pip install pillow-simd
# fetch_image.py'da image compression ekle
```

2. CDN cache'lemeyi aktifleştir (Netlify otomatik yapar)

3. Images klasörü boyutunu sınırla:
```bash
# 30 gün = ~30 image, ~100-200MB toplam
# Bu kabul edilebilir sınırlar içinde
```

---

## Debug Mode

### Verbose Logging Aktifleştir

**fetch_image.py'da ekle:**
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Adımlar:
logger.debug(f"Fetching from Flickr...")
logger.debug(f"Got {len(photos)} photos")
logger.debug(f"Analyzing with LLaVA...")
```

### Manual Test (Local)

```bash
# .env dosyasını ayarla
cp .env.example .env
# API key'leri .env'ye ekle

# Python script'i doğrudan çalıştır
python scripts/fetch_image.py

# Çıktı:
# 🔍 Fetching random image from British Library...
# 📸 Found: [image title]
# 🤖 Analyzing with LLaVA AI...
# ✨ Analysis complete!
# 💾 Saving data...
# 🎉 Done!
```

---

## Emergency Procedures

### "Tüm sistem çöktü, en son çalışan versiyona dön"

```bash
# Git history'yi kontrol et
git log --oneline

# Çalışan commite dön
git checkout <commit-hash>

# Veya son başarılı version'a geri git
git revert HEAD
```

### "API key'i yanlışlıkla expose ettim"

**HEMEN YAP:**
1. Flickr API key'ini yenile: https://www.flickr.com/services/apps/
2. HF token'ı revoke et: https://huggingface.co/settings/tokens
3. Yeni key'leri GitHub Secrets'te güncelle
4. Git history'den expose olan key'i temizle:
```bash
# Tüm history'den sil
git filter-branch --force --index-filter \
  "git rm -r --cached --ignore-unmatch [exposed key]" \
  --prune-empty --tag-name-filter cat -- --all

git push --force
```

---

## Support & Resources

| Kaynak | Link |
|--------|------|
| Flickr API Docs | https://www.flickr.com/services/api/ |
| Hugging Face Docs | https://huggingface.co/docs |
| GitHub Actions | https://docs.github.com/en/actions |
| Netlify Docs | https://docs.netlify.com |
| Python Requests | https://requests.readthedocs.io |

