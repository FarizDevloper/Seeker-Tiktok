<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?center=true&lines=🕵️+TikTok+Investigator+CLI+Tool;Analyze+Suspicious+Accounts+on+TikTok;PDF+Reports+%7C+Map+Tracking+%7C+LIVE+Check&font=Fira+Code&pause=1000&color=58A6FF&center=true&width=1000&height=50">
</p>

<h1 align="center">🕵️ TikTok Investigator - <code>seeker.py</code></h1>

<p align="center">
  <b>A professional OSINT tool for scanning and analyzing TikTok accounts for scam behavior, location tracking, and comment-based red flags.</b><br>
  Generates a full PDF report, opens Google Maps, and checks LIVE status.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
  <img src="https://img.shields.io/badge/Platform-Windows%7CLinux%7CMacOS-lightgrey">
  <img src="https://img.shields.io/badge/Report-PDF%20Auto-red.svg?logo=adobeacrobatreader">
  <img src="https://img.shields.io/badge/Map-Google%20Route-yellow.svg?logo=googlemaps">
</p>

---

   TikTok Scam & Location Investigator CLI
     [PDF Reports | Live Check | Maps]      

---

## 🔍 Key Features

- 🧠 **Scam Comment Detection** – Flags risky keywords like `cuan`, `pinjol`, `promo`, etc.
- 🌐 **Location Tracker** – Extracts location clues from bio, captions, and comments.
- 🎥 **LIVE Status Detector** – Check if account is currently live on TikTok.
- 🧾 **Professional PDF Report** – Auto-exported report with all data in beautiful layout.
- 🗺️ **Google Maps Integration** – Trace user’s detected locations visually in a multi-stop route.
- 📦 **JSON Output** – Structured data also saved for use in other tools.

---

## 🧪 Sample Output

> Output files:
> 📄 @username_laporan.pdf → Full investigation report
> 📜 @username_laporan.json → Raw data in structured format
> 🌍 Google Maps route → Locations found from comments & bios


---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/tiktok-investigator.git
cd tiktok-investigator

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your Google Maps API Key to the script:

python
Copy
Edit
GOOGLE_MAPS_API_KEY = "YOUR_API_KEY_HERE"
🚀 Usage
bash
Copy
Edit
python seeker.py
Masukkan username TikTok (tanpa @) saat diminta. Tool akan langsung bekerja.

📚 Roadmap
✅ Scam comment detection

✅ Location hint extraction

✅ PDF & JSON export

✅ Google Maps routing

🚧 GUI mode (Streamlit/PyQt)

🚧 Telegram/Email alert system

🚧 Threat level scoring system

💡 Example Use Cases

User	Benefit
🕵️ OSINT Investigator	Trace scam patterns & TikTok scam networks
👨‍👩‍👧 Parents	Monitor suspicious influencers followed by children
📰 Journalists	Research viral scam tactics via TikTok
🛡️ Cybersecurity Teams	Flag dangerous financial TikTok trends
🤝 Contribute
PRs welcome! You can:

🔍 Add smarter keyword detection (NLP-based)

🎨 Improve PDF report formatting

🌍 Expand location extraction logic

💬 Translate to multi-language support

