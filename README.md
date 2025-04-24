🕵️ TikTok Investigator: seeker.py
Investigate TikTok accounts for potential scam behavior, location hints, and suspicious comments — fully automated with PDF reports, map tracing, and live status detection.


🧠 Overview
seeker.py is a professional-grade investigation tool designed for OSINT analysts, cybersecurity teams, digital journalists, and concerned users to analyze public TikTok accounts.

This tool scrapes account metadata, detects scam-related comments, extracts location hints, checks LIVE status, and generates an automated PDF report — complete with comment analysis and Google Maps route preview.

⚙️ Features

Feature	Description
🔍 Scam Keyword Detection	Automatically identifies suspicious comments using a customizable keyword list (cuan, pinjol, etc).
🗺️ Location Extraction	Detects potential location names from bios, video captions, and comments.
📡 Live Stream Scanner	Determines if the user is currently live and displays metadata.
🧾 PDF Report Generator	Exports all findings into a professional PDF, including suspicious comments per video.
🗂 JSON Export	Full investigation logs are stored in structured .json format for future reference.
🌐 Google Maps Integration	Opens traced locations as directions on Google Maps (multi-stop route).
📷 Sample Output
✅ Sample generated content:

@target_laporan.pdf – Full professional report with all data

@target_laporan.json – Raw structured data

Google Maps – Open suspected locations directly

👇 Sample PDF snippet:

🚀 Quickstart
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/tiktok-investigator.git
cd tiktok-investigator
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
⚠️ Ensure you're using Python 3.12+

3. Set Google Maps API Key
Edit the script seeker.py:

python
Copy
Edit
GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
🔑 Get your API key here

4. Run the Tool
bash
Copy
Edit
python seeker.py
Then enter the TikTok username (without @) when prompted.

🧠 Use Cases
👮‍♂️ OSINT Investigators tracking potential fraudulent accounts

🎓 Academic research into TikTok activity trends or scam behaviors

👨‍👩‍👧‍👦 Parents monitoring suspicious TikTok accounts

📰 Digital journalists collecting evidence on scam trends

🛡️ Cybercrime units monitoring financial scam accounts

🛠️ Roadmap (Planned Upgrades)
 GUI mode (PyQt or Streamlit)

 Email or Telegram alert support

 Export to Excel and Google Sheets

 More intelligent NLP-based comment filtering

 Threat level rating system

📁 File Structure
bash
Copy
Edit
📦 tiktok-investigator/
├── seeker.py              # Main investigation script
├── requirements.txt       # Dependencies
├── @username_laporan.pdf  # Output: generated report
├── @username_laporan.json # Output: raw investigation data
🤝 Contributing
Contributions are welcome!

💡 Suggest new scam keywords

🧪 Improve AI/NLP-based comment filtering

📊 Add better visualization/reporting

🎨 Enhance PDF styling
