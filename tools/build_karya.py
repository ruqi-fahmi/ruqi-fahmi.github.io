"""
Bangun halaman detail karya, dua bahasa, dari satu sumber data.

Sengaja dibuat sebagai generator, bukan sepuluh berkas HTML yang ditulis
tangan. Sepuluh salinan yang ditulis manual pasti akan menyimpang satu sama
lain begitu ada perubahan kecil.

Jalankan dari mana saja:
    python tools/build_karya.py
"""

from __future__ import annotations

import html as H
import json
import pathlib

AKAR = pathlib.Path(__file__).resolve().parent.parent
SITUS = "https://ruqi-fahmi.github.io"

# ---------------------------------------------------------------- data

KARYA = [
    {
        "slug": "pranpc-indihome",
        "varian": "papan",
        "id": {
            "nama": "Dashboard PraNPC IndiHome",
            "ringkas": "Papan pantau efektivitas penagihan tahap akhir untuk pelanggan IndiHome.",
            "peran": "Perancang dan pengembang tunggal",
            "masa": "2026 sampai sekarang",
            "masalah": [
                "Tim penagihan tahap akhir menilai capaian dari beberapa sumber yang terpisah. "
                "Data pekerjaan lapangan ada di satu tempat, hasil kontak di tempat lain, dan "
                "konfirmasi pembayaran di tempat ketiga. Menyatukannya dikerjakan manual, "
                "berulang setiap hari, dan hasilnya sering berbeda antar orang.",
                "Akibatnya pertanyaan sederhana seperti berapa capaian hari ini dan siapa yang "
                "tertinggal justru butuh waktu lama untuk dijawab, padahal jawabannya "
                "dibutuhkan setiap pagi.",
            ],
            "pendekatan": [
                "Saya menyatukan ketiga sumber itu ke dalam satu basis data, lalu membangun "
                "papan pantau yang menjawab pertanyaan harian tim secara langsung: capaian "
                "terhadap target, laju harian, perbandingan dengan periode sebelumnya, sampai "
                "peringkat per wilayah dan per petugas.",
                "Seluruh lapisannya saya kerjakan sendiri, mulai dari pengambilan dan "
                "sinkronisasi data, perancangan skema dan kueri, antarmuka yang dipakai tim, "
                "sampai penerapan di server produksi berikut pemantauannya.",
            ],
            "keputusan": [
                ("Definisi metrik dibakukan lebih dulu",
                 "Sebelum menulis kueri, saya menetapkan definisi baku untuk setiap metrik dan "
                 "mendokumentasikannya. Satu metrik yang didefinisikan berbeda antar halaman "
                 "akan menyesatkan keputusan tanpa ada yang menyadari, dan kesalahan seperti itu "
                 "jauh lebih mahal daripada tampilan yang kurang menarik."),
                ("Periode operasional tidak sama dengan bulan kalender",
                 "Siklus penagihan tidak berhenti di akhir bulan, sehingga seluruh perhitungan "
                 "laju dan perbandingan antar periode harus mengikuti definisi periode "
                 "operasional. Menyalin logika bulan kalender akan membuat setiap angka meleset."),
                ("Perhitungan berat dipindahkan ke basis data",
                 "Agregasi dilakukan sedekat mungkin dengan datanya, dengan indeks yang memang "
                 "dipakai. Antarmuka hanya menerima hasil yang sudah siap, sehingga halaman "
                 "tetap ringan meski data terus bertambah."),
            ],
            "hasil": "Dipakai harian oleh tim operasional sebagai rujukan utama capaian penagihan.",
            "stack": ["Python", "MySQL", "SQL Server", "Vue 3", "PrimeVue", "Vite",
                      "Linux", "Nginx", "Git", "GitHub Actions"],
        },
        "en": {
            "nama": "Dashboard PraNPC IndiHome",
            "ringkas": "A board for tracking late-stage collections effectiveness across IndiHome subscribers.",
            "peran": "Sole designer and developer",
            "masa": "2026 to present",
            "masalah": [
                "The late-stage collections team judged its performance from several separate "
                "sources. Field work orders lived in one place, contact outcomes in another, and "
                "payment confirmations in a third. Reconciling them was manual, repeated every "
                "day, and different people arrived at different numbers.",
                "Simple questions, such as where we stand today and who is falling behind, took "
                "a long time to answer, even though the answers were needed every morning.",
            ],
            "pendekatan": [
                "I brought the three sources into a single database and built a board that "
                "answers the team's daily questions directly: attainment against target, daily "
                "pace, comparison with the previous period, and rankings by region and by agent.",
                "I handled every layer myself, from ingestion and synchronisation, through schema "
                "and query design and the interface the team works in, to production deployment "
                "and monitoring.",
            ],
            "keputusan": [
                ("Metric definitions came first",
                 "Before writing a single query I fixed a canonical definition for every metric "
                 "and wrote it down. A metric defined differently on two pages misleads decisions "
                 "without anyone noticing, and that costs far more than a plain-looking screen."),
                ("The operating period is not the calendar month",
                 "The collections cycle does not stop at month end, so every pace and "
                 "period-over-period calculation has to follow the operating period. Reusing "
                 "calendar-month logic would put every number slightly out."),
                ("Heavy work belongs in the database",
                 "Aggregation happens as close to the data as possible, on indexes that are "
                 "actually used. The interface only receives finished results, so pages stay fast "
                 "as the data keeps growing."),
            ],
            "hasil": "Used daily by the operations team as the primary reference for collections performance.",
            "stack": ["Python", "MySQL", "SQL Server", "Vue 3", "PrimeVue", "Vite",
                      "Linux", "Nginx", "Git", "GitHub Actions"],
        },
    },
    {
        "slug": "pranpc-mobile",
        "varian": "corong",
        "id": {
            "nama": "Dashboard PraNPC Mobile",
            "ringkas": "Papan pantau penagihan untuk lini seluler pascabayar, dengan model periode dan kanal yang berbeda.",
            "peran": "Perancang dan pengembang tunggal",
            "masa": "2026",
            "masalah": [
                "Lini seluler membutuhkan papan pantau serupa, tetapi menyalin sistem yang sudah "
                "ada akan salah. Model periodenya berbeda, dan pelanggan disentuh lewat beberapa "
                "kanal sekaligus, bukan satu jalur tunggal.",
                "Karena satu pelanggan bisa dikunjungi sekaligus dihubungi, menjumlahkan angka "
                "per kanal secara mentah akan menghasilkan total yang melebihi jumlah pelanggan "
                "sebenarnya.",
            ],
            "pendekatan": [
                "Saya membangun sistem terpisah dengan model perhitungan sendiri, lalu menyatukan "
                "seluruh kanal sentuhan menjadi satu gambaran perjalanan pelanggan, dari "
                "dihubungi sampai membayar.",
                "Kanal disimpan sebagai penanda terpisah, bukan satu label tunggal, sehingga "
                "pelanggan yang disentuh lewat dua kanal tetap tercatat utuh di keduanya.",
            ],
            "keputusan": [
                ("Corong dibuat bersarang, bukan sekadar berjenjang",
                 "Sebagian pembayaran terjadi tanpa pelanggan pernah terkontak. Kalau tahap "
                 "berikutnya diisi total pembayaran, corongnya menjadi bohong. Yang lewat jalur "
                 "pintas ditampilkan terpisah agar keduanya jujur."),
                ("Kanal tidak boleh dijumlahkan mentah",
                 "Jumlah baris per kanal memang bisa melebihi jumlah pelanggan, dan itu disengaja. "
                 "Angka gabungan dihitung dari pelanggan unik, bukan dari penjumlahan kolom."),
            ],
            "hasil": "Menjadi rujukan capaian penagihan untuk lini seluler pascabayar.",
            "stack": ["Python", "MySQL", "Vue 3", "PrimeVue", "Vite"],
        },
        "en": {
            "nama": "Dashboard PraNPC Mobile",
            "ringkas": "A collections board for postpaid mobile, built around a different period model and a different set of channels.",
            "peran": "Sole designer and developer",
            "masa": "2026",
            "masalah": [
                "The mobile line needed a similar board, but copying the existing system would "
                "have been wrong. Its period model differs, and customers are reached through "
                "several channels at once rather than a single path.",
                "Because one customer can be visited and called in the same cycle, adding channel "
                "figures together produces a total larger than the customer base itself.",
            ],
            "pendekatan": [
                "I built a separate system with its own calculation model, then unified every "
                "touch channel into a single view of the customer journey, from first contact "
                "through to payment.",
                "Channels are stored as separate flags rather than one label, so a customer "
                "reached through two channels is fully recorded in both.",
            ],
            "keputusan": [
                ("The funnel is nested, not merely sequential",
                 "A share of payments happens without the customer ever being contacted. Filling "
                 "the next stage with total payments would make the funnel lie. Those who took the "
                 "shortcut are shown separately so both figures stay honest."),
                ("Channels must not be summed raw",
                 "Row counts per channel can exceed the customer base, and that is by design. "
                 "Combined figures are computed from unique customers, not by adding columns."),
            ],
            "hasil": "Serves as the reference for collections performance on the postpaid mobile line.",
            "stack": ["Python", "MySQL", "Vue 3", "PrimeVue", "Vite"],
        },
    },
    {
        "slug": "c3mr-indihome",
        "varian": "denyut",
        "id": {
            "nama": "Dashboard C3MR IndiHome",
            "ringkas": "Pemantauan efektivitas penagihan pada tahap paling awal, di atas basis pelanggan berskala jutaan baris.",
            "peran": "Pengembang",
            "masa": "2026",
            "masalah": [
                "Penagihan tahap awal berjalan pada basis pelanggan yang jauh lebih besar "
                "daripada tahap akhir. Skalanya membuat pemeriksaan manual mustahil, sementara "
                "kegagalan proses baru ketahuan ketika angkanya sudah terlihat aneh.",
            ],
            "pendekatan": [
                "Saya membangun pemantauan yang mengukur efektivitas penagihan pada masa First "
                "Reminder dan Second Reminder, dengan pemrosesan yang berjalan berkala dan "
                "peringatan otomatis ketika ada proses yang gagal.",
                "Bersama PraNPC, keduanya menutup rentang penagihan dari tahap paling awal "
                "sampai tahap akhir.",
            ],
            "keputusan": [
                ("Kegagalan harus berteriak, bukan menunggu ditemukan",
                 "Proses terjadwal yang gagal diam-diam jauh lebih berbahaya daripada proses yang "
                 "gagal berisik. Setiap kegagalan mengirim peringatan, sehingga masalah "
                 "ditangani sebelum sempat mengotori angka."),
                ("Hasil yang mahal dihitung dihitung sekali saja",
                 "Perhitungan berat disimpan dan dipakai ulang, bukan diulang setiap ada yang "
                 "membuka halaman. Pada skala jutaan baris, perbedaannya bukan soal kenyamanan "
                 "tetapi soal sanggup atau tidak."),
            ],
            "hasil": "Memberi gambaran efektivitas penagihan tahap awal tanpa pemeriksaan manual.",
            "stack": ["Python", "FastAPI", "MySQL", "Redis", "Nginx", "Linux"],
        },
        "en": {
            "nama": "Dashboard C3MR IndiHome",
            "ringkas": "Monitoring collections effectiveness at the earliest stage, across a subscriber base in the millions of rows.",
            "peran": "Developer",
            "masa": "2026",
            "masalah": [
                "Early-stage collections runs against a far larger base than the late stage. The "
                "scale makes manual checking impossible, while a failed job would only surface "
                "once the numbers already looked strange.",
            ],
            "pendekatan": [
                "I built monitoring that measures collections effectiveness during the First and "
                "Second Reminder windows, with scheduled processing and automated alerting "
                "whenever a job fails.",
                "Together with PraNPC, the two cover the collections span from the earliest stage "
                "through to the last.",
            ],
            "keputusan": [
                ("Failures should shout, not wait to be found",
                 "A scheduled job that fails quietly is far more dangerous than one that fails "
                 "loudly. Every failure raises an alert, so problems are handled before they can "
                 "contaminate the numbers."),
                ("Expensive results are computed once",
                 "Heavy calculations are stored and reused rather than recomputed on every page "
                 "load. At this scale that is not a matter of comfort but of whether it works at "
                 "all."),
            ],
            "hasil": "Gives a clear picture of early-stage collections effectiveness without manual checking.",
            "stack": ["Python", "FastAPI", "MySQL", "Redis", "Nginx", "Linux"],
        },
    },
    {
        "slug": "tiketing-ordering",
        "varian": "antre",
        "id": {
            "nama": "Dashboard Tiketing dan Ordering All Channel",
            "ringkas": "Tiket layanan dan pemesanan dari seluruh kanal dalam satu tampilan.",
            "peran": "Pengembang",
            "masa": "2025 sampai 2026",
            "masalah": [
                "Tiket dan pemesanan masuk dari beberapa kanal yang berbeda, masing-masing dengan "
                "bentuk data sendiri. Selama tidak disatukan, tidak ada yang bisa melihat beban "
                "kerja sebenarnya, apalagi membandingkan kanal satu dengan lainnya.",
            ],
            "pendekatan": [
                "Saya menyatukan seluruh kanal ke dalam satu papan pantau, dengan pipeline "
                "pengambilan data yang berjalan terjadwal sehingga isinya selalu segar tanpa "
                "perlu ada yang mengunggah manual.",
                "Karena isinya menyangkut data layanan, aksesnya dilindungi autentikasi dua "
                "faktor.",
            ],
            "keputusan": [
                ("Bentuk data yang berbeda diseragamkan di pintu masuk",
                 "Setiap kanal punya format sendiri, dan perbedaannya diselesaikan saat data "
                 "masuk, bukan dibiarkan menyebar ke seluruh kueri. Satu tempat yang rumit jauh "
                 "lebih mudah dirawat daripada rumit di banyak tempat."),
                ("Impor dibuat aman diulang",
                 "Berkas yang sama boleh diimpor berkali-kali tanpa menggandakan baris. Tanpa "
                 "sifat ini, satu kesalahan kecil akan meninggalkan data kotor yang sulit "
                 "ditelusuri."),
            ],
            "hasil": "Beban tiket dan pemesanan seluruh kanal terlihat dalam satu tempat.",
            "stack": ["Python", "MySQL", "Docker", "Git", "GitHub Actions"],
        },
        "en": {
            "nama": "Dashboard Tiketing dan Ordering All Channel",
            "ringkas": "Service tickets and orders from every channel on a single board.",
            "peran": "Developer",
            "masa": "2025 to 2026",
            "masalah": [
                "Tickets and orders arrive from several channels, each with its own data shape. "
                "Until they were unified, nobody could see the real workload, let alone compare "
                "one channel against another.",
            ],
            "pendekatan": [
                "I unified every channel onto one board, with a scheduled ingestion pipeline so "
                "the content stays current without anyone uploading anything by hand.",
                "Because the content concerns service data, access is protected with two-factor "
                "authentication.",
            ],
            "keputusan": [
                ("Differing data shapes are normalised at the door",
                 "Every channel has its own format, and those differences are resolved on the way "
                 "in rather than allowed to spread through every query. One complicated place is "
                 "far easier to maintain than complications everywhere."),
                ("Imports are safe to repeat",
                 "The same file can be imported many times without duplicating rows. Without that "
                 "property, one small mistake leaves dirty data that is hard to trace."),
            ],
            "hasil": "Ticket and order load across all channels is visible in one place.",
            "stack": ["Python", "MySQL", "Docker", "Git", "GitHub Actions"],
        },
    },
    {
        "slug": "sentimen-media-sosial",
        "varian": "sebaran",
        "id": {
            "nama": "Dashboard Analytics Trend Sentimen Media Sosial",
            "ringkas": "Memantau tren dan sentimen percakapan di media sosial.",
            "peran": "Pengembang",
            "masa": "2026",
            "masalah": [
                "Percakapan tentang layanan berlangsung terus di media sosial, jauh lebih cepat "
                "daripada yang bisa diikuti secara manual. Tanpa rangkuman, yang tertangkap hanya "
                "kejadian yang kebetulan terlihat.",
            ],
            "pendekatan": [
                "Saya membangun papan pantau yang merangkum tren dan sentimen percakapan menjadi "
                "gambaran yang bisa dibaca cepat oleh tim.",
            ],
            "keputusan": [],
            "hasil": "Tren percakapan terbaca tanpa harus mengikuti linimasa satu per satu.",
            "stack": ["Python", "MySQL", "Vue 3"],
        },
        "en": {
            "nama": "Dashboard Analytics Trend Sentimen Media Sosial",
            "ringkas": "Tracking conversation trends and sentiment across social media.",
            "peran": "Developer",
            "masa": "2026",
            "masalah": [
                "Conversation about the service runs continuously on social media, far faster "
                "than anyone can follow by hand. Without a summary, only whatever happens to be "
                "noticed gets caught.",
            ],
            "pendekatan": [
                "I built a board that summarises conversation trends and sentiment into something "
                "the team can read at a glance.",
            ],
            "keputusan": [],
            "hasil": "Conversation trends are legible without following timelines one by one.",
            "stack": ["Python", "MySQL", "Vue 3"],
        },
    },
]

