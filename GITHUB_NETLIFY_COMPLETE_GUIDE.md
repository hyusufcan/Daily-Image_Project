# 📝 Step-by-Step: GitHub + Netlify Setup

## ⏱️ Toplam Zaman: ~30 dakika

---

## 1️⃣ GITHUB REPOSITORY OLUŞTUR (5 dakika)

### Adım 1: GitHub'a Git

1. https://github.com/new ziyaret et
2. **Repository name:** `Daily-Image-Project`
3. **Description:** `Victorian-themed daily showcase of historical images from British Library`
4. **Visibility:** Public (Netlify'ın erişmesi için)
5. **.gitignore:** Python seç
6. **License:** MIT (opsiyonel)
7. **"Create repository"** tıkla

### Adım 2: Repository Linki Al

Oluşturulduktan sonra şunu göreceksin:
```
https://github.com/YOUR_USERNAME/Daily-Image-Project
```

Bu link'i kopyala - sonra kullanacağız.

---

## 2️⃣ GIT'I CONFIGURE ET (5 dakika)

### Terminal'de:

```powershell
# Git konfigürasyonu (ilk defa)
git config --global user.email "your.email@gmail.com"
git config --global user.name "Your Full Name"

# Proje klasörüne git
cd c:\Users\ASUS\Downloads\Daily_Image_Project

# Repository'i initialize et
git init

# GitHub'u remote olarak ekle (linkini yapıştır)
git remote add origin https://github.com/YOUR_USERNAME/Daily-Image-Project.git

# Branch ismini "main" yap
git branch -M main

# Doğruluğunu kontrol et
git remote -v
```

**Çıktı:**
```
origin  https://github.com/YOUR_USERNAME/Daily-Image-Project.git (fetch)
origin  https://github.com/YOUR_USERNAME/Daily-Image-Project.git (push)
```

---

## 3️⃣ TÜᲛ DOSYALARI PUSH ET (5 dakika)

### Terminal'de:

```powershell
# Tüm dosyaları stage et
git add .

# Kontrol et (neyi ekleyecek?)
git status

# Commit et
git commit -m "Initial commit: Complete documentation and local dev environment"

# GitHub'a push et
git push -u origin main
```

**Beklenen Çıktı:**
```
Enumerating objects: ...
Counting objects: ...
Delta compression using ...
Writing objects: 100% (...)
...
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### GitHub'da Kontrol Et

1. https://github.com/YOUR_USERNAME/Daily-Image-Project ziyaret et
2. Tüm dosyalar görünüyor mu?
3. `public/`, `docs/`, `tests/`, `scripts/` klasörleri var mı?

---

## 4️⃣ NETLIFY'A BAĞLAN (10 dakika)

### Seçenek A: Web GUI (Önerilen - Kolay)

#### 1. Netlify'a Git ve Sign Up Yap

- https://app.netlify.com ziyaret et
- **"Sign up"** tıkla
- **"GitHub with GitHub"** seç
- GitHub'a yönlendir ve authorize et

#### 2. Site Oluştur

- **"Add new site"** → **"Import an existing project"**
- **GitHub** seç
- Repo'nu seç: **Daily-Image-Project**
- Build settings:
  ```
  Branch to deploy: main
  Build command: echo 'Static site'
  Publish directory: public
  ```
- **"Deploy site"** tıkla

#### 3. Deployment'ı Bekle

Netlify otomatik build edecek. Bitmesini bekle (~2 dakika).

**Site URL'si:**
```
https://YOUR-RANDOM-NAME.netlify.app
```

Bu URL'i tarayıcıda aç - website açılmalı! 🎉

---

### Seçenek B: CLI (Terminal)

```powershell
# 1. Netlify CLI yükle
npm install -g netlify-cli

# 2. Netlify'a giriş yap
netlify login
# → Browser açılır ve GitHub ile authorize etmen istenir

# 3. Project'i initialize et
netlify init
# → Sorular soracak:
#   - What is the publish directory? → public
#   - Configure a build command? → No

# 4. Production'a deploy et
netlify deploy --prod
```

---

## 5️⃣ API KEYS CONFIGURE ET (5 dakika)

### GitHub Secrets'e Ekle

1. GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. **"New repository secret"** → Ekle:

   **Secret 1:**
   - Name: `FLICKR_API_KEY`
   - Value: [Flickr API key'ini yapıştır]
   - Add secret

   **Secret 2:**
   - Name: `HF_API_KEY`
   - Value: [Hugging Face token'ı yapıştır]
   - Add secret

### Netlify Environment Variables'a Ekle (Opsiyonel)

1. Netlify site → **Settings** → **Build & deploy** → **Environment**
2. **"Edit variables"** tıkla
3. Ekle:
   - `FLICKR_API_KEY` = [key]
   - `HF_API_KEY` = [token]

---

## ✅ TEST ET

### 1. Website Açılıyor mu?

```
https://YOUR-SITE.netlify.app
```

**Görmen gerekeni:**
- ✅ Victorian UI
- ✅ Crystal Palace fotoğrafı (mock veri)
- ✅ AI analiz metni
- ✅ Layout responsive

### 2. GitHub Workflow Çalışıyor mu?

1. GitHub repo → **Actions** tab
2. **"Daily British Library Image"** workflow
3. **"Run workflow"** → **"Run workflow"**
4. 2-5 dakika bekle
5. ✅ olmuş mu kontrol et

---

## 🔗 BAĞLANTILARIN ÇALIŞTIĞINI DOĞRULA

### Flickr Linki Test Et

1. Website'de **"View Original Source"** düğmesine tıkla
2. Flickr'a yönlendirildin mi?

### JSON Verisi Kontrol Et

```
https://YOUR-SITE.netlify.app/data/daily-image.json
```

Tarayıcıda açtığında JSON görebilmen gerekir.

---

## 🚨 YAYGGIN SORUNLAR

### "Build failed" hatası

```
→ Netlify Dashboard → Deploys → kırmızı deploy
→ Click → "View deploy log"
→ Hata mesajını oku

Genellikle:
- publish directory yanlış
- build command hata veriyor
```

### "Site not found (404)"

```
→ DNS propagation bekleniyor (24 saat)
→ Netlify'ın assigned URL'sini kullan: *.netlify.app
```

### "GitHub Actions workflow başlamıyor"

```
→ Settings → Actions → General
→ "Workflow permissions" → "Read and write permissions"
→ Workflow'u manual trigger et
```

### "API keys not working"

```
→ GitHub Secrets doğru set mi?
→ Secret name: FLICKR_API_KEY (typo kontrol et)
→ Value boş mu?
→ Workflow trigger'ı new push ile yapılmış mı?
```

---

## 📊 NETLIFY SETUP CHECKLIST

- [ ] GitHub repo oluşturuldu
- [ ] Git configure edildi
- [ ] Tüm dosyalar push edildi
- [ ] Netlify'a bağlandı
- [ ] Build başarılı
- [ ] Site URL'si aldı
- [ ] Website açılıyor
- [ ] Mock veri gösteriliyor
- [ ] Flickr linki çalışıyor
- [ ] GitHub Secrets eklendi
- [ ] Workflow test edildi
- [ ] Environment variables set

---

## 🎯 ÖNEMLİ NOTLAR

### Önemli: Branch Protection

Workflow'un başarılı çalışması için:

```
Settings → Branches → Add rule
Branch name pattern: main
✅ Require status checks to pass before merging
✅ Select status checks: (GitHub Actions)
```

### Önemli: Commits

Workflow automatic commit yapar. Infinite loop'u önlemek için:

```yaml
if: github.actor != 'github-actions'
```

---

## ✨ TAMAMLANDIKTAN SONRA

1. **Site live:** https://YOUR-SITE.netlify.app
2. **Workflow active:** Her gün 09:00 UTC
3. **Data updates:** `public/data/daily-image.json`
4. **Archive:** `public/data/archive.json`

---

## 📞 SONRAKI ADIMLAR

✅ Site kuruldu  
➡️ API bağlantılarını test et  
➡️ Custom domain ekle (opsiyonel)  
➡️ Monitoring setup yap  

---

**Bitirdin mi? Mubarek olsun! 🎉**

Şimdi API connections kısmına geçebiliriz!

