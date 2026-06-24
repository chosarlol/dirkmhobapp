from pathlib import Path
root = Path('frontend')
files = {
    'res_brown.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | Brown</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    img { display:block; max-width:100%; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .icon-btn:hover, .login-btn:hover, .primary-btn:hover { transform:translateY(-2px); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg, rgba(0,119,200,0.95), rgba(255,107,53,0.95)); color:white; border-radius:30px; padding:2rem; display:grid; grid-template-columns:1.2fr .8fr; gap:1.5rem; box-shadow:var(--shadow); }
    .hero-badge { display:inline-flex; align-items:center; gap:0.4rem; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); font-size:0.9rem; width:max-content; margin-bottom:1rem; }
    .hero h1 { font-size:clamp(1.8rem, 3vw, 2.7rem); margin-bottom:0.6rem; }
    .hero p { color:rgba(255,255,255,0.9); max-width:650px; }
    .hero-stats { display:flex; flex-wrap:wrap; gap:0.75rem; margin-top:1.2rem; }
    .hero-stats span { background:rgba(255,255,255,0.14); padding:0.65rem 0.85rem; border-radius:999px; font-weight:600; }
    .restaurant-spotlight { background:rgba(255,255,255,0.16); border:1px solid rgba(255,255,255,0.2); border-radius:24px; padding:1rem; display:grid; gap:0.85rem; align-content:start; }
    .spotlight-top { display:flex; align-items:center; gap:0.8rem; }
    .spotlight-logo { width:64px; height:64px; display:flex; align-items:center; justify-content:center; border-radius:20px; background:white; color:var(--primary); font-size:1.5rem; font-weight:800; }
    .section { padding:1rem 0 2rem; }
    .layout { display:grid; grid-template-columns:1.6fr .8fr; gap:1.2rem; align-items:start; }
    .panel { background:var(--surface); border:1px solid var(--border); border-radius:24px; box-shadow:var(--shadow); }
    .panel-header { padding:1.25rem 1.25rem 0; display:flex; justify-content:space-between; align-items:center; }
    .panel-title { font-size:1.15rem; font-weight:800; }
    .menu-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem; padding:1.25rem; }
    .menu-card { border:1px solid var(--border); border-radius:18px; overflow:hidden; transition:transform .2s ease, box-shadow .2s ease; }
    .menu-card:hover { transform:translateY(-3px); box-shadow:0 12px 30px rgba(15,23,42,0.1); }
    .menu-image { height:150px; background:linear-gradient(135deg,#ffefe7,#ffedd5); display:flex; align-items:center; justify-content:center; font-size:2.5rem; }
    .menu-body { padding:0.95rem; display:grid; gap:0.6rem; }
    .menu-body h3 { font-size:1rem; }
    .menu-body p { color:var(--muted); font-size:0.92rem; }
    .menu-meta { display:flex; justify-content:space-between; align-items:center; font-weight:700; }
    .qty-row { display:flex; align-items:center; gap:0.5rem; }
    .qty-btn { width:30px; height:30px; border-radius:50%; border:1px solid var(--border); background:var(--bg); cursor:pointer; font-weight:700; }
    .cart-panel { padding:1.25rem; position:sticky; top:95px; display:grid; gap:1rem; }
    .cart-item { display:flex; justify-content:space-between; align-items:center; padding:0.7rem 0; border-bottom:1px solid var(--border); }
    .cart-item:last-child { border-bottom:none; }
    .summary-row { display:flex; justify-content:space-between; padding:0.3rem 0; color:var(--muted); }
    .summary-total { font-size:1.1rem; font-weight:800; color:var(--text); }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .layout{grid-template-columns:1fr;} .cart-panel{position:static;} .hero-card{grid-template-columns:1fr;} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .menu-grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container navbar">
      <a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a>
      <nav class="nav-links" aria-label="Main navigation">
        <a href="home_screen.html">Home</a>
        <a href="search_screen.html">Restaurants</a>
        <a href="asian_dish.html">Categories</a>
        <a href="home_screen.html">Promotions</a>
        <a href="home_screen.html">Contact</a>
      </nav>
      <div class="nav-actions">
        <label class="search-box"><span>🔍</span><input placeholder="Search dishes" /></label>
        <a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a>
        <a class="login-btn" href="login.html">Login</a>
      </div>
    </div>
  </header>
  <main class="container">
    <section class="hero">
      <div class="hero-card">
        <div>
          <div class="hero-badge">☕ Bakery & Coffee</div>
          <h1>Brown - TK Avenue</h1>
          <p>Fresh pastries, handcrafted coffee, and a calm café experience delivered to your door in minutes.</p>
          <div class="hero-stats"><span>⭐ 4.6 (250+ reviews)</span><span>⏱ 20–30 min</span><span>🚚 Free delivery</span><span>🥐 Bakery</span></div>
        </div>
        <div class="restaurant-spotlight">
          <div class="spotlight-top"><div class="spotlight-logo">B</div><div><strong>Brown Café</strong><div style="color:rgba(255,255,255,.9);">Open now • 7:00 AM – 10:00 PM</div></div></div>
          <div>Popular picks: Croissant, Latte, Cinnamon Roll</div>
          <div>Best for: breakfast, coffee breaks, dessert cravings</div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="layout">
        <div class="panel">
          <div class="panel-header"><h2 class="panel-title">Popular Items</h2><span style="color:var(--muted); font-weight:600;">Fresh today</span></div>
          <div class="menu-grid">
            <article class="menu-card"><div class="menu-image">🥐</div><div class="menu-body"><h3>Butter Croissant</h3><p>Flaky pastry with a golden crust and buttery finish.</p><div class="menu-meta"><span>$3.80</span><div class="qty-row" data-price="3.80"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article>
            <article class="menu-card"><div class="menu-image">☕</div><div class="menu-body"><h3>House Latte</h3><p>Velvety espresso with steamed milk and sweet aroma.</p><div class="menu-meta"><span>$4.20</span><div class="qty-row" data-price="4.20"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article>
            <article class="menu-card"><div class="menu-image">🍰</div><div class="menu-body"><h3>Cinnamon Roll</h3><p>Soft swirls glazed with vanilla and cinnamon spice.</p><div class="menu-meta"><span>$4.90</span><div class="qty-row" data-price="4.90"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article>
            <article class="menu-card"><div class="menu-image">🥪</div><div class="menu-body"><h3>Breakfast Sandwich</h3><p>Egg, cheese, and tomato served on toasted brioche.</p><div class="menu-meta"><span>$5.60</span><div class="qty-row" data-price="5.60"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article>
          </div>
        </div>
        <aside class="panel cart-panel">
          <div class="panel-header" style="padding:0;"><h2 class="panel-title">Your order</h2><span style="color:var(--muted); font-weight:600;">Delivery</span></div>
          <div id="cart-items"><div class="cart-item"><span>Your cart is empty</span><strong>$0.00</strong></div></div>
          <div><div class="summary-row"><span>Subtotal</span><span id="subtotal">$0.00</span></div><div class="summary-row"><span>Delivery fee</span><span>$2.00</span></div><div class="summary-row"><span>Service fee</span><span>$1.00</span></div><div class="summary-row summary-total"><span>Total</span><span id="total">$0.00</span></div></div>
          <a class="primary-btn" href="check_out.html">Checkout</a>
        </aside>
      </div>
    </section>
  </main>
  <footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer>
  <script>
    const cartItems = document.getElementById('cart-items');
    const subtotalEl = document.getElementById('subtotal');
    const totalEl = document.getElementById('total');
    const rows = document.querySelectorAll('.qty-row');
    rows.forEach(row => { const qtyEl = row.querySelector('.qty-value'); row.querySelectorAll('.qty-btn').forEach(btn => { btn.addEventListener('click', () => { const action = btn.dataset.action; const current = parseInt(qtyEl.textContent,10); const next = action === 'increase' ? current + 1 : Math.max(0,current - 1); qtyEl.textContent = next; updateCart();});});});
    function updateCart(){ const items = []; rows.forEach(row => { const qty = parseInt(row.querySelector('.qty-value').textContent,10); if (qty > 0) { const name = row.closest('.menu-card').querySelector('h3').textContent; const price = parseFloat(row.dataset.price); items.push({name, qty, price}); }}); if (!items.length) { cartItems.innerHTML = '<div class="cart-item"><span>Your cart is empty</span><strong>$0.00</strong></div>'; subtotalEl.textContent = '$0.00'; totalEl.textContent = '$0.00'; return; } const subtotal = items.reduce((sum,item)=>sum+item.qty*item.price,0); cartItems.innerHTML = items.map(item => `<div class="cart-item"><span>${item.qty}× ${item.name}</span><strong>$${(item.qty*item.price).toFixed(2)}</strong></div>`).join(''); subtotalEl.textContent = `$${subtotal.toFixed(2)}`; totalEl.textContent = `$${(subtotal+2+1).toFixed(2)}`; }
  </script>
</body>
</html>''',
    'res_kfc.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | KFC</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    img { display:block; max-width:100%; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg, rgba(0,119,200,0.95), rgba(255,107,53,0.95)); color:white; border-radius:30px; padding:2rem; display:grid; grid-template-columns:1.2fr .8fr; gap:1.5rem; box-shadow:var(--shadow); }
    .hero-badge { display:inline-flex; align-items:center; gap:0.4rem; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); font-size:0.9rem; width:max-content; margin-bottom:1rem; }
    .hero h1 { font-size:clamp(1.8rem, 3vw, 2.7rem); margin-bottom:0.6rem; }
    .hero p { color:rgba(255,255,255,0.9); max-width:650px; }
    .hero-stats { display:flex; flex-wrap:wrap; gap:0.75rem; margin-top:1.2rem; }
    .hero-stats span { background:rgba(255,255,255,0.14); padding:0.65rem 0.85rem; border-radius:999px; font-weight:600; }
    .restaurant-spotlight { background:rgba(255,255,255,0.16); border:1px solid rgba(255,255,255,0.2); border-radius:24px; padding:1rem; display:grid; gap:0.85rem; align-content:start; }
    .spotlight-top { display:flex; align-items:center; gap:0.8rem; }
    .spotlight-logo { width:64px; height:64px; display:flex; align-items:center; justify-content:center; border-radius:20px; background:white; color:var(--primary); font-size:1.5rem; font-weight:800; }
    .section { padding:1rem 0 2rem; }
    .layout { display:grid; grid-template-columns:1.6fr .8fr; gap:1.2rem; align-items:start; }
    .panel { background:var(--surface); border:1px solid var(--border); border-radius:24px; box-shadow:var(--shadow); }
    .panel-header { padding:1.25rem 1.25rem 0; display:flex; justify-content:space-between; align-items:center; }
    .panel-title { font-size:1.15rem; font-weight:800; }
    .menu-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem; padding:1.25rem; }
    .menu-card { border:1px solid var(--border); border-radius:18px; overflow:hidden; transition:transform .2s ease, box-shadow .2s ease; }
    .menu-card:hover { transform:translateY(-3px); box-shadow:0 12px 30px rgba(15,23,42,0.1); }
    .menu-image { height:150px; background:linear-gradient(135deg,#fff4ec,#ffe6d9); display:flex; align-items:center; justify-content:center; font-size:2.5rem; }
    .menu-body { padding:0.95rem; display:grid; gap:0.6rem; }
    .menu-body h3 { font-size:1rem; }
    .menu-body p { color:var(--muted); font-size:0.92rem; }
    .menu-meta { display:flex; justify-content:space-between; align-items:center; font-weight:700; }
    .qty-row { display:flex; align-items:center; gap:0.5rem; }
    .qty-btn { width:30px; height:30px; border-radius:50%; border:1px solid var(--border); background:var(--bg); cursor:pointer; font-weight:700; }
    .cart-panel { padding:1.25rem; position:sticky; top:95px; display:grid; gap:1rem; }
    .cart-item { display:flex; justify-content:space-between; align-items:center; padding:0.7rem 0; border-bottom:1px solid var(--border); }
    .cart-item:last-child { border-bottom:none; }
    .summary-row { display:flex; justify-content:space-between; padding:0.3rem 0; color:var(--muted); }
    .summary-total { font-size:1.1rem; font-weight:800; color:var(--text); }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .layout{grid-template-columns:1fr;} .cart-panel{position:static;} .hero-card{grid-template-columns:1fr;} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .menu-grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header"><div class="container navbar"><a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a><nav class="nav-links" aria-label="Main navigation"><a href="home_screen.html">Home</a><a href="search_screen.html">Restaurants</a><a href="asian_dish.html">Categories</a><a href="home_screen.html">Promotions</a><a href="home_screen.html">Contact</a></nav><div class="nav-actions"><label class="search-box"><span>🔍</span><input placeholder="Search dishes" /></label><a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a><a class="login-btn" href="login.html">Login</a></div></div></header>
  <main class="container"><section class="hero"><div class="hero-card"><div><div class="hero-badge">🍗 Fried Chicken</div><h1>KFC - TK Avenue</h1><p>Classic fried chicken, comfort meals, and speedy delivery for every craving.</p><div class="hero-stats"><span>⭐ 4.5 (300+ reviews)</span><span>⏱ 15–25 min</span><span>🚚 Free delivery</span><span>🍗 Fast food</span></div></div><div class="restaurant-spotlight"><div class="spotlight-top"><div class="spotlight-logo">K</div><div><strong>KFC</strong><div style="color:rgba(255,255,255,.9);">Open now • 10:00 AM – 11:00 PM</div></div></div><div>Popular picks: Zinger Burger, Bucket Meal, Fries</div><div>Best for: lunch, family meals, quick dinner</div></div></div></section><section class="section"><div class="layout"><div class="panel"><div class="panel-header"><h2 class="panel-title">Best Sellers</h2><span style="color:var(--muted); font-weight:600;">Popular right now</span></div><div class="menu-grid"><article class="menu-card"><div class="menu-image">🍗</div><div class="menu-body"><h3>Original Bucket</h3><p>6 pieces of crispy chicken with fries and a drink.</p><div class="menu-meta"><span>$12.50</span><div class="qty-row" data-price="12.50"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article><article class="menu-card"><div class="menu-image">🍔</div><div class="menu-body"><h3>Zinger Burger</h3><p>Spicy chicken filet with lettuce and sauce.</p><div class="menu-meta"><span>$6.90</span><div class="qty-row" data-price="6.90"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article><article class="menu-card"><div class="menu-image">🍟</div><div class="menu-body"><h3>Large Fries</h3><p>Golden fries with a crunchy finish.</p><div class="menu-meta"><span>$3.20</span><div class="qty-row" data-price="3.20"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article><article class="menu-card"><div class="menu-image">🥤</div><div class="menu-body"><h3>Cola Combo</h3><p>Signature drink with your meal combo.</p><div class="menu-meta"><span>$2.80</span><div class="qty-row" data-price="2.80"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article></div></div><aside class="panel cart-panel"><div class="panel-header" style="padding:0;"><h2 class="panel-title">Your order</h2><span style="color:var(--muted); font-weight:600;">Fast delivery</span></div><div id="cart-items"><div class="cart-item"><span>Your cart is empty</span><strong>$0.00</strong></div></div><div><div class="summary-row"><span>Subtotal</span><span id="subtotal">$0.00</span></div><div class="summary-row"><span>Delivery fee</span><span>$2.00</span></div><div class="summary-row"><span>Service fee</span><span>$1.00</span></div><div class="summary-row summary-total"><span>Total</span><span id="total">$0.00</span></div></div><a class="primary-btn" href="check_out.html">Checkout</a></aside></div></section></main><footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer><script>const cartItems=document.getElementById('cart-items');const subtotalEl=document.getElementById('subtotal');const totalEl=document.getElementById('total');const rows=document.querySelectorAll('.qty-row');rows.forEach(row=>{const qtyEl=row.querySelector('.qty-value');row.querySelectorAll('.qty-btn').forEach(btn=>{btn.addEventListener('click',()=>{const action=btn.dataset.action;const current=parseInt(qtyEl.textContent,10);const next=action==='increase'?current+1:Math.max(0,current-1);qtyEl.textContent=next;updateCart();});});});function updateCart(){const items=[];rows.forEach(row=>{const qty=parseInt(row.querySelector('.qty-value').textContent,10);if(qty>0){const name=row.closest('.menu-card').querySelector('h3').textContent;const price=parseFloat(row.dataset.price);items.push({name,qty,price});}});if(!items.length){cartItems.innerHTML='<div class="cart-item"><span>Your cart is empty</span><strong>$0.00</strong></div>';subtotalEl.textContent='$0.00';totalEl.textContent='$0.00';return;}const subtotal=items.reduce((sum,item)=>sum+item.qty*item.price,0);cartItems.innerHTML=items.map(item=>`<div class="cart-item"><span>${item.qty}× ${item.name}</span><strong>$${(item.qty*item.price).toFixed(2)}</strong></div>`).join('');subtotalEl.textContent=`$${subtotal.toFixed(2)}`;totalEl.textContent=`$${(subtotal+2+1).toFixed(2)}`;}</script></body></html>''',
    'res_texas.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | Texas Chicken</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    img { display:block; max-width:100%; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg, rgba(0,119,200,0.95), rgba(255,107,53,0.95)); color:white; border-radius:30px; padding:2rem; display:grid; grid-template-columns:1.2fr .8fr; gap:1.5rem; box-shadow:var(--shadow); }
    .hero-badge { display:inline-flex; align-items:center; gap:0.4rem; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); font-size:0.9rem; width:max-content; margin-bottom:1rem; }
    .hero h1 { font-size:clamp(1.8rem, 3vw, 2.7rem); margin-bottom:0.6rem; }
    .hero p { color:rgba(255,255,255,0.9); max-width:650px; }
    .hero-stats { display:flex; flex-wrap:wrap; gap:0.75rem; margin-top:1.2rem; }
    .hero-stats span { background:rgba(255,255,255,0.14); padding:0.65rem 0.85rem; border-radius:999px; font-weight:600; }
    .restaurant-spotlight { background:rgba(255,255,255,0.16); border:1px solid rgba(255,255,255,0.2); border-radius:24px; padding:1rem; display:grid; gap:0.85rem; align-content:start; }
    .spotlight-top { display:flex; align-items:center; gap:0.8rem; }
    .spotlight-logo { width:64px; height:64px; display:flex; align-items:center; justify-content:center; border-radius:20px; background:white; color:var(--primary); font-size:1.5rem; font-weight:800; }
    .section { padding:1rem 0 2rem; }
    .layout { display:grid; grid-template-columns:1.6fr .8fr; gap:1.2rem; align-items:start; }
    .panel { background:var(--surface); border:1px solid var(--border); border-radius:24px; box-shadow:var(--shadow); }
    .panel-header { padding:1.25rem 1.25rem 0; display:flex; justify-content:space-between; align-items:center; }
    .panel-title { font-size:1.15rem; font-weight:800; }
    .menu-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem; padding:1.25rem; }
    .menu-card { border:1px solid var(--border); border-radius:18px; overflow:hidden; transition:transform .2s ease, box-shadow .2s ease; }
    .menu-card:hover { transform:translateY(-3px); box-shadow:0 12px 30px rgba(15,23,42,0.1); }
    .menu-image { height:150px; background:linear-gradient(135deg,#fff6e8,#ffe2b8); display:flex; align-items:center; justify-content:center; font-size:2.5rem; }
    .menu-body { padding:0.95rem; display:grid; gap:0.6rem; }
    .menu-body h3 { font-size:1rem; }
    .menu-body p { color:var(--muted); font-size:0.92rem; }
    .menu-meta { display:flex; justify-content:space-between; align-items:center; font-weight:700; }
    .qty-row { display:flex; align-items:center; gap:0.5rem; }
    .qty-btn { width:30px; height:30px; border-radius:50%; border:1px solid var(--border); background:var(--bg); cursor:pointer; font-weight:700; }
    .cart-panel { padding:1.25rem; position:sticky; top:95px; display:grid; gap:1rem; }
    .cart-item { display:flex; justify-content:space-between; align-items:center; padding:0.7rem 0; border-bottom:1px solid var(--border); }
    .cart-item:last-child { border-bottom:none; }
    .summary-row { display:flex; justify-content:space-between; padding:0.3rem 0; color:var(--muted); }
    .summary-total { font-size:1.1rem; font-weight:800; color:var(--text); }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .layout{grid-template-columns:1fr;} .cart-panel{position:static;} .hero-card{grid-template-columns:1fr;} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .menu-grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header"><div class="container navbar"><a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a><nav class="nav-links" aria-label="Main navigation"><a href="home_screen.html">Home</a><a href="search_screen.html">Restaurants</a><a href="asian_dish.html">Categories</a><a href="home_screen.html">Promotions</a><a href="home_screen.html">Contact</a></nav><div class="nav-actions"><label class="search-box"><span>🔍</span><input placeholder="Search dishes" /></label><a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a><a class="login-btn" href="login.html">Login</a></div></div></header>
  <main class="container"><section class="hero"><div class="hero-card"><div><div class="hero-badge">🍗 Fried Chicken</div><h1>Texas Chicken</h1><p>Juicy fried chicken, hearty sides, and trusted comfort food delivered fast.</p><div class="hero-stats"><span>⭐ 4.5 (120+ reviews)</span><span>⏱ 15–25 min</span><span>🚚 Free delivery</span><span>🍗 Fried chicken</span></div></div><div class="restaurant-spotlight"><div class="spotlight-top"><div class="spotlight-logo">T</div><div><strong>Texas Chicken</strong><div style="color:rgba(255,255,255,.9);">Open now • 10:00 AM – 10:30 PM</div></div></div><div>Popular picks: Spicy Chicken, Wrap Meal, Nuggets</div><div>Best for: casual dining, family orders, late-night cravings</div></div></div></section><section class="section"><div class="layout"><div class="panel"><div class="panel-header"><h2 class="panel-title">Recommended For You</h2><span style="color:var(--muted); font-weight:600;">Combo favorites</span></div><div class="menu-grid"><article class="menu-card"><div class="menu-image">🍗</div><div class="menu-body"><h3>Spicy Chicken Meal</h3><p>2 spicy chicken pieces, fries, and a soft drink.</p><div class="menu-meta"><span>$9.80</span><div class="qty-row" data-price="9.80"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article><article class="menu-card"><div class="menu-image">🌯</div><div class="menu-body"><h3>Chicken Wrap</h3><p>Grilled chicken wrap with lettuce and creamy sauce.</p><div class="menu-meta"><span>$5.40</span><div class="qty-row" data-price="5.40"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article><article class="menu-card"><div class="menu-image">🍟</div><div class="menu-body"><h3>Loaded Fries</h3><p>Golden fries topped with cheese and herbs.</p><div class="menu-meta"><span>$4.60</span><div class="qty-row" data-price="4.60"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article><article class="menu-card"><div class="menu-image">🥤</div><div class="menu-body"><h3>Family Combo</h3><p>Perfect for sharing with chicken strips and sides.</p><div class="menu-meta"><span>$15.90</span><div class="qty-row" data-price="15.90"><button class="qty-btn" data-action="decrease">−</button><span class="qty-value">0</span><button class="qty-btn" data-action="increase">+</button></div></div></div></article></div></div><aside class="panel cart-panel"><div class="panel-header" style="padding:0;"><h2 class="panel-title">Your order</h2><span style="color:var(--muted); font-weight:600;">Fast delivery</span></div><div id="cart-items"><div class="cart-item"><span>Your cart is empty</span><strong>$0.00</strong></div></div><div><div class="summary-row"><span>Subtotal</span><span id="subtotal">$0.00</span></div><div class="summary-row"><span>Delivery fee</span><span>$2.00</span></div><div class="summary-row"><span>Service fee</span><span>$1.00</span></div><div class="summary-row summary-total"><span>Total</span><span id="total">$0.00</span></div></div><a class="primary-btn" href="check_out.html">Checkout</a></aside></div></section></main><footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer><script>const cartItems=document.getElementById('cart-items');const subtotalEl=document.getElementById('subtotal');const totalEl=document.getElementById('total');const rows=document.querySelectorAll('.qty-row');rows.forEach(row=>{const qtyEl=row.querySelector('.qty-value');row.querySelectorAll('.qty-btn').forEach(btn=>{btn.addEventListener('click',()=>{const action=btn.dataset.action;const current=parseInt(qtyEl.textContent,10);const next=action==='increase'?current+1:Math.max(0,current-1);qtyEl.textContent=next;updateCart();});});});function updateCart(){const items=[];rows.forEach(row=>{const qty=parseInt(row.querySelector('.qty-value').textContent,10);if(qty>0){const name=row.closest('.menu-card').querySelector('h3').textContent;const price=parseFloat(row.dataset.price);items.push({name,qty,price});}});if(!items.length){cartItems.innerHTML='<div class="cart-item"><span>Your cart is empty</span><strong>$0.00</strong></div>';subtotalEl.textContent='$0.00';totalEl.textContent='$0.00';return;}const subtotal=items.reduce((sum,item)=>sum+item.qty*item.price,0);cartItems.innerHTML=items.map(item=>`<div class="cart-item"><span>${item.qty}× ${item.name}</span><strong>$${(item.qty*item.price).toFixed(2)}</strong></div>`).join('');subtotalEl.textContent=`$${subtotal.toFixed(2)}`;totalEl.textContent=`$${(subtotal+2+1).toFixed(2)}`;}</script></body></html>''',
    'asian_dish.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | Asian Cuisine</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg,#0f172a,#1d4ed8); color:white; border-radius:30px; padding:2rem; box-shadow:var(--shadow); }
    .hero-card h1 { font-size:clamp(1.8rem,3vw,2.4rem); margin-bottom:0.6rem; }
    .hero-card p { color:rgba(255,255,255,0.85); max-width:640px; }
    .filters { display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:0.8rem; background:var(--surface); padding:1rem; border-radius:24px; border:1px solid var(--border); box-shadow:var(--shadow); margin-bottom:1.2rem; }
    .filter input, .filter select { width:100%; padding:0.7rem 0.8rem; border:1px solid var(--border); border-radius:12px; background:#f8fafc; }
    .grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem; }
    .card { background:var(--surface); border:1px solid var(--border); border-radius:24px; overflow:hidden; box-shadow:var(--shadow); transition:transform .2s ease, box-shadow .2s ease; position:relative; }
    .card:hover { transform:translateY(-4px); box-shadow:0 20px 40px rgba(15,23,42,0.12); }
    .card img { height:180px; width:100%; object-fit:cover; background:#e2e8f0; }
    .card-body { padding:1rem; display:grid; gap:0.65rem; }
    .card-top { display:flex; justify-content:space-between; align-items:center; }
    .fav-btn { width:36px; height:36px; border:none; border-radius:50%; background:#fff7ed; color:var(--secondary); cursor:pointer; }
    .meta-row { display:flex; flex-wrap:wrap; gap:0.6rem; color:var(--muted); font-size:0.9rem; }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .filters{grid-template-columns:repeat(3,1fr);} .grid{grid-template-columns:repeat(2,1fr);} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .filters{grid-template-columns:1fr 1fr;} .grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .filters{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header"><div class="container navbar"><a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a><nav class="nav-links" aria-label="Main navigation"><a href="home_screen.html">Home</a><a href="search_screen.html">Restaurants</a><a href="asian_dish.html">Categories</a><a href="home_screen.html">Promotions</a><a href="home_screen.html">Contact</a></nav><div class="nav-actions"><label class="search-box"><span>🔍</span><input id="searchInput" placeholder="Search restaurants" /></label><a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a><a class="login-btn" href="login.html">Login</a></div></div></header>
  <main class="container"><section class="hero"><div class="hero-card"><div><div style="display:inline-flex; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); margin-bottom:1rem;">🍜 Asian Cuisine</div><h1>Discover authentic Asian flavors near you.</h1><p>From ramen and sushi to Korean BBQ and noodles, our curated restaurants deliver comfort and variety.</p></div></div></section><section class="filters"><label class="filter"><input placeholder="Search" id="searchField" /></label><label class="filter"><select><option>Any rating</option><option>4.5+</option><option>4.0+</option></select></label><label class="filter"><select><option>Any time</option><option>15–25 min</option><option>25–35 min</option></select></label><label class="filter"><select><option>Any price</option><option>$</option><option>$$</option></select></label><label class="filter"><select><option>Free delivery</option><option>Paid delivery</option></select></label><label class="filter"><select><option>Sort by</option><option>Top rated</option><option>Fastest</option></select></label></section><section class="grid"><article class="card" data-name="Sushi House" data-cuisine="Japanese" data-rating="4.8" data-time="20" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23f1f5f9'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%230077C8'%3E🍣%3C/text%3E%3C/svg%3E" alt="Sushi House" /><div class="card-body"><div class="card-top"><strong>Sushi House</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Japanese</span><span>⭐ 4.8</span><span>⏱ 20 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_brown.html">View Menu</a></div></article><article class="card" data-name="Noodle Street" data-cuisine="Chinese" data-rating="4.6" data-time="25" data-price="$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23fef3c7'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%23ff6b35'%3E🍜%3C/text%3E%3C/svg%3E" alt="Noodle Street" /><div class="card-body"><div class="card-top"><strong>Noodle Street</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Chinese</span><span>⭐ 4.6</span><span>⏱ 25 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_kfc.html">View Menu</a></div></article><article class="card" data-name="Korean Grill" data-cuisine="Korean" data-rating="4.7" data-time="22" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23fef2f2'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%23dc2626'%3E🥩%3C/text%3E%3C/svg%3E" alt="Korean Grill" /><div class="card-body"><div class="card-top"><strong>Korean Grill</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Korean</span><span>⭐ 4.7</span><span>⏱ 22 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_texas.html">View Menu</a></div></article></section></main><footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer><script>const searchInput=document.getElementById('searchInput');const searchField=document.getElementById('searchField');const cards=Array.from(document.querySelectorAll('.card'));const filterCards=()=>{const term=(searchInput.value+' '+searchField.value).toLowerCase();cards.forEach(card=>{const text=`${card.dataset.name} ${card.dataset.cuisine}`.toLowerCase();card.style.display=text.includes(term)?'block':'none';});};searchInput.addEventListener('input',filterCards);searchField.addEventListener('input',filterCards);document.querySelectorAll('.fav-btn').forEach(btn=>btn.addEventListener('click',()=>{btn.textContent=btn.textContent==='♡'?'♥':'♡';}));</script></body></html>''',
    'khmer_dish.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | Khmer Cuisine</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg,#14532d,#16a34a); color:white; border-radius:30px; padding:2rem; box-shadow:var(--shadow); }
    .hero-card h1 { font-size:clamp(1.8rem,3vw,2.4rem); margin-bottom:0.6rem; }
    .hero-card p { color:rgba(255,255,255,0.85); max-width:640px; }
    .filters { display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:0.8rem; background:var(--surface); padding:1rem; border-radius:24px; border:1px solid var(--border); box-shadow:var(--shadow); margin-bottom:1.2rem; }
    .filter input, .filter select { width:100%; padding:0.7rem 0.8rem; border:1px solid var(--border); border-radius:12px; background:#f8fafc; }
    .grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem; }
    .card { background:var(--surface); border:1px solid var(--border); border-radius:24px; overflow:hidden; box-shadow:var(--shadow); transition:transform .2s ease, box-shadow .2s ease; position:relative; }
    .card:hover { transform:translateY(-4px); box-shadow:0 20px 40px rgba(15,23,42,0.12); }
    .card img { height:180px; width:100%; object-fit:cover; background:#e2e8f0; }
    .card-body { padding:1rem; display:grid; gap:0.65rem; }
    .card-top { display:flex; justify-content:space-between; align-items:center; }
    .fav-btn { width:36px; height:36px; border:none; border-radius:50%; background:#fff7ed; color:var(--secondary); cursor:pointer; }
    .meta-row { display:flex; flex-wrap:wrap; gap:0.6rem; color:var(--muted); font-size:0.9rem; }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .filters{grid-template-columns:repeat(3,1fr);} .grid{grid-template-columns:repeat(2,1fr);} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .filters{grid-template-columns:1fr 1fr;} .grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .filters{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header"><div class="container navbar"><a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a><nav class="nav-links" aria-label="Main navigation"><a href="home_screen.html">Home</a><a href="search_screen.html">Restaurants</a><a href="asian_dish.html">Categories</a><a href="home_screen.html">Promotions</a><a href="home_screen.html">Contact</a></nav><div class="nav-actions"><label class="search-box"><span>🔍</span><input id="searchInput" placeholder="Search restaurants" /></label><a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a><a class="login-btn" href="login.html">Login</a></div></div></header>
  <main class="container"><section class="hero"><div class="hero-card"><div><div style="display:inline-flex; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); margin-bottom:1rem;">🥗 Khmer Cuisine</div><h1>Traditional Cambodian dishes from top restaurants.</h1><p>Enjoy fresh lok lak, amok, rice noodles, and other beloved local favorites prepared with care.</p></div></div></section><section class="filters"><label class="filter"><input placeholder="Search" id="searchField" /></label><label class="filter"><select><option>Any rating</option><option>4.5+</option><option>4.0+</option></select></label><label class="filter"><select><option>Any time</option><option>15–25 min</option><option>25–35 min</option></select></label><label class="filter"><select><option>Any price</option><option>$</option><option>$$</option></select></label><label class="filter"><select><option>Free delivery</option><option>Paid delivery</option></select></label><label class="filter"><select><option>Sort by</option><option>Top rated</option><option>Fastest</option></select></label></section><section class="grid"><article class="card" data-name="Lok Lak House" data-cuisine="Khmer" data-rating="4.7" data-time="20" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23ecfdf5'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%2316a34a'%3E🥬%3C/text%3E%3C/svg%3E" alt="Lok Lak House" /><div class="card-body"><div class="card-top"><strong>Lok Lak House</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Khmer</span><span>⭐ 4.7</span><span>⏱ 20 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_brown.html">View Menu</a></div></article><article class="card" data-name="Angkor Noodles" data-cuisine="Khmer" data-rating="4.5" data-time="22" data-price="$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23fefce8'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%23ca8a04'%3E🍜%3C/text%3E%3C/svg%3E" alt="Angkor Noodles" /><div class="card-body"><div class="card-top"><strong>Angkor Noodles</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Khmer</span><span>⭐ 4.5</span><span>⏱ 22 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_kfc.html">View Menu</a></div></article><article class="card" data-name="River Kitchen" data-cuisine="Cambodian" data-rating="4.8" data-time="18" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23f5f3ff'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%238b5cf6'%3E🍚%3C/text%3E%3C/svg%3E" alt="River Kitchen" /><div class="card-body"><div class="card-top"><strong>River Kitchen</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Cambodian</span><span>⭐ 4.8</span><span>⏱ 18 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_texas.html">View Menu</a></div></article></section></main><footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer><script>const searchInput=document.getElementById('searchInput');const searchField=document.getElementById('searchField');const cards=Array.from(document.querySelectorAll('.card'));const filterCards=()=>{const term=(searchInput.value+' '+searchField.value).toLowerCase();cards.forEach(card=>{const text=`${card.dataset.name} ${card.dataset.cuisine}`.toLowerCase();card.style.display=text.includes(term)?'block':'none';});};searchInput.addEventListener('input',filterCards);searchField.addEventListener('input',filterCards);document.querySelectorAll('.fav-btn').forEach(btn=>btn.addEventListener('click',()=>{btn.textContent=btn.textContent==='♡'?'♥':'♡';}));</script></body></html>''',
    'pastry_dish.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | Pastry & Bakery</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg,#7c2d12,#ea580c); color:white; border-radius:30px; padding:2rem; box-shadow:var(--shadow); }
    .hero-card h1 { font-size:clamp(1.8rem,3vw,2.4rem); margin-bottom:0.6rem; }
    .hero-card p { color:rgba(255,255,255,0.85); max-width:640px; }
    .filters { display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:0.8rem; background:var(--surface); padding:1rem; border-radius:24px; border:1px solid var(--border); box-shadow:var(--shadow); margin-bottom:1.2rem; }
    .filter input, .filter select { width:100%; padding:0.7rem 0.8rem; border:1px solid var(--border); border-radius:12px; background:#f8fafc; }
    .grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem; }
    .card { background:var(--surface); border:1px solid var(--border); border-radius:24px; overflow:hidden; box-shadow:var(--shadow); transition:transform .2s ease, box-shadow .2s ease; position:relative; }
    .card:hover { transform:translateY(-4px); box-shadow:0 20px 40px rgba(15,23,42,0.12); }
    .card img { height:180px; width:100%; object-fit:cover; background:#e2e8f0; }
    .card-body { padding:1rem; display:grid; gap:0.65rem; }
    .card-top { display:flex; justify-content:space-between; align-items:center; }
    .fav-btn { width:36px; height:36px; border:none; border-radius:50%; background:#fff7ed; color:var(--secondary); cursor:pointer; }
    .meta-row { display:flex; flex-wrap:wrap; gap:0.6rem; color:var(--muted); font-size:0.9rem; }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .filters{grid-template-columns:repeat(3,1fr);} .grid{grid-template-columns:repeat(2,1fr);} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .filters{grid-template-columns:1fr 1fr;} .grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .filters{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header"><div class="container navbar"><a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a><nav class="nav-links" aria-label="Main navigation"><a href="home_screen.html">Home</a><a href="search_screen.html">Restaurants</a><a href="asian_dish.html">Categories</a><a href="home_screen.html">Promotions</a><a href="home_screen.html">Contact</a></nav><div class="nav-actions"><label class="search-box"><span>🔍</span><input id="searchInput" placeholder="Search restaurants" /></label><a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a><a class="login-btn" href="login.html">Login</a></div></div></header>
  <main class="container"><section class="hero"><div class="hero-card"><div><div style="display:inline-flex; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); margin-bottom:1rem;">🥐 Pastry & Bakery</div><h1>Fresh pastries and desserts delivered daily.</h1><p>Enjoy croissants, cheesecakes, cookies, and artisan breads from the city’s favorite bakeries.</p></div></div></section><section class="filters"><label class="filter"><input placeholder="Search" id="searchField" /></label><label class="filter"><select><option>Any rating</option><option>4.5+</option><option>4.0+</option></select></label><label class="filter"><select><option>Any time</option><option>15–25 min</option><option>25–35 min</option></select></label><label class="filter"><select><option>Any price</option><option>$</option><option>$$</option></select></label><label class="filter"><select><option>Free delivery</option><option>Paid delivery</option></select></label><label class="filter"><select><option>Sort by</option><option>Top rated</option><option>Fastest</option></select></label></section><section class="grid"><article class="card" data-name="Golden Crust" data-cuisine="Bakery" data-rating="4.8" data-time="20" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23fff7ed'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%23ea580c'%3E🥐%3C/text%3E%3C/svg%3E" alt="Golden Crust" /><div class="card-body"><div class="card-top"><strong>Golden Crust</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Bakery</span><span>⭐ 4.8</span><span>⏱ 20 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_brown.html">View Menu</a></div></article><article class="card" data-name="Sweet Oven" data-cuisine="Desserts" data-rating="4.6" data-time="22" data-price="$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23fef2f2'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%23f43f5e'%3E🍰%3C/text%3E%3C/svg%3E" alt="Sweet Oven" /><div class="card-body"><div class="card-top"><strong>Sweet Oven</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Desserts</span><span>⭐ 4.6</span><span>⏱ 22 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_kfc.html">View Menu</a></div></article><article class="card" data-name="Morning Bake" data-cuisine="Bakery" data-rating="4.7" data-time="18" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23f8fafc'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%230077C8'%3E🥨%3C/text%3E%3C/svg%3E" alt="Morning Bake" /><div class="card-body"><div class="card-top"><strong>Morning Bake</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Bakery</span><span>⭐ 4.7</span><span>⏱ 18 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_texas.html">View Menu</a></div></article></section></main><footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer><script>const searchInput=document.getElementById('searchInput');const searchField=document.getElementById('searchField');const cards=Array.from(document.querySelectorAll('.card'));const filterCards=()=>{const term=(searchInput.value+' '+searchField.value).toLowerCase();cards.forEach(card=>{const text=`${card.dataset.name} ${card.dataset.cuisine}`.toLowerCase();card.style.display=text.includes(term)?'block':'none';});};searchInput.addEventListener('input',filterCards);searchField.addEventListener('input',filterCards);document.querySelectorAll('.fav-btn').forEach(btn=>btn.addEventListener('click',()=>{btn.textContent=btn.textContent==='♡'?'♥':'♡';}));</script></body></html>''',
    'coffee_dish.html': '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>DirkMhob | Coffee Shops</title>
  <style>
    :root { --primary:#0077C8; --secondary:#FF6B35; --bg:#F8FAFC; --surface:#FFFFFF; --text:#1E293B; --muted:#64748B; --border:#E2E8F0; --shadow:0 16px 45px rgba(15, 23, 42, 0.08); }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:var(--bg); color:var(--text); line-height:1.5; }
    a { color:inherit; text-decoration:none; }
    button, input { font:inherit; }
    .container { width:min(1220px, calc(100% - 2rem)); margin:0 auto; }
    .site-header { position:sticky; top:0; z-index:50; backdrop-filter:blur(16px); background:rgba(248,250,252,0.95); border-bottom:1px solid rgba(226,232,240,0.8); }
    .navbar { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 0; }
    .brand { display:flex; align-items:center; gap:0.75rem; font-weight:800; font-size:1.05rem; }
    .brand-mark { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border-radius:14px; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; box-shadow:0 10px 25px rgba(0,119,200,0.2); }
    .nav-links { display:flex; gap:1.1rem; align-items:center; color:var(--muted); font-weight:600; }
    .nav-links a:hover { color:var(--primary); }
    .nav-actions { display:flex; align-items:center; gap:0.7rem; }
    .search-box { display:flex; align-items:center; gap:0.5rem; background:white; border:1px solid var(--border); border-radius:999px; padding:0.7rem 0.9rem; min-width:250px; }
    .search-box input { border:none; outline:none; width:100%; background:transparent; color:var(--text); }
    .icon-btn, .login-btn, .primary-btn { display:inline-flex; align-items:center; justify-content:center; border:none; border-radius:999px; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease; }
    .icon-btn { width:42px; height:42px; background:white; border:1px solid var(--border); box-shadow:0 6px 20px rgba(15,23,42,0.05); }
    .login-btn { padding:0.75rem 1.1rem; background:var(--primary); color:white; font-weight:700; }
    .primary-btn { padding:0.8rem 1rem; background:linear-gradient(135deg,var(--primary),var(--secondary)); color:white; font-weight:700; box-shadow:0 12px 30px rgba(0,119,200,0.18); }
    .hero { padding:2rem 0 1.5rem; }
    .hero-card { background:linear-gradient(135deg,#4c1d95,#7c3aed); color:white; border-radius:30px; padding:2rem; box-shadow:var(--shadow); }
    .hero-card h1 { font-size:clamp(1.8rem,3vw,2.4rem); margin-bottom:0.6rem; }
    .hero-card p { color:rgba(255,255,255,0.85); max-width:640px; }
    .filters { display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:0.8rem; background:var(--surface); padding:1rem; border-radius:24px; border:1px solid var(--border); box-shadow:var(--shadow); margin-bottom:1.2rem; }
    .filter input, .filter select { width:100%; padding:0.7rem 0.8rem; border:1px solid var(--border); border-radius:12px; background:#f8fafc; }
    .grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:1rem; }
    .card { background:var(--surface); border:1px solid var(--border); border-radius:24px; overflow:hidden; box-shadow:var(--shadow); transition:transform .2s ease, box-shadow .2s ease; position:relative; }
    .card:hover { transform:translateY(-4px); box-shadow:0 20px 40px rgba(15,23,42,0.12); }
    .card img { height:180px; width:100%; object-fit:cover; background:#e2e8f0; }
    .card-body { padding:1rem; display:grid; gap:0.65rem; }
    .card-top { display:flex; justify-content:space-between; align-items:center; }
    .fav-btn { width:36px; height:36px; border:none; border-radius:50%; background:#fff7ed; color:var(--secondary); cursor:pointer; }
    .meta-row { display:flex; flex-wrap:wrap; gap:0.6rem; color:var(--muted); font-size:0.9rem; }
    .footer { margin-top:2rem; padding:2.2rem 0; background:#0f172a; color:#cbd5e1; }
    .footer-grid { display:grid; grid-template-columns:1.2fr 1fr 1fr 1fr; gap:1.5rem; }
    .footer h4 { color:white; margin-bottom:0.7rem; }
    .footer ul { list-style:none; display:grid; gap:0.5rem; color:#94a3b8; }
    .footer a:hover { color:white; }
    .footer-bottom { margin-top:1.2rem; padding-top:1rem; border-top:1px solid rgba(148,163,184,0.2); color:#94a3b8; }
    @media (max-width:980px){ .filters{grid-template-columns:repeat(3,1fr);} .grid{grid-template-columns:repeat(2,1fr);} }
    @media (max-width:760px){ .nav-links{display:none;} .search-box{display:none;} .filters{grid-template-columns:1fr 1fr;} .grid{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr 1fr;} }
    @media (max-width:520px){ .navbar{flex-wrap:wrap;} .filters{grid-template-columns:1fr;} .footer-grid{grid-template-columns:1fr;} }
  </style>
</head>
<body>
  <header class="site-header"><div class="container navbar"><a class="brand" href="home_screen.html"><span class="brand-mark">DM</span><span>DirkMhob</span></a><nav class="nav-links" aria-label="Main navigation"><a href="home_screen.html">Home</a><a href="search_screen.html">Restaurants</a><a href="asian_dish.html">Categories</a><a href="home_screen.html">Promotions</a><a href="home_screen.html">Contact</a></nav><div class="nav-actions"><label class="search-box"><span>🔍</span><input id="searchInput" placeholder="Search restaurants" /></label><a class="icon-btn" href="cart_screen.html" aria-label="Cart">🛒</a><a class="login-btn" href="login.html">Login</a></div></div></header>
  <main class="container"><section class="hero"><div class="hero-card"><div><div style="display:inline-flex; padding:0.45rem 0.8rem; border-radius:999px; background:rgba(255,255,255,0.18); margin-bottom:1rem;">☕ Coffee Shops</div><h1>Fresh coffee and drinks delivered fast.</h1><p>Discover local cafés with espresso, cold brew, pastries, and quick delivery options around the clock.</p></div></div></section><section class="filters"><label class="filter"><input placeholder="Search" id="searchField" /></label><label class="filter"><select><option>Any rating</option><option>4.5+</option><option>4.0+</option></select></label><label class="filter"><select><option>Any time</option><option>15–25 min</option><option>25–35 min</option></select></label><label class="filter"><select><option>Any price</option><option>$</option><option>$$</option></select></label><label class="filter"><select><option>Free delivery</option><option>Paid delivery</option></select></label><label class="filter"><select><option>Sort by</option><option>Top rated</option><option>Fastest</option></select></label></section><section class="grid"><article class="card" data-name="Bean & Bloom" data-cuisine="Coffee" data-rating="4.9" data-time="15" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23f5f3ff'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%234c1d95'%3E☕%3C/text%3E%3C/svg%3E" alt="Bean & Bloom" /><div class="card-body"><div class="card-top"><strong>Bean & Bloom</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Coffee</span><span>⭐ 4.9</span><span>⏱ 15 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_brown.html">View Menu</a></div></article><article class="card" data-name="Café Nova" data-cuisine="Coffee" data-rating="4.6" data-time="20" data-price="$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23eff6ff'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%230077C8'%3E🧋%3C/text%3E%3C/svg%3E" alt="Café Nova" /><div class="card-body"><div class="card-top"><strong>Café Nova</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Coffee</span><span>⭐ 4.6</span><span>⏱ 20 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_kfc.html">View Menu</a></div></article><article class="card" data-name="Morning Brew" data-cuisine="Coffee" data-rating="4.7" data-time="18" data-price="$$"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400'%3E%3Crect width='600' height='400' fill='%23fff7ed'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='140' fill='%23ea580c'%3E🥃%3C/text%3E%3C/svg%3E" alt="Morning Brew" /><div class="card-body"><div class="card-top"><strong>Morning Brew</strong><button class="fav-btn">♡</button></div><div class="meta-row"><span>Coffee</span><span>⭐ 4.7</span><span>⏱ 18 min</span><span>🚚 Free</span></div><a class="primary-btn" href="res_texas.html">View Menu</a></div></article></section></main><footer class="footer"><div class="container footer-grid"><div><h4>DirkMhob</h4><p>Fast delivery, healthier choices, and beautifully curated meals from your favorite local spots.</p></div><div><h4>Quick links</h4><ul><li><a href="home_screen.html">Home</a></li><li><a href="search_screen.html">Restaurants</a></li><li><a href="asian_dish.html">Categories</a></li><li><a href="home_screen.html">Promotions</a></li></ul></div><div><h4>Support</h4><ul><li><a href="home_screen.html">Help Center</a></li><li><a href="home_screen.html">Contact Us</a></li><li><a href="home_screen.html">Terms</a></li><li><a href="home_screen.html">Privacy Policy</a></li></ul></div><div><h4>Follow</h4><ul><li>Instagram</li><li>Facebook</li><li>Twitter</li></ul></div></div><div class="container footer-bottom">© 2026 DirkMhob. Crafted for modern food delivery.</div></footer><script>const searchInput=document.getElementById('searchInput');const searchField=document.getElementById('searchField');const cards=Array.from(document.querySelectorAll('.card'));const filterCards=()=>{const term=(searchInput.value+' '+searchField.value).toLowerCase();cards.forEach(card=>{const text=`${card.dataset.name} ${card.dataset.cuisine}`.toLowerCase();card.style.display=text.includes(term)?'block':'none';});};searchInput.addEventListener('input',filterCards);searchField.addEventListener('input',filterCards);document.querySelectorAll('.fav-btn').forEach(btn=>btn.addEventListener('click',()=>{btn.textContent=btn.textContent==='♡'?'♥':'♡';}));</script></body></html>'''
}
for name, content in files.items():
    (root / name).write_text(content, encoding='utf-8')
print('Updated', len(files), 'files')