LOGO = {
    "Python": "python", "JavaScript": "javascript", "PHP": "php", "Java": "java",
    "R": "r", "HTML": "html", "CSS": "css", "MySQL": "mysql",
    "PostgreSQL": "postgresql", "MongoDB": "mongodb", "Redis": "redis",
    "DBeaver": "dbeaver", "phpMyAdmin": "phpmyadmin", "XAMPP": "xampp",
    "Laragon": "laragon", "FastAPI": "fastapi", "Express": "express",
    "Node.js": "nodejs", "Laravel": "laravel", "Vue 3": "vue",
    "PrimeVue": "primevue", "Vite": "vite", "React": "react", "Next.js": "nextjs",
    "Bootstrap": "bootstrap", "Android": "android", "Linux": "linux",
    "Nginx": "nginx", "Docker": "docker", "Git": "git",
    "GitHub Actions": "githubactions", "Uptime Kuma": "uptimekuma",
}

TEKS = {
    "id": {
        "kembali": "Kembali ke profil", "peran": "Peran", "masa": "Masa",
        "masalah": "Masalah", "pendekatan": "Pendekatan",
        "keputusan": "Keputusan teknis", "hasil": "Hasil",
        "stack": "Teknologi", "lain": "Karya lainnya",
        "catatan": "Ilustrasi di atas adalah gambaran tata letak, bukan tangkapan layar. "
                   "Sistem ini memuat data pelanggan sehingga tampilan aslinya tidak dipublikasikan.",
        "beranda": "/id/", "akar": "karya",
    },
    "en": {
        "kembali": "Back to profile", "peran": "Role", "masa": "Period",
        "masalah": "Problem", "pendekatan": "Approach",
        "keputusan": "Technical decisions", "hasil": "Outcome",
        "stack": "Technology", "lain": "Other work",
        "catatan": "The illustration above is a layout sketch, not a screenshot. This system "
                   "holds customer data, so the real interface is not published.",
        "beranda": "/", "akar": "work",
    },
}


