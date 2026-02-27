# 🚀 Netlify Deployment Rehberi

## Adım 1: GitHub'a Push Et

```powershell
# Proje klasörüne git
cd c:\Users\ASUS\Downloads\Daily_Image_Project

# Git'i konfigure et (ilk defa)
git config --global user.email "your.email@gmail.com"
git config --global user.name "Your Name"

# Repository'i initialize et (eğer git kullanmıyorsan)
git init

# Tüm dosyaları stage et
git add .

# Commit et
git commit -m "Initial project setup with documentation and local dev environment"

# GitHub'a push et (repo oluştur ve linki buraya yapıştır)
git remote add origin https://github.com/YOUR_USERNAME/Daily-Image-Project.git
git branch -M main
git push -u origin main
```

---

## Adım 2: Netlify'a Bağlan

### Seçenek A: Web'de (En Kolay)

1. **https://app.netlify.com** ziyaret et
2. **"Sign up"** (GitHub ile bağlan)
3. Authorize Netlify for GitHub
4. **"Add new site"** → **"Import an existing project"**
5. **GitHub** seç
6. **Daily-Image-Project** repo'sunu seç
7. Build settings:
   - Build command: `echo 'Static site'` (veya boş bırak)
   - Publish directory: `public`
8. **"Deploy site"** tıkla

### Seçenek B: CLI (Terminal)

```powershell
# Netlify CLI yükle
npm install -g netlify-cli

# Netlify'a giriş yap
netlify login

# Project'i initialize et
netlify init

# Production'a deploy et
netlify deploy --prod
```

---

## Adım 3: Environment Variables (API Keys) Ekle

### Netlify Dashboard'da:

1. Site → **Settings** → **Build & deploy** → **Environment**
2. **"Edit variables"** tıkla
3. Ekle:
   ```
   FLICKR_API_KEY = your_actual_flickr_key
   HF_API_KEY = your_actual_hugging_face_token
   ```
4. **Save** tıkla

### Veya CLI ile:

```powershell
netlify env:set FLICKR_API_KEY "your_key_here"
netlify env:set HF_API_KEY "your_token_here"
```

---

## Adım 4: Site URL'si Al

Deployment tamamlandıktan sonra:

```
Site URL: https://YOUR-SITE-NAME.netlify.app
```

Bu link'i kopyala ve tarayıcıda aç!

---

## Adım 5: GitHub Actions Workflow Setup

### 1. GitHub Secrets Ekle

1. GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. **"New repository secret"** tıkla
3. Ekle:
   - Name: `FLICKR_API_KEY` → Value: [Flickr API Key]
   - Name: `HF_API_KEY` → Value: [HF Token]

### 2. Workflow Dosyasını Kontrol Et

Dosya: `.github/workflows/daily-image.yml`

```yaml
name: Daily British Library Image

on:
  schedule:
    - cron: '0 9 * * *'  # Her gün 09:00 UTC
  workflow_dispatch:

jobs:
  fetch-and-analyze:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install requests pillow
      
      - name: Fetch and analyze image
        env:
          FLICKR_API_KEY: ${{ secrets.FLICKR_API_KEY }}
          HF_API_KEY: ${{ secrets.HF_API_KEY }}
        run: python scripts/fetch_image.py
      
      - name: Commit and push
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add data/daily-image.json public/images/ public/data/
          git diff --quiet && git diff --staged --quiet || \
            (git commit -m "Daily image: $(date +'%Y-%m-%d')" && git push)
```

### 3. Workflow'u Test Et

1. GitHub → **Actions** tab
2. **"Daily British Library Image"** workflow'u seç
3. **"Run workflow"** → **"Run workflow"**
4. Çalışıyor mu kontrol et

---

## ✅ Kontrol Listesi

- [ ] Repository GitHub'a push edildi
- [ ] Netlify'a bağlandı
- [ ] Build başarılı
- [ ] Site URL'si alındı
- [ ] Environment variables (API keys) eklendi
- [ ] GitHub Secrets configured
- [ ] Workflow test edildi
- [ ] Website açılıyor
- [ ] Mock data gösteriliyor

---

## 🔧 Troubleshooting

### "Build failed" hatası

```
→ Netlify dashboard → Deploys → Failed deploy log'u aç
→ Hata mesajını oku
→ Genellikle build command veya publish directory yanlış
```

### "Site not found" (DNS)

```
→ DNS propagation 24 saat sürebilir
→ Netlify assigned URL kullan: https://YOUR-RANDOM-ID.netlify.app
```

### "API keys not working"

```
→ GitHub Secrets ayarlanmış mı kontrol et
→ Netlify Environment variables set mi
→ Key'ler geçerli mi test et
→ Logs kontrol et
```

---

## 🎯 Sonraki Adımlar

1. **Site erişilebildi mi?**
   - Evet → Adım 2'ye git
   - Hayır → Troubleshooting kontrol et

2. **API keys working mi?**
   - Evet → Manual workflow trigger et
   - Hayır → Adım 3'ü tekrar yap

3. **Workflow çalışıyor mu?**
   - Evet → Tamamlandı! 🎉
   - Hayır → Logs kontrol et

---

## 📞 Yardım

- Setup sorunları: `docs/TROUBLESHOOTING.md`
- API detayları: `docs/API.md`
- GitHub Actions: `.github/workflows/daily-image.yml`
- Deployment: `docs/DEPLOYMENT.md`

---

**Site kurulumu tamamlandıktan sonra API bağlantılarını test edebiliriz!**

