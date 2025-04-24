import json
import requests
import webbrowser
import asyncio
from TikTokApi import TikTokApi
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pyfiglet

# ========== ASCII HEADER ==========

def print_ascii_header():
    ascii_art = r"""
                      ▄
                     ▄█▄
                    ▄███▄
                   ▄█████▄
                  ▄███████▄
                 ▄ ▀▀██████▄
                ▄██▄▄ ▀█████▄
               ▄█████████████▄
              ▄███████████████▄
             ▄█████████████████▄
            ▄███████████████████▄
           ▄█████████▀▀▀▀████████▄
          ▄████████▀      ▀███████▄
         ▄█████████        ████▀▀██▄
        ▄██████████        █████▄▄▄
       ▄██████████▀        ▀█████████▄
      ▄██████▀▀▀              ▀▀██████▄
     ▄███▀▀                       ▀▀███▄
    ▄▀▀                               ▀▀▄
    """
    print(ascii_art)
    print(pyfiglet.figlet_format("TikTok Scraper", font="slant"))
    print(pyfiglet.figlet_format("Investigate", font="slant"))

# ========== KONFIGURASI ==========

GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
KEYWORDS_SCAM = ["cuan", "transfer", "pinjol", "hadiah", "dm gue", "bagi duit", "saldo"]
LOKASI_KEYWORDS = ["jakarta", "bandung", "surabaya", "medan", "bali", "makassar", "jogja", "indonesia"]

# ========== FUNGSI BANTUAN ==========

def detect_location(text):
    text = text.lower()
    return next((loc.title() for loc in LOKASI_KEYWORDS if loc in text), None)

def extract_location(profile_bio, videos):
    locations = set()
    if bio_loc := detect_location(profile_bio):
        locations.add(bio_loc)
    for vid in videos:
        if loc := detect_location(vid['desc']):
            locations.add(loc)
        for c in vid.get('comments', []):
            if loc := detect_location(c['comment']):
                locations.add(loc)
    return list(locations)

def geocode_location(location_name):
    try:
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json",
                                params={"address": location_name, "key": GOOGLE_MAPS_API_KEY})
        data = response.json()
        if data["status"] == "OK":
            loc = data["results"][0]["geometry"]["location"]
            return loc["lat"], loc["lng"], data["results"][0]["formatted_address"]
    except Exception as e:
        print(f"[!] Geocoding gagal: {e}")
    return None, None, None

def open_map(locations):
    base_url = "https://www.google.com/maps/dir/"
    coords = []
    for loc in locations:
        lat, lng, detail = geocode_location(loc)
        if lat and lng:
            coords.append(f"{lat},{lng}")
            print(f"[→] Lokasi: {detail}")
    if coords:
        webbrowser.open(base_url + "/".join(coords))
    else:
        print("[!] Tidak ada koordinat yang valid.")

def generate_pdf(username, data):
    filename = f"{username}_laporan.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"Laporan Investigasi TikTok: @{username}")
    y -= 30

    c.setFont("Helvetica", 11)
    lokasi_text = ", ".join(data['lokasi_diduga']) or "Tidak diketahui"
    c.drawString(50, y, f"Lokasi Diduga: {lokasi_text}")
    y -= 15
    live = data['live_status']
    live_text = f"LIVE: {live['title']} | Viewers: {live['viewers']}" if live['is_live'] else "Tidak sedang LIVE"
    c.drawString(50, y, f"Status: {live_text}")
    y -= 25

    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Komentar Mencurigakan:")
    y -= 20

    for video in data['videos']:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, f"Video: {video['url']}")
        y -= 12
        c.setFont("Helvetica", 9)
        c.drawString(60, y, f"Deskripsi: {video['desc'][:80]}...")
        y -= 12
        for cmt in video.get('comments', []):
            c.drawString(70, y, f"- @{cmt['user']}: {cmt['comment'][:80]}... [Keyword: {cmt['keyword']}]")
            y -= 10
            if y < 100:
                c.showPage()
                y = height - 50
        y -= 10

    c.save()
    print(f"[✓] PDF laporan disimpan sebagai: {filename}")

# ========== FUNGSI UTAMA ==========

async def scrape_account(username, max_videos=5):
    # Membuat instance TikTokApi secara manual
    api = TikTokApi.get_instance()

    try:
        # Mendapatkan profil pengguna
        user = api.user(username)
        profile = await user.info()

        bio = profile['signature']  # Mengambil bio pengguna
        user_id = profile['id']

        # Mendapatkan status live (jika ada)
        live_status = await api.get_user_live(user_id=user_id)

        videos_data = []
        scam_count = 0

        for video in await user.videos(count=max_videos):
            v = video.as_dict
            video_id = v['id']
            comments_detected = []

            try:
                # Mengambil komentar untuk setiap video
                for comment in video.comments():
                    text = comment['text'].lower()
                    for k in KEYWORDS_SCAM:
                        if k in text:
                            comments_detected.append({
                                'user': comment['user']['nickname'],
                                'comment': text,
                                'keyword': k
                            })
                            scam_count += 1
            except Exception as e:
                print(f"[!] Gagal ambil komentar: {e}")

            videos_data.append({
                'id': video_id,
                'desc': v.get('desc', ''),
                'url': f"https://www.tiktok.com/@{username}/video/{video_id}",
                'comments': comments_detected
            })

        # Mengekstrak lokasi yang diduga dari profil dan video
        lokasi_diduga = extract_location(bio, videos_data)

        # Menyusun hasil data
        result = {
            'username': username,
            'profile': profile,
            'lokasi_diduga': lokasi_diduga,
            'live_status': live_status,
            'videos': videos_data,
            'total_scam_comments': scam_count
        }

        # Menyimpan data ke file JSON
        with open(f"{username}_laporan.json", "w") as f:
            json.dump(result, f, indent=2)

        # Membuat PDF laporan
        generate_pdf(username, result)

        print(f"[✓] Investigasi selesai untuk @{username}.")
        if lokasi_diduga:
            print("[🗺️] Membuka dugaan lokasi di Google Maps...")
            open_map(lokasi_diduga)
        else:
            print("[!] Lokasi tidak ditemukan.")

    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")
    finally:
        await api.close()

# ========== MAIN ==========

if __name__ == "__main__":
    print_ascii_header()
    target = input("Masukkan username TikTok (tanpa @): ").strip()
    if target:
        asyncio.run(scrape_account(target))
    else:
        print("[!] Username tidak boleh kosong.")
