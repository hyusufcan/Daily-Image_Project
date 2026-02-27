# 🚀 Quick Start Guide

## 5-Minute Setup

### Step 1: Get Your API Keys (5 min)

**Flickr API:**
1. Visit: https://www.flickr.com/services/apps/create/apply/
2. Fill in: App name (anything), Description (personal use)
3. Submit → Copy your **API Key**

**Hugging Face:**
1. Visit: https://huggingface.co/join
2. After signup: Settings → Access Tokens
3. Create token → Copy it

### Step 2: Fork & Setup (2 min)

1. **Fork this repository** (button at top right on GitHub)
2. Go to **your forked repo** → Settings → Secrets and variables → Actions
3. Add two secrets:
   - Name: `FLICKR_API_KEY` → Value: [paste your Flickr key]
   - Name: `HF_API_KEY` → Value: [paste your HF token]

### Step 3: Deploy to Netlify (3 min)

1. Visit: https://app.netlify.com/start
2. Click **"Import from Git"**
3. Choose **GitHub** → Select your forked repo
4. Build settings:
   - Build command: Leave empty or type `echo 'static'`
   - Publish directory: `public`
5. Click **"Deploy site"**
6. Done! 🎉

### Step 4: Test It

1. In your GitHub repo → **Actions** tab
2. Click **"Daily British Library Image"**
3. Click **"Run workflow"** → Run workflow
4. Wait ~2 minutes
5. Refresh your Netlify site → See your first image!

---

## What Happens Next?

- **Every day at 9:00 AM UTC**, a new image is automatically fetched
- GitHub Actions runs the Python script
- LLaVA AI analyzes the image
- New content auto-deploys to your Netlify site
- Zero maintenance required!

---

## Troubleshooting

**"Workflow doesn't run"**
→ Go to Actions tab → Enable workflows

**"No image showing"**
→ Run workflow manually first (Step 4 above)

**"API error"**
→ Check your API keys are correct in Secrets

---

## Customization

**Change the daily time:**
Edit `.github/workflows/daily-image.yml` line 5:
```yaml
- cron: '0 9 * * *'  # Change '9' to any hour (0-23, UTC)
```

**Modify the AI prompt:**
Edit `scripts/fetch_image.py` around line 68

**Change colors:**
Edit `public/index.html` CSS variables (line 20-30)

---

**Need help?** Check the full README.md for detailed docs!
