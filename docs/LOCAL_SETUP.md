# Local Development Server

Lokal geliştirme ve test için bu rehberi kullanın.

## Hızlı Başlangıç

### 1. Bağımlılıkları Yükle

```bash
cd c:\Users\ASUS\Downloads\Daily_Image_Project
pip install -r requirements.txt
```

### 2. Development Server Başlat

```bash
python -m http.server 8000
```

### 3. Tarayıcıda Aç

```
http://localhost:8000/public/
```

---

## Advanced Setup

### Python Virtual Environment (Recommended)

```bash
# Virtual environment oluştur
python -m venv venv

# Aktifleştir
venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### Flask Development Server (Advanced)

Dinamik test verisi sunmak için:

```bash
pip install flask
python dev_server.py
```

Ardından: `http://localhost:5000`

---

## Test Verisi

Mock görüntü ve JSON verisi `public/` klasöründe hazırlanmıştır:

- **JSON:** `public/data/daily-image.json` ✅
- **Görüntü:** Placeholder (local test için)

### Manual Test

```bash
# JSON validate
python -m json.tool public/data/daily-image.json

# HTML validate
# Tarayıcı Devtools → Console kontrolü
```

---

## Dosya Yapısı

```
Daily_Image_Project/
├── public/
│   ├── index.html              ← Ana website
│   ├── data/
│   │   └── daily-image.json    ← Mock test verisi ✅
│   └── images/                 ← Placeholder (test için)
├── requirements.txt            ← Bağımlılıklar ✅
├── .env.example               ← API key template ✅
└── docs/                       ← Tüm dokümantasyon ✅
```

---

## İlk İzlenim Linki

### Localhost'ta Canlı Önizleme:

**Start Command:**
```bash
python -m http.server 8000
```

**URL:** `http://localhost:8000/public/`

---

## Sorun Giderme

### "404 Not Found"
→ Doğru klasöre değilsin  
→ `cd public` sonra sunucuyu başlat

### "Port 8000 zaten kullanımda"
→ Başka port kullan: `python -m http.server 8080`

### "CORS hatası"
→ Yerel sunucudan dinamik veri yüklenemiyor  
→ public.http.server sorunları yok

---

**Hazır!** 🚀 Website artık localhost'ta çalışıyor.

