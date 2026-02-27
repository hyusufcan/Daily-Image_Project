╔════════════════════════════════════════════════════════════════╗
║         🚀 NETLIFY + API SETUP - COMPLETE GUIDE                ║
║                   Production Deploy Rehberi                     ║
╚════════════════════════════════════════════════════════════════╝

📋 İçindekiler
  1. GitHub Setup (5 min)
  2. Netlify Setup (10 min)
  3. API Configuration (5 min)
  4. Testing (10 min)
  5. Monitoring & Maintenance

═══════════════════════════════════════════════════════════════════

✅ QUICK SUMMARY

Adımlar:
  1. GitHub'a repository oluştur ve push et
  2. Netlify'a bağla
  3. API keys'i GitHub Secrets'e ekle
  4. Site canlı yayında
  5. API connections test et

Toplam Zaman: ~30 dakika

Sonuç: https://YOUR-SITE.netlify.app (canlı)

═══════════════════════════════════════════════════════════════════

📁 YENİ REHBERLER (OKU SIRASI)

1️⃣  GITHUB_NETLIFY_COMPLETE_GUIDE.md
    └─ Adım adım tüm setup
    └─ 30 dakika içinde tamamla

2️⃣  API_CONNECTION_TEST.md
    └─ API keys al
    └─ Local test yap
    └─ Production test et

3️⃣  NETLIFY_SETUP_GUIDE.md
    └─ Netlify troubleshooting
    └─ Advanced configuration

═══════════════════════════════════════════════════════════════════

🎯 İLK 30 DAKİKADA YAPILACakLAR

⏱️ 5 dakika:  GitHub Repository oluştur
⏱️ 5 dakika:  Git configure et & push
⏱️ 10 dakika: Netlify bağla & deploy
⏱️ 5 dakika:  API keys ekle
⏱️ 5 dakika:  Test et

SONUÇ: Site canlı! 🎉

═══════════════════════════════════════════════════════════════════

📋 PRODUCTION DEPLOYMENT CHECKLIST

GitHub Setup:
  [ ] Repository oluştur
  [ ] Git initialize et
  [ ] Tüm dosyaları push et
  [ ] Public visibility (Netlify erişim için)

Netlify Setup:
  [ ] GitHub ile authorize et
  [ ] Repository seç
  [ ] Build settings konfigure et
  [ ] Deploy başlat
  [ ] Site URL aldı

Environment Configuration:
  [ ] FLICKR_API_KEY - GitHub Secrets
  [ ] HF_API_KEY - GitHub Secrets
  [ ] (Optional) Netlify Environment variables

