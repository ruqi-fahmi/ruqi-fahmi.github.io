/**
 * Sumber tunggal untuk seluruh halaman karya, dua bahasa.
 *
 * Halaman /work/<slug>/ dan /karya/<slug>/ dibangun dari berkas ini. Menambah
 * karya baru cukup menambah satu entri di sini, tidak perlu menyentuh HTML.
 */

export type Locale = "en" | "id";

export interface Decision {
  title: string;
  body: string;
}

export interface WorkContent {
  name: string;
  summary: string;
  role: string;
  period: string;
  problem: string[];
  approach: string[];
  decisions: Decision[];
  outcome: string;
  stack: string[];
}

export interface Work {
  slug: string;
  /** Watak sketsa tata letak yang digambar untuk halaman ini. */
  variant: "papan" | "corong" | "denyut" | "antre" | "sebaran";
  en: WorkContent;
  id: WorkContent;
}

export const works: Work[] = [
  {
    "slug": "pranpc-indihome",
    "variant": "papan",
    "en": {
      "name": "Dashboard PraNPC IndiHome",
      "summary": "A board for tracking late-stage collections effectiveness across IndiHome subscribers.",
      "role": "Sole designer and developer",
      "period": "2026 to present",
      "problem": [
        "The late-stage collections team judged its performance from several separate sources. Field work orders lived in one place, contact outcomes in another, and payment confirmations in a third. Reconciling them was manual, repeated every day, and different people arrived at different numbers.",
        "Simple questions, such as where we stand today and who is falling behind, took a long time to answer, even though the answers were needed every morning."
      ],
      "approach": [
        "I brought the three sources into a single database and built a board that answers the team's daily questions directly: attainment against target, daily pace, comparison with the previous period, and rankings by region and by agent.",
        "I handled every layer myself, from ingestion and synchronisation, through schema and query design and the interface the team works in, to production deployment and monitoring."
      ],
      "decisions": [
        {
          "title": "Metric definitions came first",
          "body": "Before writing a single query I fixed a canonical definition for every metric and wrote it down. A metric defined differently on two pages misleads decisions without anyone noticing, and that costs far more than a plain-looking screen."
        },
        {
          "title": "The operating period is not the calendar month",
          "body": "The collections cycle does not stop at month end, so every pace and period-over-period calculation has to follow the operating period. Reusing calendar-month logic would put every number slightly out."
        },
        {
          "title": "Heavy work belongs in the database",
          "body": "Aggregation happens as close to the data as possible, on indexes that are actually used. The interface only receives finished results, so pages stay fast as the data keeps growing."
        }
      ],
      "outcome": "Used daily by the operations team as the primary reference for collections performance.",
      "stack": [
        "Python",
        "MySQL",
        "SQL Server",
        "Vue 3",
        "PrimeVue",
        "Vite",
        "Linux",
        "Nginx",
        "Git",
        "GitHub Actions"
      ]
    },
    "id": {
      "name": "Dashboard PraNPC IndiHome",
      "summary": "Papan pantau efektivitas penagihan tahap akhir untuk pelanggan IndiHome.",
      "role": "Perancang dan pengembang tunggal",
      "period": "2026 sampai sekarang",
      "problem": [
        "Tim penagihan tahap akhir menilai capaian dari beberapa sumber yang terpisah. Data pekerjaan lapangan ada di satu tempat, hasil kontak di tempat lain, dan konfirmasi pembayaran di tempat ketiga. Menyatukannya dikerjakan manual, berulang setiap hari, dan hasilnya sering berbeda antar orang.",
        "Akibatnya pertanyaan sederhana seperti berapa capaian hari ini dan siapa yang tertinggal justru butuh waktu lama untuk dijawab, padahal jawabannya dibutuhkan setiap pagi."
      ],
      "approach": [
        "Saya menyatukan ketiga sumber itu ke dalam satu basis data, lalu membangun papan pantau yang menjawab pertanyaan harian tim secara langsung: capaian terhadap target, laju harian, perbandingan dengan periode sebelumnya, sampai peringkat per wilayah dan per petugas.",
        "Seluruh lapisannya saya kerjakan sendiri, mulai dari pengambilan dan sinkronisasi data, perancangan skema dan kueri, antarmuka yang dipakai tim, sampai penerapan di server produksi berikut pemantauannya."
      ],
      "decisions": [
        {
          "title": "Definisi metrik dibakukan lebih dulu",
          "body": "Sebelum menulis kueri, saya menetapkan definisi baku untuk setiap metrik dan mendokumentasikannya. Satu metrik yang didefinisikan berbeda antar halaman akan menyesatkan keputusan tanpa ada yang menyadari, dan kesalahan seperti itu jauh lebih mahal daripada tampilan yang kurang menarik."
        },
        {
          "title": "Periode operasional tidak sama dengan bulan kalender",
          "body": "Siklus penagihan tidak berhenti di akhir bulan, sehingga seluruh perhitungan laju dan perbandingan antar periode harus mengikuti definisi periode operasional. Menyalin logika bulan kalender akan membuat setiap angka meleset."
        },
        {
          "title": "Perhitungan berat dipindahkan ke basis data",
          "body": "Agregasi dilakukan sedekat mungkin dengan datanya, dengan indeks yang memang dipakai. Antarmuka hanya menerima hasil yang sudah siap, sehingga halaman tetap ringan meski data terus bertambah."
        }
      ],
      "outcome": "Dipakai harian oleh tim operasional sebagai rujukan utama capaian penagihan.",
      "stack": [
        "Python",
        "MySQL",
        "SQL Server",
        "Vue 3",
        "PrimeVue",
        "Vite",
        "Linux",
        "Nginx",
        "Git",
        "GitHub Actions"
      ]
    }
  },
  {
    "slug": "pranpc-mobile",
    "variant": "corong",
    "en": {
      "name": "Dashboard PraNPC Mobile",
      "summary": "A collections board for postpaid mobile, built around a different period model and a different set of channels.",
      "role": "Sole designer and developer",
      "period": "2026",
      "problem": [
        "The mobile line needed a similar board, but copying the existing system would have been wrong. Its period model differs, and customers are reached through several channels at once rather than a single path.",
        "Because one customer can be visited and called in the same cycle, adding channel figures together produces a total larger than the customer base itself."
      ],
      "approach": [
        "I built a separate system with its own calculation model, then unified every touch channel into a single view of the customer journey, from first contact through to payment.",
        "Channels are stored as separate flags rather than one label, so a customer reached through two channels is fully recorded in both."
      ],
      "decisions": [
        {
          "title": "The funnel is nested, not merely sequential",
          "body": "A share of payments happens without the customer ever being contacted. Filling the next stage with total payments would make the funnel lie. Those who took the shortcut are shown separately so both figures stay honest."
        },
        {
          "title": "Channels must not be summed raw",
          "body": "Row counts per channel can exceed the customer base, and that is by design. Combined figures are computed from unique customers, not by adding columns."
        }
      ],
      "outcome": "Serves as the reference for collections performance on the postpaid mobile line.",
      "stack": [
        "Python",
        "MySQL",
        "Vue 3",
        "PrimeVue",
        "Vite"
      ]
    },
    "id": {
      "name": "Dashboard PraNPC Mobile",
      "summary": "Papan pantau penagihan untuk lini seluler pascabayar, dengan model periode dan kanal yang berbeda.",
      "role": "Perancang dan pengembang tunggal",
      "period": "2026",
      "problem": [
        "Lini seluler membutuhkan papan pantau serupa, tetapi menyalin sistem yang sudah ada akan salah. Model periodenya berbeda, dan pelanggan disentuh lewat beberapa kanal sekaligus, bukan satu jalur tunggal.",
        "Karena satu pelanggan bisa dikunjungi sekaligus dihubungi, menjumlahkan angka per kanal secara mentah akan menghasilkan total yang melebihi jumlah pelanggan sebenarnya."
      ],
      "approach": [
        "Saya membangun sistem terpisah dengan model perhitungan sendiri, lalu menyatukan seluruh kanal sentuhan menjadi satu gambaran perjalanan pelanggan, dari dihubungi sampai membayar.",
        "Kanal disimpan sebagai penanda terpisah, bukan satu label tunggal, sehingga pelanggan yang disentuh lewat dua kanal tetap tercatat utuh di keduanya."
      ],
      "decisions": [
        {
          "title": "Corong dibuat bersarang, bukan sekadar berjenjang",
          "body": "Sebagian pembayaran terjadi tanpa pelanggan pernah terkontak. Kalau tahap berikutnya diisi total pembayaran, corongnya menjadi bohong. Yang lewat jalur pintas ditampilkan terpisah agar keduanya jujur."
        },
        {
          "title": "Kanal tidak boleh dijumlahkan mentah",
          "body": "Jumlah baris per kanal memang bisa melebihi jumlah pelanggan, dan itu disengaja. Angka gabungan dihitung dari pelanggan unik, bukan dari penjumlahan kolom."
        }
      ],
      "outcome": "Menjadi rujukan capaian penagihan untuk lini seluler pascabayar.",
      "stack": [
        "Python",
        "MySQL",
        "Vue 3",
        "PrimeVue",
        "Vite"
      ]
    }
  },
  {
    "slug": "c3mr-indihome",
    "variant": "denyut",
    "en": {
      "name": "Dashboard C3MR IndiHome",
      "summary": "Monitoring collections effectiveness at the earliest stage, across a subscriber base in the millions of rows.",
      "role": "Developer",
      "period": "2026",
      "problem": [
        "Early-stage collections runs against a far larger base than the late stage. The scale makes manual checking impossible, while a failed job would only surface once the numbers already looked strange."
      ],
      "approach": [
        "I built monitoring that measures collections effectiveness during the First and Second Reminder windows, with scheduled processing and automated alerting whenever a job fails.",
        "Together with PraNPC, the two cover the collections span from the earliest stage through to the last."
      ],
      "decisions": [
        {
          "title": "Failures should shout, not wait to be found",
          "body": "A scheduled job that fails quietly is far more dangerous than one that fails loudly. Every failure raises an alert, so problems are handled before they can contaminate the numbers."
        },
        {
          "title": "Expensive results are computed once",
          "body": "Heavy calculations are stored and reused rather than recomputed on every page load. At this scale that is not a matter of comfort but of whether it works at all."
        }
      ],
      "outcome": "Gives a clear picture of early-stage collections effectiveness without manual checking.",
      "stack": [
        "Python",
        "FastAPI",
        "MySQL",
        "Redis",
        "Nginx",
        "Linux"
      ]
    },
    "id": {
      "name": "Dashboard C3MR IndiHome",
      "summary": "Pemantauan efektivitas penagihan pada tahap paling awal, di atas basis pelanggan berskala jutaan baris.",
      "role": "Pengembang",
      "period": "2026",
      "problem": [
        "Penagihan tahap awal berjalan pada basis pelanggan yang jauh lebih besar daripada tahap akhir. Skalanya membuat pemeriksaan manual mustahil, sementara kegagalan proses baru ketahuan ketika angkanya sudah terlihat aneh."
      ],
      "approach": [
        "Saya membangun pemantauan yang mengukur efektivitas penagihan pada masa First Reminder dan Second Reminder, dengan pemrosesan yang berjalan berkala dan peringatan otomatis ketika ada proses yang gagal.",
        "Bersama PraNPC, keduanya menutup rentang penagihan dari tahap paling awal sampai tahap akhir."
      ],
      "decisions": [
        {
          "title": "Kegagalan harus berteriak, bukan menunggu ditemukan",
          "body": "Proses terjadwal yang gagal diam-diam jauh lebih berbahaya daripada proses yang gagal berisik. Setiap kegagalan mengirim peringatan, sehingga masalah ditangani sebelum sempat mengotori angka."
        },
        {
          "title": "Hasil yang mahal dihitung dihitung sekali saja",
          "body": "Perhitungan berat disimpan dan dipakai ulang, bukan diulang setiap ada yang membuka halaman. Pada skala jutaan baris, perbedaannya bukan soal kenyamanan tetapi soal sanggup atau tidak."
        }
      ],
      "outcome": "Memberi gambaran efektivitas penagihan tahap awal tanpa pemeriksaan manual.",
      "stack": [
        "Python",
        "FastAPI",
        "MySQL",
        "Redis",
        "Nginx",
        "Linux"
      ]
    }
  },
  {
    "slug": "tiketing-ordering",
    "variant": "antre",
    "en": {
      "name": "Dashboard Tiketing dan Ordering All Channel",
      "summary": "Service tickets and orders from every channel on a single board.",
      "role": "Developer",
      "period": "2025 to 2026",
      "problem": [
        "Tickets and orders arrive from several channels, each with its own data shape. Until they were unified, nobody could see the real workload, let alone compare one channel against another."
      ],
      "approach": [
        "I unified every channel onto one board, with a scheduled ingestion pipeline so the content stays current without anyone uploading anything by hand.",
        "Because the content concerns service data, access is protected with two-factor authentication."
      ],
      "decisions": [
        {
          "title": "Differing data shapes are normalised at the door",
          "body": "Every channel has its own format, and those differences are resolved on the way in rather than allowed to spread through every query. One complicated place is far easier to maintain than complications everywhere."
        },
        {
          "title": "Imports are safe to repeat",
          "body": "The same file can be imported many times without duplicating rows. Without that property, one small mistake leaves dirty data that is hard to trace."
        }
      ],
      "outcome": "Ticket and order load across all channels is visible in one place.",
      "stack": [
        "Python",
        "MySQL",
        "Docker",
        "Git",
        "GitHub Actions"
      ]
    },
    "id": {
      "name": "Dashboard Tiketing dan Ordering All Channel",
      "summary": "Tiket layanan dan pemesanan dari seluruh kanal dalam satu tampilan.",
      "role": "Pengembang",
      "period": "2025 sampai 2026",
      "problem": [
        "Tiket dan pemesanan masuk dari beberapa kanal yang berbeda, masing-masing dengan bentuk data sendiri. Selama tidak disatukan, tidak ada yang bisa melihat beban kerja sebenarnya, apalagi membandingkan kanal satu dengan lainnya."
      ],
      "approach": [
        "Saya menyatukan seluruh kanal ke dalam satu papan pantau, dengan pipeline pengambilan data yang berjalan terjadwal sehingga isinya selalu segar tanpa perlu ada yang mengunggah manual.",
        "Karena isinya menyangkut data layanan, aksesnya dilindungi autentikasi dua faktor."
      ],
      "decisions": [
        {
          "title": "Bentuk data yang berbeda diseragamkan di pintu masuk",
          "body": "Setiap kanal punya format sendiri, dan perbedaannya diselesaikan saat data masuk, bukan dibiarkan menyebar ke seluruh kueri. Satu tempat yang rumit jauh lebih mudah dirawat daripada rumit di banyak tempat."
        },
        {
          "title": "Impor dibuat aman diulang",
          "body": "Berkas yang sama boleh diimpor berkali-kali tanpa menggandakan baris. Tanpa sifat ini, satu kesalahan kecil akan meninggalkan data kotor yang sulit ditelusuri."
        }
      ],
      "outcome": "Beban tiket dan pemesanan seluruh kanal terlihat dalam satu tempat.",
      "stack": [
        "Python",
        "MySQL",
        "Docker",
        "Git",
        "GitHub Actions"
      ]
    }
  },
  {
    "slug": "sentimen-media-sosial",
    "variant": "sebaran",
    "en": {
      "name": "Dashboard Analytics Trend Sentimen Media Sosial",
      "summary": "Tracking conversation trends and sentiment across social media.",
      "role": "Developer",
      "period": "2026",
      "problem": [
        "Conversation about the service runs continuously on social media, far faster than anyone can follow by hand. Without a summary, only whatever happens to be noticed gets caught."
      ],
      "approach": [
        "I built a board that summarises conversation trends and sentiment into something the team can read at a glance."
      ],
      "decisions": [],
      "outcome": "Conversation trends are legible without following timelines one by one.",
      "stack": [
        "Python",
        "MySQL",
        "Vue 3"
      ]
    },
    "id": {
      "name": "Dashboard Analytics Trend Sentimen Media Sosial",
      "summary": "Memantau tren dan sentimen percakapan di media sosial.",
      "role": "Pengembang",
      "period": "2026",
      "problem": [
        "Percakapan tentang layanan berlangsung terus di media sosial, jauh lebih cepat daripada yang bisa diikuti secara manual. Tanpa rangkuman, yang tertangkap hanya kejadian yang kebetulan terlihat."
      ],
      "approach": [
        "Saya membangun papan pantau yang merangkum tren dan sentimen percakapan menjadi gambaran yang bisa dibaca cepat oleh tim."
      ],
      "decisions": [],
      "outcome": "Tren percakapan terbaca tanpa harus mengikuti linimasa satu per satu.",
      "stack": [
        "Python",
        "MySQL",
        "Vue 3"
      ]
    }
  }
];

export const bySlug = (slug: string): Work | undefined =>
  works.find((w) => w.slug === slug);
