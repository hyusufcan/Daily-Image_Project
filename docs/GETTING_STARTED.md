# 🚀 Local Kurulum ve Test Rehberi

Lokal makinenizde The Daily Antiquarian projesini çalıştırmak için bu rehberi takip edin.

---

## 📋 Ön Gereksinimler

- ✅ Python 3.8+
- ✅ pip (Python paket yöneticisi)
- ✅ Bir web tarayıcı (Chrome, Firefox, Edge, vb.)
- ✅ Git (isteğe bağlı)

---

## 🎯 Hızlı Başlangıç (5 dakika)

### 1. Proje Klasörüne Git

```powershell
cd c:\Users\ASUS\Downloads\Daily_Image_Project
```

### 2. Bağımlılıkları Yükle

```powershell
pip install -r requirements.txt
```

**Beklenen çıktı:**
```
Successfully installed requests-2.x.x pillow-9.x.x python-dotenv-0.20.0
```

### 3. Development Server'ı Başlat

#### **Seçenek A: Basit HTTP Server (Önerilen)**

```powershell
python -m http.server 8000 --directory public
```

**Tarayıcıda aç:** http://localhost:8000/

#### **Seçenek B: Flask Development Server**

```powershell
pip install flask
python dev_server.py
```

**Tarayıcıda aç:** http://localhost:5000/

**Dev Dashboard:** http://localhost:5000/dev

---

## 🌐 Website'i Görüntüle

Tarayıcıda aşağıdaki URL'yi ziyaret edin:

```
http://localhost:8000/
```

Hemen **bugünün seçilen görüntüsünü** mock test verisiyle göreceksiniz! 🎉

---

## 📁 Dosya Yapısı

```
Daily_Image_Project/
│
├── 📄 README.md                    ← Ana proje tanıtımı
├── 📄 QUICKSTART.md                ← 5 dakikalık hızlı başlangıç
├── 📄 DOCUMENTATION_ANALYSIS.md    ← Detaylı dokümantasyon analizi
│
├── 📂 public/                       ← Website dosyaları
│   ├── index.html                  ← Ana sayfa (AÇMAK İSTEDİĞİNİZ)
│   ├── 📂 data/
│   │   ├── daily-image.json        ← Bugünün test verisi ✅
│   │   └── archive.json            ← Geçmiş 30 gün verisi ✅
│   └── 📂 images/                  ← Placeholder görüntü klasörü
│
├── 📂 docs/                         ← Kapsamlı dokümantasyon
│   ├── API.md                       ← API referansı
│   ├── TROUBLESHOOTING.md           ← Sorun giderme kılavuzu
│   ├── CUSTOMIZATION.md             ← Özelleştirme rehberi
│   └── LOCAL_SETUP.md               ← Bu dokümantasyon
│
├── 📂 tests/                        ← Unit testler
│   └── test_fetch_image.py          ← Test örnekleri
│
├── 📂 scripts/                      ← Python scriptleri
│   └── fetch_image.py               ← Ana script (GitHub Actions'ta çalışır)
│
├── 📂 .github/workflows/            ← GitHub Actions
│   └── daily-image.yml              ← Workflow tanımı
│
├── 📄 requirements.txt              ← Python bağımlılıkları ✅
├── 📄 .env.example                  ← API key şablonu ✅
├── 📄 dev_server.py                 ← Flask dev server ✅
├── 📄 netlify.toml                  ← Netlify konfigürasyonu
└── 📄 daily-image.yml               ← GitHub Actions (eski lokasyon)
```

---

## 🧪 Test Senariyoları

### Senaryo 1: Ana Sayfayı Test Et

1. **http://localhost:8000/** ziyaret et
2. Görüntü ve analiz yüklendiğini kontrol et
3. "View Original Source" düğmesine tıkla

**Beklenen Sonuç:** ✅ Flickr linkine yönlendir

---

### Senaryo 2: JSON Veri Doğrulama

```powershell
# Terminal'de:
python -m json.tool public/data/daily-image.json
```

**Beklenen Sonuç:** ✅ Formatted JSON output (hata yok)

---

### Senaryo 3: API Uçlarını Test Et (Flask kullanıyorsanız)

```powershell
# Terminal 1:
python dev_server.py

# Terminal 2:
# Browser'da aç: http://localhost:5000/dev
```

**Beklenen Sonuç:** ✅ Dev Dashboard açılır

---