# ---------------------------------------------------------------- ilustrasi

def ilustrasi(varian: str) -> str:
    """Sketsa tata letak dashboard. Murni bentuk, tanpa data."""
    kotak = ('<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
             'fill="{f}" opacity="{o}"/>')
    bagian = [
        '<svg viewBox="0 0 560 300" role="img" aria-label="Sketsa tata letak dashboard" '
        'xmlns="http://www.w3.org/2000/svg" class="sketsa">',
        kotak.format(x=0, y=0, w=560, h=300, r=12, f="var(--surface)", o=1),
        kotak.format(x=0, y=0, w=560, h=34, r=12, f="var(--border)", o=.55),
        kotak.format(x=16, y=13, w=86, h=8, r=4, f="var(--accent)", o=.85),
        kotak.format(x=470, y=12, w=74, h=10, r=5, f="var(--text-mute)", o=.3),
    ]
    for i in range(4):
        x = 16 + i * 133
        bagian += [
            kotak.format(x=x, y=50, w=117, h=52, r=8, f="var(--bg-elevated)", o=1),
            kotak.format(x=x + 12, y=62, w=44, h=6, r=3, f="var(--text-mute)", o=.45),
            kotak.format(x=x + 12, y=76, w=66, h=13, r=4, f="var(--accent)", o=.75),
        ]

    if varian == "papan":
        tinggi = [58, 74, 44, 88, 66, 96, 52]
        for i, t in enumerate(tinggi):
            bagian.append(kotak.format(x=26 + i * 42, y=248 - t, w=24, h=t, r=5,
                                       f="var(--accent)", o=.30 + i * .07))
        bagian.append(kotak.format(x=336, y=120, w=208, h=128, r=8, f="var(--bg-elevated)", o=1))
        for i in range(5):
            bagian += [kotak.format(x=350, y=136 + i * 22, w=96, h=7, r=3, f="var(--text-mute)", o=.4),
                       kotak.format(x=470, y=136 + i * 22, w=58, h=7, r=3, f="var(--text-mute)", o=.22)]
    elif varian == "corong":
        for i, w in enumerate([420, 330, 240, 150]):
            bagian.append(kotak.format(x=(560 - w) // 2, y=124 + i * 34, w=w, h=24, r=6,
                                       f="var(--accent)", o=.55 - i * .1))
    elif varian == "denyut":
        bagian.append('<polyline points="24,220 84,196 144,206 204,150 264,172 324,128 384,146 444,110 528,132" '
                      'fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" '
                      'stroke-linejoin="round" opacity=".8"/>')
        bagian.append(kotak.format(x=16, y=118, w=528, h=130, r=8, f="var(--bg-elevated)", o=.55))
        for i in range(9):
            bagian.append(f'<circle cx="{24 + i * 63}" cy="{[220,196,206,150,172,128,146,110,132][i]}" '
                          'r="4" fill="var(--accent)"/>')
    elif varian == "antre":
        for i in range(6):
            bagian += [kotak.format(x=16, y=120 + i * 22, w=10, h=10, r=3, f="var(--accent)", o=.7 - i * .09),
                       kotak.format(x=36, y=122, w=0, h=0, r=0, f="none", o=0),
                       kotak.format(x=36, y=123 + i * 22, w=300 - i * 26, h=7, r=3, f="var(--text-mute)", o=.38),
                       kotak.format(x=470, y=123 + i * 22, w=74, h=7, r=3, f="var(--text-mute)", o=.2)]
    else:  # sebaran
        titik = [(70, 200, 9), (128, 172, 14), (186, 208, 7), (244, 150, 18),
                 (302, 186, 11), (360, 140, 22), (418, 178, 9), (476, 158, 13)]
        for cx, cy, r in titik:
            bagian.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--accent)" opacity=".45"/>')
        bagian.append(kotak.format(x=16, y=254, w=528, h=2, r=1, f="var(--border-strong)", o=1))

    bagian.append("</svg>")
    return "\n        ".join(bagian)