Testing:
  [ ] Website açılıyor (https://YOUR-SITE.netlify.app)
  [ ] Mock veri gösteriliyor
  [ ] Workflow manuel trigger et
  [ ] 5 dakika bekle
  [ ] Yeni veri işlendi mi?
  [ ] JSON accessible (https://YOUR-SITE/data/daily-image.json)

Verification:
  [ ] Logs hiçbir hata göstermiyor
  [ ] Data commit'i otomatik oldu
  [ ] Website yeni veriyi gösteriyor
  [ ] Archive build up oluyor

═══════════════════════════════════════════════════════════════════

🔗 ÖNEMLİ LİNKLER (Boş Bırakacak)

GitHub Repository:
  https://github.com/YOUR_USERNAME/Daily-Image-Project
  👉 Burada doldur: _________________________________

Netlify Site:
  https://YOUR-SITE-NAME.netlify.app
  👉 Burada doldur: _________________________________

API Keys Konumu:
  GitHub Secrets: /YOUR_USERNAME/Daily-Image-Project/settings/secrets/actions
  👉 Link: _________________________________

GitHub Actions Workflow:
  https://github.com/YOUR_USERNAME/Daily-Image-Project/actions
  👉 Link: _________________________________

═══════════════════════════════════════════════════════════════════

🚀 STEP-BY-STEP FLOW

ADIM 1: GitHub Setup
├─ Repository create et
├─ Git initialize et
├─ Commit & push
└─ ✅ Repository görülüyor

ADIM 2: Netlify Setup
├─ GitHub authorize et
├─ Repository seç
├─ Build settings (public/)
├─ Deploy et
└─ ✅ Site URL alındı

ADIM 3: API Configuration
├─ FLICKR_API_KEY ekle
├─ HF_API_KEY ekle
├─ Local'de test et
└─ ✅ Keys working

ADIM 4: Testing
├─ Website açılıyor?
├─ Mock veri gösteriliyor?
├─ Workflow trigger et
├─ 5 dakika bekle
├─ Yeni veri işlendi?
└─ ✅ All systems go!

ADIM 5: Monitoring
├─ Daily check (veri güncel mi?)
├─ Weekly check (errors var mı?)
├─ Monthly check (archive büyüyor mu?)
└─ ✅ System stable

═══════════════════════════════════════════════════════════════════

⏰ SONRAKI OTOMATİK ADIMLAR

Günlük (09:00 UTC):
  🔄 GitHub Actions trigger olur
  📸 Flickr'dan rastgele foto çekilir
  🤖 LLaVA ile analiz yapılır
  💾 public/data/ güncellenir
  🚀 Netlify otomatik redeploy eder
  🌐 Website güncellenmiş veriyi gösterir

Arşiv Yönetimi:
  📊 archive.json son 30 günü tutuyor
  🗑️ Otomatik olarak eski veri temizlenir
  💾 Total size ~50-100MB

═══════════════════════════════════════════════════════════════════

🎯 SUCCESS INDICATORS

✅ Website canlı yayında
✅ Mock veri gösteriliyor
✅ Günlük güncelleme yapılıyor
✅ GitHub Actions başarılı
✅ Logs temiz (error yok)
✅ Archive build up oluyor
✅ Data JSON accessible
✅ Responsivedesign çalışıyor

Hepsini görüyorsan → BAŞARI! 🎉

═══════════════════════════════════════════════════════════════════

🚨 YAYGGIN SORUNLAR & ÇÖZÜMLER

Problem: "Build failed"
Solution: Netlify logs açılı → Hata mesajını oku
          (publish directory, build command, etc.)

Problem: "API error 401"
Solution: GitHub Secrets check et
          API key'i yenile ve update et

Problem: "Website eski veriyi gösteriyor"
Solution: Browser cache clear et (CTRL+Shift+Delete)
          veya Netlify cache clear et

Problem: "Workflow başlamıyor"
Solution: Actions enabled mi? Settings check et
          Secrets complete mi?

Problem: "JSON geçersiz"
Solution: Script logs check et
          Manual python scripts/fetch_image.py çalıştır

İlgili Dosya: docs/TROUBLESHOOTING.md

═══════════════════════════════════════════════════════════════════

📚 DOKÜMANTASYON

Detaylı Rehberler:
  📖 GITHUB_NETLIFY_COMPLETE_GUIDE.md    - Full setup
  📖 API_CONNECTION_TEST.md              - API testing
  📖 NETLIFY_SETUP_GUIDE.md              - Netlify config
  📖 docs/DEPLOYMENT.md                  - Production

Hızlı Referanslar:
  📋 docs/TROUBLESHOOTING.md             - Sorun giderme
  📋 docs/API.md                         - API reference
  📋 .github/workflows/daily-image.yml   - Workflow config

═══════════════════════════════════════════════════════════════════

📞 DESTEK

Sorun mu?
  → docs/TROUBLESHOOTING.md kontrol et
  → API errors? → docs/API.md
  → Deployment? → docs/DEPLOYMENT.md

API Key alma:
  → Flickr: https://www.flickr.com/services/apps/create/
  → HF: https://huggingface.co/settings/tokens

═══════════════════════════════════════════════════════════════════

✨ TAMAMLAMA MESAJI

Hepsini bitirdiysen:

  ✅ Site: https://YOUR-SITE.netlify.app (canlı)
  ✅ API: Flickr + HuggingFace connected
  ✅ Automation: Daily workflow running
  ✅ Data: JSON updated & archived
  ✅ Monitoring: System stable

BAŞARILI DEPLOYMENT! 🏛️

İyi kodlamalar!

═══════════════════════════════════════════════════════════════════

