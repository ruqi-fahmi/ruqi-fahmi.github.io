// @ts-check
import { defineConfig } from "astro/config";
import vue from "@astrojs/vue";

// Situs ini sengaja dibangun statis. Astro dipakai untuk komponen, layout, dan
// alur build, tetapi keluarannya tetap HTML siap baca. Alasannya bukan selera:
// tujuan utama situs ini adalah peringkat pencarian nama pemiliknya, dan halaman
// yang harus dirender JavaScript lebih lambat serta lebih rapuh diindeks.
export default defineConfig({
  site: "https://ruqi-fahmi.github.io",

  // Menghasilkan /work/slug/index.html, sehingga alamatnya persis sama dengan
  // susunan sebelumnya. Alamat lama tidak boleh berubah karena sudah terindeks.
  build: { format: "directory" },
  trailingSlash: "always",

  integrations: [vue()],

  // sitemap.xml ditulis tangan di public/ agar pasangan hreflang antara
  // /work/<slug>/ dan /karya/<slug>/ tetap terkendali. Susunan alamat kita
  // tidak mengikuti pola awalan bahasa yang diasumsikan integrasi bawaan.
});
