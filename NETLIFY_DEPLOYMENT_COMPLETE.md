# 🚀 NETLIFY DEPLOYMENT - ADIM ADIM

**Site:** https://dailyimage.netlify.app/ ✅

---

## 1️⃣ GITHUB-NETLIFY BAĞLANTISI

### Adım 1: Netlify'de Site Bağla
1. https://app.netlify.com/sites → Siteni seç
2. **Site settings** → **Build & deploy**
3. **Repository** bölümünde → **Edit settings**
4. **Repository:** `hyusufcan/Daily-Image_Project`
5. **Branch to deploy:** `main`
6. **Save**

### Adım 2: Automatic Deploy Etkinleştir
✅ Otomatik olarak etkindir
- Her `git push main` → Netlify auto-deploy
- Deploy status: Netlify dashboard'da gözükür

---

## 2️⃣ ENVIRONMENT VARIABLES (ÖNEMLİ!)

### Netlify'de Secrets Ekle

**Path:** https://app.netlify.com/sites/dailyimage/settings/deploys#environment

**Ekle:**
```
FLICKR_API_KEY = [your-flickr-key]
HF_API_KEY = [your-huggingface-token]
```

### Adım:
1. Site settings → **Deploys**
2. **Environment** → **Edit variables**
3. Add variable:
   - Name: `FLICKR_API_KEY`
   - Value: [actual key from Flickr]
4. Add variable:
   - Name: `HF_API_KEY`
   - Value: [actual token from HF]
5. **Save**

⚠️ **NOT:** GitHub Secrets ile AYNI şekilde yapılandır!

---

## 3️⃣ GITHUB ACTIONS - ENVIRONMENT SECRETS

### GitHub Settings'e git:
https://github.com/hyusufcan/Daily-Image_Project/settings/secrets/actions

### Ekle:

**1. FLICKR_API_KEY**
- Name: `FLICKR_API_KEY`
- Secret: [your-actual-flickr-api-key]

**2. HF_API_KEY**
- Name: `HF_API_KEY`
- Secret: [your-actual-huggingface-token]

### Workflow Otomatik Çalışacak:
- **Schedule:** Her gün 09:00 UTC
- **Manual trigger:** Dilersen `workflow_dispatch`
- **Output:** GitHub Actions → Actions tab'ında gözükür

---

## 4️⃣ API KEYLERİ ALMA

### Flickr API Key:
1. https://www.flickr.com/services/apps/create/
2. Sign in → API key iste
3. Application name: "Daily Antiquarian"
4. Key copy et → GitHub/Netlify secrets'e ekle

### HuggingFace Token:
1. https://huggingface.co/settings/tokens
2. "New token" → Create
3. Name: "daily-image-token"
4. Role: "read"
5. Token copy et → GitHub/Netlify secrets'e ekle

---

## 5️⃣ TEST WORKFLOW

### Manual Test (GitHub):
1. Repository → **Actions**
2. **daily-image workflow** seç
3. **Run workflow** → **Main branch**
4. **Run workflow** tıkla
5. 2-3 dakika bekle

### Başarı Kontrol:
✅ Workflow logs: All green
✅ `daily-image.json` update edildi
✅ Netlify auto-deploy triggered

### Netlify'de Gözle:
https://app.netlify.com/sites/dailyimage → **Deploys**
- Last deploy: Workflow'dan
- Status: Published ✅

---

## 6️⃣ PRODUCTION URL VERİFİKASYON

### Test Et:
```
https://dailyimage.netlify.app/
```

### Kontrol Listesi:
✅ HTML yükleniyor
✅ CSS styles apply
✅ Mock image görünüyor (veya live image)
✅ AI analysis text var
✅ Archive sidebar çalışıyor
✅ Mobile responsive

---

## 7️⃣ DAILY AUTOMATION

### Workflow Schedule:
```yaml
schedule:
  - cron: '0 9 * * *'  # 09:00 UTC her gün
```

### İşlem Sırası:
1. **09:00 UTC** → GitHub Actions trigger
2. Flickr API → Random photo al
3. LLaVA AI → Analiz yap
4. JSON update → `daily-image.json`
5. Git commit → `main` branch
6. Netlify auto-deploy → Live update

---

## 8️⃣ MONITORING

### GitHub Actions:
- Repository → **Actions**
- Recent workflow runs gözle
- Failures → Logs'u kontrol et

### Netlify:
- Dashboard → **Deploys**
- Recent deploys gözle
- Deployment preview link

### Error Handling:
- API timeout → Fallback mock data
- Network error → Previous day's image
- AI error → Default analysis text

---

## 9️⃣ TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Workflow fails | Check GitHub Secrets are set |
| Deploy fails | Check `netlify.toml` publish directory |
| Images not load | Check Flickr API key valid |
| AI analysis missing | Check HF API token valid |
| No auto-deploy | Check GitHub-Netlify connection |

---

## 🔟 NEXT STEPS

✅ **Completed:**
- GitHub repo created
- Netlify site deployed
- Site connected to GitHub

📋 **To-Do:**
1. [ ] Add FLICKR_API_KEY to Netlify environment
2. [ ] Add HF_API_KEY to Netlify environment
3. [ ] Add FLICKR_API_KEY to GitHub Secrets
4. [ ] Add HF_API_KEY to GitHub Secrets
5. [ ] Manual workflow trigger to test
6. [ ] Verify daily-image.json updated
7. [ ] Check live site on https://dailyimage.netlify.app/

---

## 📞 QUICK REFERENCE

**Site URL:** https://dailyimage.netlify.app/

**GitHub:** https://github.com/hyusufcan/Daily-Image_Project

**Netlify Dashboard:** https://app.netlify.com/sites/dailyimage

**GitHub Actions:** https://github.com/hyusufcan/Daily-Image_Project/actions

**Netlify Logs:** https://app.netlify.com/sites/dailyimage/deploys

---

**Status:** 🟢 LIVE & READY FOR API KEYS

