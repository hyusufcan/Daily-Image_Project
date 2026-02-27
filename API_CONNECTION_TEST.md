# 🔌 API CONNECTION TEST REHBERI

## Adım 1: API Keys'i Al

### Flickr API Key

1. https://www.flickr.com/services/apps/create/ ziyaret et
2. **"Create a Non-Commercial Application"** seç
3. Bilgileri doldur:
   - **App name:** "Daily Antiquarian" (veya başka isim)
   - **Description:** "Personal project - historical image collection"
4. **"Create application"** tıkla
5. **API Key** kopyala (uzun string)

### Hugging Face Token

1. https://huggingface.co/join (veya giriş yap)
2. Settings → **Access Tokens** → **New token**
3. Token name: "Daily Antiquarian"
4. Permission: **Read**
5. **Generate token** → Token'ı kopyala

---

## Adım 2: Local'de Test Et

### .env Dosyası Oluştur

```powershell
cd c:\Users\ASUS\Downloads\Daily_Image_Project

# .env.example'den kopyala
copy .env.example .env
```

### .env Dosyasını Düzenle

Notepad'de `.env` aç ve ekle:

```env
FLICKR_API_KEY=YOUR_FLICKR_API_KEY_HERE
HF_API_KEY=YOUR_HUGGING_FACE_TOKEN_HERE
```

### Script'i Test Et

```powershell
# Bağımlılıkları yükle
pip install -r requirements.txt

# Script'i çalıştır
python scripts/fetch_image.py
```

**Beklenen çıktı:**
```
🔍 Fetching random image from British Library...
📸 Found: [Image Title]
🤖 Analyzing with LLaVA AI...
✨ Analysis complete!
💾 Saving data...
✅ Daily image saved: [Title]
🎉 Done!
```

---

## Adım 3: Sonuçları Kontrol Et

### JSON Oluşturuldu mu?

```powershell
python -m json.tool public/data/daily-image.json
```

**Görmek gerekeni:**
```json
{
  "date": "2026-02-27",
  "photo": {
    "id": "...",
    "title": "...",
    "description": "...",
    ...
  },
  "ai_analysis": {
    "analysis": "AI tarafından yazılmış metni...",
    "model": "llava-1.5-7b-hf",
    "analyzed_at": "2026-02-27T..."
  }
}
```

### Görüntü İndirildi mi?

```powershell
ls public/images/

# Output:
# daily-2026-02-27.jpg (veya günün tarihi)
```

### Website Güncellenmiş mi?

```
http://localhost:8000/
```

Tarayıcıda açtığında:
- ✅ Yeni görüntü gösterilmesi gerekir
- ✅ Yeni analiz metni
- ✅ Günün tarihi

---

## Adım 4: GitHub Actions Test

### GitHub'a Push Et

```powershell
git add .
git commit -m "API keys configured and tested"
git push origin main
```

### Manual Workflow Trigger

1. GitHub repo → **Actions**
2. **"Daily British Library Image"** workflow
3. **"Run workflow"** → **"Run workflow"**
4. ⏳ 2-5 dakika bekle

### Logs Kontrol Et

1. Workflow başladığında → Click
2. **"fetch-and-analyze"** job → Click
3. **"Fetch and analyze image"** step
4. ✅ başarılı oldu mu, ❌ başarısız mı?

**Başarılı çıktı:**
```
✅ Daily image saved: [Title]
```

**Hatalı çıktı:**
```
❌ Error: [error message]
API error, network error, vs.
```

---

## Adım 5: GitHub Repository Güncellemesi

### Otomatik Commit Kontrolü

Workflow başarılı oldu mu?
- ✅ Evet: `public/data/daily-image.json` güncellenmiş olmalı
- ❌ Hayır: Logs kontrol et

### Website Güncellenmesi (Netlify)

1. GitHub push → automatic Netlify rebuild
2. Netlify dashboard → Deploys
3. Son deploy "Published" mi?
4. Website'e git: https://YOUR-SITE.netlify.app
5. Yeni veri gösteriliyor mu?

---

## 🧪 API TEST KOMUTLARI

### Flickr API'yi Direkt Test Et

```powershell
$flickrKey = "YOUR_KEY"
$userId = "12403504@N02"

Invoke-WebRequest -Uri "https://api.flickr.com/services/rest/?method=flickr.people.getPublicPhotos&api_key=$flickrKey&user_id=$userId&per_page=10&format=json&nojsoncallback=1" | ConvertFrom-Json | Select-Object -ExpandProperty photos | Select-Object -ExpandProperty photo | Select-Object id, title | Format-Table
```

