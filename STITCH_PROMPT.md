# 🎨 Stitch AI Design Prompt

Use this prompt when creating additional design variations or components in Stitch:

---

## Victorian Library Aesthetic - Design System

**Theme:** Dark Victorian Library / Antiquarian Scholar's Study

**Core Mood:**
- Scholarly gravitas with ornamental luxury
- Rich, atmospheric darkness punctuated by golden accents
- Reverence for history and accumulated knowledge
- Melancholic beauty of preserved wisdom

**Color Palette:**

```
PRIMARY DARK TONES:
- Deep Charcoal: #1a1614 (main background)
- Burnt Umber: #2d2520 (secondary background)
- Sepia Brown: #704214 (aged effect)

ACCENT COLORS:
- Antique Gold: #d4af37 (borders, titles, highlights)
- Deep Burgundy: #6b2737 (decorative elements)
- Forest Green: #2d4a3e (secondary accent)

LIGHT TONES:
- Aged Parchment: #f4e9d8 (primary text)
- Weathered Paper: #e8dcc4 (secondary text)
```

**Typography Hierarchy:**

```
DISPLAY (Titles, Headers):
- Font: Cinzel
- Weight: 600-700
- Style: Uppercase, generous letter-spacing (2-4px)
- Color: Antique Gold
- Effects: Subtle text-shadow with gold glow

DECORATIVE (Subtitles, Italics):
- Font: IM Fell English
- Style: Italic
- Color: Aged Paper
- Use: Poetic flourishes, quotes, subtitles

BODY (Main Content):
- Font: Crimson Text
- Size: 1.15-1.3rem
- Line-height: 1.8-2.0
- Style: Serif, highly readable
- Color: Parchment
```

**Visual Elements:**

BORDERS & FRAMES:
- Double-line borders in gold
- Corner decorations: ⚜ ❦ ❧ symbols
- Gradient borders mixing burgundy and gold
- 8-10px ornate picture frames with sepia inner border

BACKGROUNDS:
- Dark gradients (never solid)
- Subtle repeating patterns (45deg diagonal lines)
- Layered transparencies
- Atmospheric vignettes on images

DECORATIVE MOTIFS:
- Fleur-de-lis (⚜)
- Ornamental dividers (◈ ❦ ❧)
- Large decorative quotation marks
- Corner flourishes
- Damask/wallpaper patterns (very subtle, 3% opacity)

**Layout Principles:**

1. **Generous Padding:** 40-60px on cards, creates breathing room
2. **Centered Symmetry:** Most elements centered for formal, classical feel
3. **Layered Depth:** Use box-shadows extensively (0 20px 60px rgba(0,0,0,0.5))
4. **Border Complexity:** Multiple nested borders create richness
5. **Fixed Ornamental Frame:** Body::after creates permanent border around entire viewport

**Animation & Interaction:**

```css
ENTRANCE ANIMATIONS:
- fadeInDown for headers (1.2s ease-out)
- fadeInUp for content (1.4s ease-out, 0.3s delay)
- Stagger delays for sequential reveal

HOVER STATES:
- Gentle scale (1.02) on images
- Transform translateY(-3px) on buttons
- Fade-in overlays with metadata
- Enhanced box-shadows with gold glow

TRANSITIONS:
- All: 0.3-0.5s ease
- Never abrupt, always elegant
```

**Component Styling Patterns:**

CARDS:
```css
background: linear-gradient(135deg, rgba(26,22,20,0.95), rgba(45,37,32,0.95));
border: 3px solid var(--gold);
box-shadow: 
    0 20px 60px rgba(0,0,0,0.5),
    inset 0 0 100px rgba(212,175,55,0.05);
padding: 60px;
```

BUTTONS/LINKS:
```css
background: linear-gradient(135deg, var(--burgundy), var(--forest-green));
border: 2px solid var(--gold);
font-family: 'Cinzel', serif;
text-transform: uppercase;
letter-spacing: 2px;
```

IMAGES:
```css
filter: sepia(0.2) contrast(1.1);
border: 8px solid var(--sepia);
box-shadow: 0 0 0 2px var(--gold);
/* Gradient overlay on top */
```

**Atmospheric Effects:**

1. **Paper Texture:** Subtle noise/grain overlay
2. **Vignette:** Dark corners on backgrounds
3. **Sepia Tinting:** Slight warm filter on images
4. **Light Rays:** Occasional diagonal gradient streaks (very subtle)
5. **Shadow Depth:** Multi-layered shadows for 3D effect

**Responsive Behavior:**

Mobile (<768px):
- Reduce padding to 20-30px
- Simplify borders (single instead of double)
- Font sizes: clamp() for fluid typography
- Maintain ornamental elements but scale down
- Keep the aristocratic feel, just more compact

**Examples for Stitch:**

"Create a Victorian library card component with an aged parchment background, gold borders, and Cinzel headings"

"Design a testimonial section in dark Victorian style with burgundy accents and ornate quotation marks"

"Make a footer with the aesthetic of an old library catalog card - sepia tones, typewriter-style font, subtle texture"

"Generate a navigation menu that looks like leather-bound book spines on a shelf, with gold lettering"

---

## Key Principles Summary:

✅ **ALWAYS USE:** Dark backgrounds, gold accents, serif fonts, generous shadows
✅ **NEVER USE:** Bright colors, sans-serif body text, flat design, minimalism
✅ **EMOTION:** Scholarly, reverent, luxurious, slightly melancholic
✅ **ERA:** 1850-1900 Victorian England
✅ **REFERENCE:** British Library, Victorian reading rooms, illuminated manuscripts

---

**Stitch Generation Tips:**

1. Start with "Victorian library aesthetic" or "antiquarian scholar theme"
2. Mention specific colors: "deep burgundy, antique gold, aged parchment"
3. Reference fonts: "Cinzel for headers, Crimson Text for body"
4. Request ornamental elements: "add fleur-de-lis corners and gold borders"
5. Specify mood: "atmospheric, scholarly, richly decorated"

**Example Full Prompt for Stitch:**

> "Create a hero section in Victorian library aesthetic: dark charcoal background (#1a1614), large centered title in Cinzel font with antique gold color (#d4af37), ornamental borders with fleur-de-lis corners, burgundy and forest green gradient accents, aged parchment text (#f4e9d8), generous padding, atmospheric depth with layered shadows, decorative dividers with ◈ symbols, overall mood: scholarly grandeur from 1880s British reading room"
