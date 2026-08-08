# Situs profil Ruqi Fahmi Sadad

Tujuan situs ini satu: kalau orang mencari **"Ruqi Fahmi Sadad"** di Google, halaman inilah yang muncul di urutan atas — bukan dokumen lama yang tidak kamu kendalikan.

---

## ISI DULU SEBELUM DIPUBLIKASIKAN

Ada beberapa bagian yang sengaja saya kosongkan supaya tidak ada informasi karangan di situs atas namamu. Cari tanda `[[...]]` di `index.html` dan `en/index.html`, lalu ganti:

| Penanda | Isi dengan |
|---|---|
| `[[EMAIL]]` | Email yang siap kamu tampilkan publik. Pertimbangkan email khusus, bukan yang utama |
| `[[NAMA_LOMBA_ANDALAS]]` | Nama resmi lomba nasional di Universitas Andalas |
| `[[TAHUN]]` | Tahun lomba tersebut |
| `[[PROGRAM_STUDI]]` | Program studi di Universitas Mulawarman |
| `[[TAHUN_LULUS]]` | Tahun lulus atau rentang kuliah |

Kalau ada bagian yang tidak ingin ditampilkan, hapus saja seluruh bloknya — jangan dibiarkan berisi `[[...]]`.

**Periksa ulang isinya.** Deskripsi pekerjaan sengaja saya tulis di tingkat kemampuan dan dampak, tanpa struktur basis data, alamat server, maupun angka internal. Tetap baca sekali lagi dengan kacamata "apakah ini aman dibaca atasan dan klien", karena nama Infomedia dan Telkomsel disebut terbuka atas permintaanmu.

---

## Cara mempublikasikan

1. **Buat repo di GitHub** dengan nama **persis** `ruqi-fahmi.github.io`, set **Public**.
   Nama repo harus sama dengan username diikuti `.github.io`, itu syarat GitHub Pages.

2. **Push isi folder ini:**

   ```bash
   cd E:/ruqi-fahmi.github.io
   git init -b main
   git add -A
   git commit -m "feat: situs profil"
   git remote add origin https://github.com/ruqi-fahmi/ruqi-fahmi.github.io.git
   git push -u origin main
   ```

3. **Aktifkan Pages** — Settings → Pages → Source: `main`, folder `/ (root)`.
   Tunggu 1–3 menit, situs hidup di `https://ruqi-fahmi.github.io/`.

4. **Daftarkan ke Google Search Console** (`search.google.com/search-console`).
   Tambahkan properti URL prefix `https://ruqi-fahmi.github.io/`, verifikasi, lalu kirim `sitemap.xml`. Tanpa langkah ini Google tetap menemukan situsmu, tapi jauh lebih lama.

5. **Minta pengindeksan langsung** — di Search Console, tempel URL-nya di kolom atas, lalu klik *Request Indexing*. Biasanya masuk indeks dalam hitungan hari.

---

## Setelah terbit — yang menentukan peringkat

Google menilai relevansi lewat **tautan dan konsistensi**, bukan cuma isi halaman. Jadi:

- Pasang `https://ruqi-fahmi.github.io/` di **bio LinkedIn**, **bio GitHub**, dan semua profil lain yang kamu punya. Ini sinyal terkuat yang bisa kamu kendalikan sendiri.
- **Tulis nama lengkap yang sama persis** di semua profil — "Ruqi Fahmi Sadad", bukan campur "Ruqi Fahmi" di satu tempat dan "R. F. Sadad" di tempat lain. Konsistensi membantu Google menyimpulkan semuanya orang yang sama.
- Isi **profil README GitHub** (lihat `profile-README.md` di folder ini).
- Perbarui situs sesekali. Halaman yang tidak pernah berubah pelan-pelan turun.

**Perkiraan waktu yang realistis:** masuk indeks beberapa hari, mulai naik peringkat 1–3 bulan, stabil di posisi atas sekitar 3–6 bulan. Ini pekerjaan jangka panjang, bukan sekali jadi.
