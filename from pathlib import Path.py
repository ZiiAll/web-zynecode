from pathlib import Path

html = r'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Zii Web Studio — Website Profesional untuk Bisnis</title>
<meta name="description" content="Jasa pembuatan website profesional, landing page, katalog produk, portfolio, dan website bisnis.">
<style>
:root{--bg:#070b14;--card:#101827;--card2:#0d1421;--text:#f5f7fb;--muted:#a9b3c5;--accent:#6c63ff;--accent2:#00d4ff;--line:#202b3d}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;background:radial-gradient(circle at 80% 10%,#18225c 0,transparent 28%),var(--bg);color:var(--text);line-height:1.6}
a{text-decoration:none;color:inherit}
.container{width:min(1120px,92%);margin:auto}
nav{position:sticky;top:0;z-index:20;background:rgba(7,11,20,.8);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.06)}
.nav{height:72px;display:flex;align-items:center;justify-content:space-between}
.logo{font-weight:900;font-size:22px}.logo span{color:var(--accent2)}
.navlinks{display:flex;gap:25px;color:var(--muted);font-size:14px}
.btn{display:inline-flex;align-items:center;justify-content:center;padding:13px 20px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#8d6bff);font-weight:800;border:0;cursor:pointer;color:white}
.btn.secondary{background:transparent;border:1px solid var(--line)}
.hero{padding:100px 0 80px;text-align:center}
.badge{display:inline-block;padding:8px 13px;border:1px solid #29365a;background:#111a31;border-radius:999px;color:#cbd5ff;font-size:13px;margin-bottom:20px}
h1{font-size:clamp(42px,7vw,76px);line-height:1.02;letter-spacing:-3px;max-width:850px;margin:auto}
.gradient{background:linear-gradient(90deg,#fff,#8b84ff,#4de4ff);-webkit-background-clip:text;color:transparent}
.hero p{max-width:700px;margin:24px auto;color:var(--muted);font-size:18px}
.actions{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:28px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:55px}
.stat{padding:22px;background:rgba(16,24,39,.75);border:1px solid var(--line);border-radius:18px}.stat b{font-size:28px}.stat small{display:block;color:var(--muted)}
section{padding:80px 0}.section-title{text-align:center;max-width:700px;margin:0 auto 40px}.section-title h2{font-size:40px;letter-spacing:-1px}.section-title p{color:var(--muted);margin-top:10px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:linear-gradient(180deg,var(--card),var(--card2));border:1px solid var(--line);border-radius:22px;padding:28px;position:relative}
.card.featured{border-color:#6c63ff;box-shadow:0 0 40px rgba(108,99,255,.12)}
.card h3{font-size:22px}.price{font-size:38px;font-weight:900;margin:15px 0}.price span{font-size:14px;color:var(--muted);font-weight:500}
.card ul{list-style:none;margin:20px 0}.card li{padding:8px 0;color:#cbd3e2}.card li::before{content:"✓";color:#63e6be;font-weight:bold;margin-right:9px}
.tag{position:absolute;right:18px;top:18px;background:#6c63ff;padding:5px 9px;border-radius:999px;font-size:11px;font-weight:800}
.services .card{min-height:210px}.icon{font-size:30px;margin-bottom:12px}
.portfolio{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}.project{min-height:250px;border-radius:22px;padding:28px;display:flex;flex-direction:column;justify-content:end;border:1px solid var(--line);background:linear-gradient(135deg,#151d3d,#0c1320)}
.project:nth-child(2){background:linear-gradient(135deg,#17343c,#0c1320)}.project:nth-child(3){background:linear-gradient(135deg,#34231b,#0c1320)}.project:nth-child(4){background:linear-gradient(135deg,#27204b,#0c1320)}
.project p{color:#b8c1d2}.project h3{font-size:25px}
.process{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.step{padding:24px;border:1px solid var(--line);border-radius:18px}.num{font-size:12px;color:#8e87ff;font-weight:900}
.cta{padding:55px;border-radius:28px;background:linear-gradient(135deg,#211d54,#102c3a);border:1px solid #343a67;text-align:center}.cta h2{font-size:42px}.cta p{color:#c0c9d8;margin:12px auto 25px;max-width:650px}
footer{padding:30px 0;border-top:1px solid var(--line);color:var(--muted);font-size:14px}
footer .foot{display:flex;justify-content:space-between;gap:20px}
@media(max-width:800px){.navlinks{display:none}.grid,.stats,.process{grid-template-columns:1fr}.portfolio{grid-template-columns:1fr}h1{letter-spacing:-2px}.hero{padding-top:70px}.cta{padding:35px 20px}.cta h2{font-size:32px}footer .foot{flex-direction:column}}
</style>
</head>
<body>
<nav><div class="container nav">
<a class="logo" href="#">Zii<span>Web.</span></a>
<div class="navlinks"><a href="#layanan">Layanan</a><a href="#harga">Harga</a><a href="#portfolio">Portfolio</a><a href="#proses">Proses</a></div>
<a class="btn" href="#kontak">Pesan Website</a>
</div></nav>

<header class="hero">
<div class="container">
<div class="badge">⚡ Website modern • cepat • responsive</div>
<h1>Bikin Bisnis Kamu <span class="gradient">Terlihat Profesional</span> di Internet.</h1>
<p>Jasa pembuatan website untuk UMKM, toko, jasa, personal brand, portfolio, dan bisnis lokal. Desain premium tanpa harus punya tim IT.</p>
<div class="actions"><a class="btn" href="#harga">Lihat Paket</a><a class="btn secondary" href="#portfolio">Lihat Demo</a></div>
<div class="stats">
<div class="stat"><b>100%</b><small>Responsive di HP & Desktop</small></div>
<div class="stat"><b>SEO</b><small>Struktur siap ditemukan Google</small></div>
<div class="stat"><b>Fast</b><small>Ringan & nyaman digunakan</small></div>
</div>
</div>
</header>

<section id="layanan" class="services"><div class="container">
<div class="section-title"><h2>Layanan Website</h2><p>Semua yang dibutuhkan untuk membuat bisnis terlihat lebih terpercaya.</p></div>
<div class="grid">
<div class="card"><div class="icon">🌐</div><h3>Website Bisnis</h3><p>Profil usaha, layanan, keunggulan, kontak, dan CTA untuk mendapatkan pelanggan.</p></div>
<div class="card"><div class="icon">🛍️</div><h3>Katalog Produk</h3><p>Tampilkan produk, harga, foto, kategori, dan tombol pesan langsung.</p></div>
<div class="card"><div class="icon">🎯</div><h3>Landing Page</h3><p>Halaman fokus untuk promosi produk, jasa, event, atau iklan digital.</p></div>
<div class="card"><div class="icon">👤</div><h3>Portfolio</h3><p>Personal branding untuk freelancer, kreator, mahasiswa, dan profesional.</p></div>
<div class="card"><div class="icon">📱</div><h3>WhatsApp Integration</h3><p>Tombol WhatsApp agar calon pelanggan bisa langsung menghubungi pemilik bisnis.</p></div>
<div class="card"><div class="icon">⚙️</div><h3>Maintenance</h3><p>Update konten, perbaikan minor, dan bantuan setelah website selesai.</p></div>
</div>
</div></section>

<section id="harga"><div class="container">
<div class="section-title"><h2>Paket Harga</h2><p>Pilih paket sesuai kebutuhan. Harga dapat kamu ubah sesuai strategi jualanmu.</p></div>
<div class="grid">
<div class="card"><h3>Starter</h3><div class="price">Rp499K <span>/ website</span></div><ul><li>1–3 halaman</li><li>Desain responsive</li><li>WhatsApp button</li><li>Form kontak</li><li>Basic SEO</li></ul><a class="btn" href="#kontak">Pilih Starter</a></div>
<div class="card featured"><span class="tag">PALING LARIS</span><h3>Business</h3><div class="price">Rp999K <span>/ website</span></div><ul><li>Hingga 7 halaman</li><li>Desain premium</li><li>Katalog produk</li><li>WhatsApp & CTA</li><li>Basic SEO</li><li>1x revisi</li></ul><a class="btn" href="#kontak">Pilih Business</a></div>
<div class="card"><h3>Premium</h3><div class="price">Rp1,99JT <span>/ website</span></div><ul><li>Website custom</li><li>Hingga 12 halaman</li><li>Katalog & fitur lanjutan</li><li>SEO lebih lengkap</li><li>Prioritas pengerjaan</li><li>2x revisi</li></ul><a class="btn" href="#kontak">Pilih Premium</a></div>
</div>
</div></section>

<section id="portfolio"><div class="container">
<div class="section-title"><h2>Contoh Portfolio</h2><p>Demo konsep yang bisa kamu tunjukkan kepada calon klien.</p></div>
<div class="portfolio">
<div class="project"><p>UMKM / Food</p><h3>RasaNusa</h3><p>Website restoran & katalog menu.</p></div>
<div class="project"><p>Fashion Store</p><h3>UrbanWear</h3><p>Landing page toko fashion modern.</p></div>
<div class="project"><p>Local Service</p><h3>CleanPro</h3><p>Website jasa dengan tombol booking.</p></div>
<div class="project"><p>Personal Brand</p><h3>Creator Portfolio</h3><p>Portfolio profesional untuk kreator.</p></div>
</div>
</div></section>

<section id="proses"><div class="container">
<div class="section-title"><h2>Proses Pengerjaan</h2><p>Sederhana, transparan, dan mudah dipahami klien.</p></div>
<div class="process">
<div class="step"><div class="num">01</div><h3>Konsultasi</h3><p>Bahas kebutuhan, konsep, dan target website.</p></div>
<div class="step"><div class="num">02</div><h3>Desain</h3><p>Buat tampilan sesuai brand dan kebutuhan bisnis.</p></div>
<div class="step"><div class="num">03</div><h3>Pengerjaan</h3><p>Website dikembangkan dan diuji di berbagai perangkat.</p></div>
<div class="step"><div class="num">04</div><h3>Serah Terima</h3><p>Website siap dipakai dan dipromosikan.</p></div>
</div>
</div></section>

<section id="kontak"><div class="container">
<div class="cta">
<h2>Siap Punya Website Profesional?</h2>
<p>Ceritakan bisnis atau ide website kamu. Klik tombol di bawah untuk mulai konsultasi melalui WhatsApp.</p>
<a class="btn" id="wa" href="#" target="_blank">💬 Konsultasi via WhatsApp</a>
</div>
</div></section>

<footer><div class="container foot"><div>© 2026 Zii Web Studio. All rights reserved.</div><div>Website • Landing Page • Portfolio • Katalog</div></div></footer>

<script>
/* GANTI NOMOR DI BAWAH DENGAN NOMOR WHATSAPP KAMU.
   Format: 628xxxxxxxxxx, tanpa + atau spasi. */
const nomor = "6281234567890";
const pesan = "Halo Zii Web Studio, saya tertarik membuat website. Saya ingin konsultasi tentang paket dan kebutuhan website.";
document.querySelectorAll('a[href="#kontak"]').forEach(a=>{
  a.addEventListener('click',()=>setTimeout(()=>{
    document.getElementById('wa').href="https://wa.me/"+nomor+"?text="+encodeURIComponent(pesan);
  },50));
});
document.getElementById('wa').href="https://wa.me/"+nomor+"?text="+encodeURIComponent(pesan);
</script>
</body>
</html>
'''

workspace_dir = Path(__file__).resolve().parent
output_path = workspace_dir / "zii-web-studio-demo.html"
output_path.write_text(html, encoding="utf-8")
print(f"File dibuat: {output_path}")
