# 🏛️ The Daily Antiquarian

Victorian-themed daily showcase of historical images from the British Library, analyzed by AI.

## ✨ Features

- 📸 **Daily Random Image** from British Library's 1M+ Flickr collection
- 🤖 **AI Analysis** using LLaVA (open-source vision-language model)
- 🎨 **Victorian Library Aesthetic** - rich, dark, ornamental design
- 🔄 **Automated** with GitHub Actions (runs daily at 9:00 UTC)
- 🌐 **Deployed on Netlify** - completely free hosting

## 🏗️ Architecture

```
GitHub Actions (Cron Job)
    ↓
Flickr API → Random British Library Image
    ↓
Hugging Face LLaVA → AI Analysis
    ↓
Save to JSON + Download Image
    ↓
Auto-commit to Repo
    ↓
Netlify Auto-deploy
```

## 🚀 Setup Instructions

### 1. Fork This Repository

Click the "Fork" button on GitHub to create your own copy.

### 2. Get API Keys

#### Flickr API Key (Free)
1. Go to https://www.flickr.com/services/apps/create/
2. Create a new app (non-commercial)
3. Copy your **API Key**

#### Hugging Face API Token (Free)
1. Sign up at https://huggingface.co
2. Go to Settings → Access Tokens
3. Create a new token with "Read" access
4. Copy your **token**

### 3. Add Secrets to GitHub

1. Go to your forked repo → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add these secrets:
   - `FLICKR_API_KEY`: Your Flickr API key
   - `HF_API_KEY`: Your Hugging Face token

### 4. Deploy to Netlify

#### Option A: Automatic (Recommended)
1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Choose GitHub and select your forked repo
4. Build settings:
   - Build command: `echo 'Static site'`
   - Publish directory: `public`
5. Click "Deploy site"

#### Option B: Netlify CLI
```bash
npm install -g netlify-cli
netlify login
netlify init
netlify deploy --prod
```

### 5. Enable GitHub Actions

1. Go to your repo → Actions tab
2. Click "I understand my workflows, go ahead and enable them"
3. The workflow will run daily at 9:00 UTC automatically

### 6. Manual Trigger (Optional)

To test immediately without waiting:
1. Go to Actions tab
2. Click "Daily British Library Image"
3. Click "Run workflow" → "Run workflow"

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── daily-image.yml      # GitHub Actions workflow
├── scripts/
│   └── fetch_image.py           # Python script for fetching & analyzing
├── public/
│   ├── index.html               # Victorian-themed webpage
│   └── images/                  # Downloaded images (auto-generated)
├── data/
│   ├── daily-image.json         # Current day's data
│   └── archive.json             # Last 30 days (optional)
├── netlify.toml                 # Netlify configuration
└── README.md
```

## 🎨 Design Theme

**Victorian Library Aesthetic:**
- Dark, rich background with burgundy and forest green accents
- Gold ornamental borders and decorations
- Serif fonts: Cinzel (headers), Crimson Text (body), IM Fell English (decorative)
- Sepia-toned images with antique frames
- Scholarly, archival presentation
- Responsive design

## 🔧 Customization

### Change Schedule

Edit `.github/workflows/daily-image.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'  # Change time (UTC)
```

### Modify AI Prompt

Edit `scripts/fetch_image.py`, around line 68:
```python
prompt = """Your custom analysis prompt here..."""
```

### Style Adjustments

Edit `public/index.html` CSS variables:
```css
:root {
    --parchment: #f4e9d8;
    --burgundy: #6b2737;
    --gold: #d4af37;
    /* Customize colors */
}
```

## 🧪 Local Testing

```bash
# Install dependencies
pip install requests pillow

# Set environment variables
export FLICKR_API_KEY="your_key"
export HF_API_KEY="your_token"

# Run script
python scripts/fetch_image.py

# Serve locally
python -m http.server 8000 --directory public
# Visit http://localhost:8000
```

## 📊 AI Model Details

**LLaVA 1.5 7B** (llava-hf/llava-1.5-7b-hf)
- Open-source vision-language model
- Fast inference (~3-5 seconds)
- Good balance of quality and speed
- Free on Hugging Face Inference API

**Alternative Models (if you want to change):**
- `Salesforce/blip-image-captioning-large` - Faster, simpler descriptions
- `nlpconnect/vit-gpt2-image-captioning` - Lightweight alternative

## 🌐 Live Demo

After deploying, your site will be at:
```
https://your-site-name.netlify.app
```

## 🔒 Privacy & Licensing

- All images from British Library Flickr (public domain/open access)
- AI analysis is original content
- Code is MIT licensed
- British Library attribution maintained

## 🐛 Troubleshooting

**Workflow doesn't run:**
- Check if Actions are enabled in repo settings
- Verify secrets are set correctly

**No image showing:**
- Check browser console for errors
- Verify `data/daily-image.json` exists
- Check image path in JSON

**API errors:**
- Verify API keys are correct
- Check Hugging Face model status
- Try manual trigger to see error logs

**Netlify deploy fails:**
- Ensure `public` directory exists
- Check netlify.toml configuration

## 📚 Resources

- [British Library Flickr](https://www.flickr.com/photos/britishlibrary/)
- [Flickr API Docs](https://www.flickr.com/services/api/)
- [Hugging Face Inference API](https://huggingface.co/docs/api-inference/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Netlify Docs](https://docs.netlify.com/)

## 🎯 Future Enhancements

- [ ] Archive view (show past 30 days)
- [ ] Multiple images per day
- [ ] User voting/favorites
- [ ] RSS feed
- [ ] Social sharing
- [ ] Print-ready PDF export
- [ ] Dark/light theme toggle

## 📝 License

MIT License - Feel free to use and modify!

---

**Built with ❤️ and a love for Victorian aesthetics**