# ---------------------------------------------------------------- rakit

def chip(nama: str) -> str:
    berkas = LOGO.get(nama)
    ikon = (f'<img src="/assets/logos/{berkas}.svg" alt="" width="15" height="15" '
            f'loading="lazy" aria-hidden="true">') if berkas else ""
    return f'<span class="chip">{ikon}{H.escape(nama)}</span>'


def halaman(k: dict, bahasa: str) -> str:
    d = k[bahasa]
    t = TEKS[bahasa]
    url = f"{SITUS}/{t['akar']}/{k['slug']}/"
    lain = [x for x in KARYA if x["slug"] != k["slug"]]

    skema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": d["nama"],
        "description": d["ringkas"],
        "url": url,
        "inLanguage": "id-ID" if bahasa == "id" else "en",
        "author": {
            "@type": "Person",
            "name": "Ruqi Fahmi Sadad",
            "url": SITUS + "/",
        },
        "keywords": ", ".join(d["stack"]),
    }
    remah = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ruqi Fahmi Sadad",
             "item": SITUS + t["beranda"]},
            {"@type": "ListItem", "position": 2, "name": d["nama"], "item": url},
        ],
    }

    def paragraf(baris):
        return "\n".join(f"    <p>{H.escape(b)}</p>" for b in baris)

    keputusan = ""
    if d["keputusan"]:
        isi = "\n".join(
            f'    <div class="item">\n      <h3>{H.escape(j)}</h3>\n      <p>{H.escape(p)}</p>\n    </div>'
            for j, p in d["keputusan"])
        keputusan = f'\n  <section id="keputusan">\n    <h2>{t["keputusan"]}</h2>\n{isi}\n  </section>\n'

    kartu_lain = "\n".join(
        f'    <a class="karya-lain" href="/{t["akar"]}/{x["slug"]}/">'
        f'<strong>{H.escape(x[bahasa]["nama"])}</strong>'
        f'<span>{H.escape(x[bahasa]["ringkas"])}</span></a>'
        for x in lain)

    return f"""<!DOCTYPE html>
<html lang="{'id' if bahasa == 'id' else 'en'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(d['nama'])} — Ruqi Fahmi Sadad</title>
<meta name="description" content="{H.escape(d['ringkas'])} Dibangun oleh Ruqi Fahmi Sadad.">
<meta name="author" content="Ruqi Fahmi Sadad">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/assets/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="theme-color" content="#b3121f">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Ruqi Fahmi Sadad">
<meta property="og:title" content="{H.escape(d['nama'])} — Ruqi Fahmi Sadad">
<meta property="og:description" content="{H.escape(d['ringkas'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITUS}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ruqi Fahmi Sadad, Data Analyst dan IT Development">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITUS}/assets/og-image.png">
<script type="application/ld+json">
{json.dumps(skema, ensure_ascii=False, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(remah, ensure_ascii=False, indent=2)}
</script>
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<div class="wrap" id="top">

  <nav class="topbar">
    <a class="brand" href="{t['beranda']}">Ruqi Fahmi Sadad</a>
    <div class="navlinks"></div>
    <a class="pill" href="{'/work/' + k['slug'] + '/' if bahasa == 'id' else '/karya/' + k['slug'] + '/'}"
       hreflang="{'en' if bahasa == 'id' else 'id'}">{'EN' if bahasa == 'id' else 'ID'}</a>
    <button class="pill" id="theme" type="button" aria-label="Ganti tema">☽</button>
  </nav>

  <header class="hero">
    <a class="kembali" href="{t['beranda']}">{t['kembali']}</a>
    <h1>{H.escape(d['nama'])}</h1>
    <p class="lead">{H.escape(d['ringkas'])}</p>
    <p class="place">{t['peran']}: {H.escape(d['peran'])} &nbsp;·&nbsp; {t['masa']}: {H.escape(d['masa'])}</p>
  </header>

  <figure class="figur">
    {ilustrasi(k['varian'])}
    <figcaption>{t['catatan']}</figcaption>
  </figure>

  <section id="masalah">
    <h2>{t['masalah']}</h2>
{paragraf(d['masalah'])}
  </section>

  <section id="pendekatan">
    <h2>{t['pendekatan']}</h2>
{paragraf(d['pendekatan'])}
  </section>
{keputusan}
  <section id="hasil">
    <h2>{t['hasil']}</h2>
    <p>{H.escape(d['hasil'])}</p>
  </section>

  <section id="stack">
    <h2>{t['stack']}</h2>
    <div class="chips">{''.join(chip(s) for s in d['stack'])}</div>
  </section>

  <section id="lain">
    <h2>{t['lain']}</h2>
{kartu_lain}
  </section>

  <footer>
    <p><a href="{t['beranda']}">Ruqi Fahmi Sadad</a> · <a href="https://github.com/ruqi-fahmi">github.com/ruqi-fahmi</a></p>
  </footer>

</div>
<script src="/assets/app.js" defer></script>
</body>
</html>
"""


def main() -> None:
    dibuat = []
    for k in KARYA:
        for bahasa in ("id", "en"):
            akar = "karya" if bahasa == "id" else "work"
            tujuan = AKAR / akar / k["slug"] / "index.html"
            tujuan.parent.mkdir(parents=True, exist_ok=True)
            tujuan.write_text(halaman(k, bahasa), encoding="utf-8")
            dibuat.append(tujuan.relative_to(AKAR).as_posix())

    for p in dibuat:
        print("  ", p)
    print(f"\n{len(dibuat)} halaman dibangun.")


if __name__ == "__main__":
    main()