**Görmek gerekeni:**
```
id          title
--          -----
123456      Historical Image Title 1
234567      Historical Image Title 2
...
```

### LLaVA API'yi Test Et

```powershell
$headers = @{"Authorization" = "Bearer YOUR_HF_TOKEN"}
$body = @{
    inputs = @{
        image = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Crystal_Palace_in_the_Great_Exhibition_of_1851.jpg/1280px-Crystal_Palace_in_the_Great_Exhibition_of_1851.jpg"
        text = "Describe this image briefly"
    }
} | ConvertTo-Json

Invoke-WebRequest -Method Post -Uri "https://api-inference.huggingface.co/models/llava-hf/llava-1.5-7b-hf" -Headers $headers -Body $body -ContentType "application/json" | ConvertFrom-Json
```

**Başarılı çıktı:**
```
generated_text: "The image shows... [AI analysis]"
```

---

## ✅ API CONNECTION CHECKLIST

### Flickr
- [ ] API key aldı
- [ ] Key geçerli (test script çalıştı)
- [ ] British Library photos çekilebiliyor
- [ ] Random selection çalışıyor
- [ ] Image URL'si geçerli

### Hugging Face
- [ ] Token aldı
- [ ] Token geçerli (test et)
- [ ] LLaVA model accessible
- [ ] Analysis metni üretiliyor
- [ ] JSON'da kaydediliyor

### GitHub Actions
- [ ] Workflow scheduled (09:00 UTC)
- [ ] Manual trigger çalışıyor
- [ ] Environment secrets set
- [ ] Logs hiçbir hata göstermiyor
- [ ] Data commits otomatik oluyor

### Netlify
- [ ] Site deployed
- [ ] Data güncellenmiş
- [ ] Website yeni veriyi gösteriyor
- [ ] Archive güncelleniyor
- [ ] JSON accessible (public URL)

---

## 🚨 SORUN GİDERME

### "Flickr API 401 Unauthorized"

```
Sebep: API key hatalı veya süresi dolmuş

Çözüm:
1. Flickr apps page'ine git
2. Yeni key generate et
3. GitHub Secrets güncelle
4. Workflow'u tekrar trigger et
```

### "HF API 429 Too Many Requests"

```
Sebep: Rate limit aşıldı (100 req/min)

Çözüm:
1. 1 dakika bekle
2. Manual retry et
3. Workflow schedule'ı azalt (6 saatte bir vb.)
```

### "HF API 504 Gateway Timeout"

```
Sebep: LLaVA modeli overload, timeout

Çözüm:
1. 5 dakika bekle
2. Tekrar trigger et
3. Daha hafif model kullan: llama-2-7b (opsiyonel)
```

### "JSON geçersiz, website açılmıyor"

```
Sebep: Script error, incomplete data save

Çözüm:
1. Script logs kontrol et
2. Error message'ı oku
3. Manual script run: python scripts/fetch_image.py
4. Logs'u kontrol et
```

### "Website eski veriyi gösteriyor"

```
Sebep: Browser cache, Netlify cache

Çözüm:
1. Browser: CTRL+Shift+Delete (cache clear)
2. Netlify: Settings → Deploys → "Clear cache and redeploy"
3. 2 dakika bekle
4. Yenile: CTRL+F5
```

---

## 📊 MONITORING

### Daily Check

```powershell
# JSON'ın güncel olup olmadığını kontrol et
$json = curl.exe -s https://YOUR-SITE.netlify.app/data/daily-image.json | ConvertFrom-Json
$json.date  # Bugünün tarihi mi?
$json.photo.title  # Resim başlığı var mı?
```

### Weekly Check

1. GitHub Actions → History → başarısız runs var mı?
2. Netlify → Deploys → failed deploys?
3. Website → New image gösteriliyor mu?

### Monthly Check

1. Archive.json 30 gün veri tutuyor mu?
2. Disk usage reasonable?
3. Performance metrics iyi mi?

---

## 🎯 BAŞARILI GÖSTERGELERI

✅ Flickr API çalışıyor  
✅ LLaVA AI analiz yapıyor  
✅ JSON dosyaları oluşturuluyor  
✅ GitHub Actions otomatik çalışıyor  
✅ Website güncellenmiş veri gösteriyor  
✅ Archive build up oluyor  
✅ No errors in logs  

**İf all green → System fully operational!** 🎉

---

## 📞 HAVARINT KAYNAKLAR

- `docs/TROUBLESHOOTING.md` - Sorun giderme
- `docs/API.md` - API detayları
- `.github/workflows/daily-image.yml` - Workflow config
- `scripts/fetch_image.py` - Main script

---

**API bağlantıları başarılı mı? Başarılıysa tamamlandık!** 🏛️✨