## 🔧 Python Virtual Environment Kurulumu (İsteğe Bağlı)

Sistem genelini etkilemeden izole ortamda çalışmak için:

```powershell
# Virtual environment oluştur
python -m venv venv

# Aktifleştir (PowerShell)
.\venv\Scripts\Activate.ps1

# veya Command Prompt için:
venv\Scripts\activate.bat

# Bağımlılıkları yükle
pip install -r requirements.txt

# Deaktifleştir (bittiğinde)
deactivate
```

---

## 🔌 API Key'lerini Ayarla (Production için)

Local test için gerekli **değildir**, ancak production için:

### Adım 1: .env Dosyası Oluştur

```powershell
copy .env.example .env
```

### Adım 2: .env Dosyasını Düzenle

Notepad'de `C:\Users\ASUS\Downloads\Daily_Image_Project\.env` açın:

```env
FLICKR_API_KEY=your_actual_api_key_here
HF_API_KEY=your_actual_token_here
```

### Adım 3: Script'i Çalıştır

```powershell
python scripts/fetch_image.py
```

---

## 📊 Development Dashboard (Flask)

Flask server'da gelişmiş geliştirme araçları mevcuttur:

```
http://localhost:5000/dev
```

Burada:
- ✅ API uçlarını test et
- ✅ Status kontrolü yap
- ✅ Mock API çağrıları gör
- ✅ Dosya yapısını görüntüle

---

## 🐛 Sorun Giderme

### "ModuleNotFoundError: No module named 'requests'"

```powershell
pip install -r requirements.txt
```

### "Port 8000 zaten kullanımda"

```powershell
# Başka port kullan
python -m http.server 8080 --directory public

# Tarayıcıda: http://localhost:8080/
```

### "Permission denied" (PowerShell)

```powershell
# PowerShell politikasını değiştir
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Website yüklenmiyor / hata gösteriyor

1. **F12 (DevTools)** aç
2. **Console** tab'ını kontrol et
3. **Network** tab'ında HTTP status'u kontrol et
4. `public/data/daily-image.json` dosyası var mı kontrol et

---

## 📝 Logları Kontrol Et

### Python Debug Modu

```powershell
# Flask'ta:
python dev_server.py

# Çıktı:
# DEBUG: ...
# WARNING: ...
```

### Browser Console

1. Website'de **F12** aç
2. **Console** tab'ı
3. Hataları oku

---

## ✅ Başarılı Kurulum Kontrol Listesi

- [ ] Python 3.8+ yüklü mü? (`python --version`)
- [ ] Bağımlılıklar yüklü mü? (`pip list | grep requests`)
- [ ] Server başlıyor mı? (`python -m http.server 8000`)
- [ ] Website açılıyor mı? (`http://localhost:8000/`)
- [ ] Görüntü gösterilüyor mu?
- [ ] JSON veri geçerli mi? (`python -m json.tool public/data/daily-image.json`)
- [ ] "View Original Source" linki çalışıyor mı?

---

## 🎯 Sonraki Adımlar

### Kendi Veri ile Test Etmek

1. `public/data/daily-image.json` düzenle
2. Yeni veri ekle
3. **F5** ile tarayıcıyı yenile
4. Website otomatik güncellenir

### API Key'ler ile Production Setup

Bkz: `docs/DEPLOYMENT.md`

### Özelleştirme

Bkz: `docs/CUSTOMIZATION.md`

### Sorun Giderme

Bkz: `docs/TROUBLESHOOTING.md`

---

## 🆘 Yardım Al

| Konu | Dosya |
|------|-------|
| Kurulum | Bu dosya (LOCAL_SETUP.md) |
| API Detayları | `docs/API.md` |
| Sorun Giderme | `docs/TROUBLESHOOTING.md` |
| Özelleştirme | `docs/CUSTOMIZATION.md` |
| Deployment | `docs/DEPLOYMENT.md` |

---

## 🎉 Tamamlandı!

Website'iniz **http://localhost:8000/** adresinde çalışıyor!

Mock test verisiyle tüm özellikleri görebilirsiniz. Production ortamına hazırlandığında:

1. API key'leri ekle → GitHub Secrets
2. Repository'yi fork et
3. Netlify'a bağla
4. GitHub Actions otomatik başlasın

---

**Sorularınız mı var?** → `docs/TROUBLESHOOTING.md` kontrol edin

**Mutlu kodlamalar!** 🏛️✨

