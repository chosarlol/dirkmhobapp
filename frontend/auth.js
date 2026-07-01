/*!
 * DirkMhob — Auth Module  v1.0
 * ─────────────────────────────────────────────────────
 * Single source of truth: localStorage key  "dirkmhob_user"
 *
 * Every page loads this file and the navbar's #nav-auth
 * slot is auto-populated based on auth state.
 * Never write raw auth data to localStorage elsewhere.
 */
(function (window) {
    'use strict';

    var AUTH_KEY = 'dirkmhob_user';

    /* ── Core read / write ───────────────────────────── */

    function getUser() {
        try {
            return JSON.parse(localStorage.getItem(AUTH_KEY)) || null;
        } catch (e) {
            return null;
        }
    }

    function isLoggedIn() {
        return getUser() !== null;
    }

    function login(userData) {
        var user = {
            name:     userData.name     || 'Guest User',
            email:    userData.email    || '',
            phone:    userData.phone    || '',
            address:  userData.address  || '',
            avatar:   userData.avatar   || '👤',
            role:     userData.role     || 'customer',
            joinedAt: userData.joinedAt || new Date().toISOString()
        };
        localStorage.setItem(AUTH_KEY, JSON.stringify(user));
        return user;
    }

    function logout() {
        localStorage.removeItem(AUTH_KEY);
        window.location.href = 'home_screen.html';
    }

    function updateUser(data) {
        var current = getUser() || {};
        var key;
        for (key in data) {
            if (Object.prototype.hasOwnProperty.call(data, key)) {
                current[key] = data[key];
            }
        }
        localStorage.setItem(AUTH_KEY, JSON.stringify(current));
        return current;
    }

    /* ── Navbar UI ───────────────────────────────────── */

    function injectStyles() {
        if (document.getElementById('dm-auth-styles')) return;
        var s = document.createElement('style');
        s.id = 'dm-auth-styles';
        s.textContent =
            /* shared button base */
            '.dm-auth-wrap{display:flex;align-items:center;gap:0.55rem;}' +
            '.dm-btn{display:inline-flex;align-items:center;justify-content:center;' +
            'border:none;border-radius:999px;padding:0.65rem 1.05rem;font-weight:700;' +
            'cursor:pointer;text-decoration:none;font-family:inherit;font-size:0.88rem;' +
            'transition:transform .18s,box-shadow .18s;white-space:nowrap;}' +
            '.dm-btn:hover{transform:translateY(-1px);}' +
            /* active nav link pill */
            '.nav-links a.dm-nav-active{color:#0077c8 !important;' +
            'background:rgba(0,119,200,0.1);' +
            'padding:0.3em 0.75em;border-radius:999px;' +
            'box-shadow:0 3px 10px rgba(0,119,200,0.15);}' +
            /* guest buttons */
            '.dm-login{background:#fff;color:#0077c8;border:1.5px solid rgba(0,119,200,0.22);}' +
            '.dm-login:hover{border-color:#0077c8;box-shadow:0 4px 14px rgba(0,119,200,0.14);}' +
            '.dm-signup{background:linear-gradient(135deg,#0077c8,#005fa0);color:#fff;' +
            'box-shadow:0 8px 20px rgba(0,119,200,0.22);}' +
            /* user wrapper + avatar button */
            '.dm-user-wrap{position:relative;}' +
            '.dm-avatar-btn{display:flex;align-items:center;gap:0.5rem;background:#fff;' +
            'border:1.5px solid #e2e8f0;border-radius:999px;' +
            'padding:0.38rem 0.75rem 0.38rem 0.38rem;cursor:pointer;font-weight:700;' +
            'font-size:0.88rem;color:#1e293b;transition:all .2s;' +
            'font-family:inherit;}' +
            '.dm-avatar-btn:hover{border-color:#0077c8;' +
            'box-shadow:0 4px 14px rgba(0,119,200,0.14);}' +
            '.dm-avatar-circle{width:30px;height:30px;border-radius:50%;' +
            'background:linear-gradient(135deg,#0077c8,#ff6b35);' +
            'display:flex;align-items:center;justify-content:center;' +
            'font-size:0.95rem;flex-shrink:0;color:#fff;}' +
            '.dm-chevron{color:#94a3b8;font-size:0.7rem;' +
            'transition:transform .2s;display:inline-block;}' +
            '.dm-user-wrap.open .dm-chevron{transform:rotate(180deg);}' +
            /* dropdown */
            '.dm-dropdown{position:absolute;right:0;top:calc(100% + 10px);' +
            'min-width:224px;background:#fff;border:1px solid #e2e8f0;' +
            'border-radius:18px;box-shadow:0 16px 48px rgba(15,23,42,0.13);' +
            'padding:6px 0;z-index:9999;' +
            'opacity:0;transform:translateY(-8px) scale(0.97);pointer-events:none;' +
            'transition:opacity .18s ease,transform .18s cubic-bezier(.34,1.56,.64,1);}' +
            '.dm-user-wrap.open .dm-dropdown{opacity:1;transform:translateY(0) scale(1);' +
            'pointer-events:all;}' +
            /* dropdown internals */
            '.dm-dd-head{padding:12px 16px 10px;border-bottom:1px solid #f1f5f9;}' +
            '.dm-dd-name{font-weight:800;color:#1e293b;font-size:0.9rem;' +
            'overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}' +
            '.dm-dd-email{font-size:0.78rem;color:#64748b;margin-top:1px;' +
            'overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}' +
            '.dm-dd-item{display:flex;align-items:center;gap:10px;' +
            'padding:10px 16px;color:#1e293b;font-size:0.88rem;font-weight:600;' +
            'text-decoration:none;cursor:pointer;background:none;border:none;' +
            'width:100%;text-align:left;font-family:inherit;' +
            'transition:background .14s;}' +
            '.dm-dd-item:hover{background:#f8fafc;}' +
            '.dm-dd-item.dm-danger{color:#ef4444;}' +
            '.dm-dd-item.dm-danger:hover{background:#fef2f2;}' +
            '.dm-dd-sep{height:1px;background:#f1f5f9;margin:4px 0;}';
        document.head.appendChild(s);
    }

    function mountNavAuth() {
        var container = document.getElementById('nav-auth');
        if (!container) return;

        injectStyles();
        var user = getUser();

        if (!user) {
            container.innerHTML =
                '<div class="dm-auth-wrap">' +
                '<a class="dm-btn dm-login" href="login.html">Login</a>' +
                '<a class="dm-btn dm-signup" href="signup.html">Sign Up</a>' +
                '</div>';
            return;
        }

        /* Logged-in: build avatar + dropdown */
        var parts = user.name.split(' ');
        var initials = parts.map(function (p) { return p[0] || ''; }).slice(0, 2).join('').toUpperCase();
        var displayAvatar = (user.avatar && user.avatar !== '👤') ? user.avatar : initials;
        var firstName = parts[0] || 'User';

        var role = user.role || 'customer';

        /* Build role-specific menu items */
        var roleItems = '';
        if (role === 'superadmin' || role === 'moderator') {
            roleItems =
                '<a class="dm-dd-item" href="admin_dashboard.html" style="color:#0077c8;font-weight:800;">&#128187;&nbsp; Admin Dashboard</a>' +
                '<div class="dm-dd-sep"></div>';
        } else if (role === 'shop_owner') {
            roleItems =
                '<a class="dm-dd-item" href="shop_dashboard.html" style="color:#16a34a;font-weight:800;">&#127981;&nbsp; Shop Dashboard</a>' +
                '<div class="dm-dd-sep"></div>';
        }

        container.innerHTML =
            '<div class="dm-user-wrap" id="dm-user-wrap">' +
            '  <button class="dm-avatar-btn" id="dm-avatar-btn" aria-haspopup="true" aria-expanded="false">' +
            '    <div class="dm-avatar-circle">' + displayAvatar + '</div>' +
            '    <span>' + escHtml(firstName) + '</span>' +
            '    <span class="dm-chevron">&#9660;</span>' +
            '  </button>' +
            '  <div class="dm-dropdown" id="dm-dropdown" role="menu">' +
            '    <div class="dm-dd-head">' +
            '      <div class="dm-dd-name">' + escHtml(user.name) + '</div>' +
            '      <div class="dm-dd-email">' + escHtml(user.email || role) + '</div>' +
            '    </div>' +
            roleItems +
            '    <a class="dm-dd-item" href="profile_screen.html">&#128100;&nbsp; My Profile</a>' +
            '    <a class="dm-dd-item" href="profile_screen.html#orders">&#128203;&nbsp; My Orders</a>' +
            '    <a class="dm-dd-item" href="cart_screen.html">&#128722;&nbsp; My Cart</a>' +
            '    <div class="dm-dd-sep"></div>' +
            '    <button class="dm-dd-item dm-danger" id="dm-logout-btn">&#128682;&nbsp; Log Out</button>' +
            '  </div>' +
            '</div>';

        var wrap   = document.getElementById('dm-user-wrap');
        var btn    = document.getElementById('dm-avatar-btn');
        var logBtn = document.getElementById('dm-logout-btn');

        btn.addEventListener('click', function (e) {
            e.stopPropagation();
            var isOpen = wrap.classList.toggle('open');
            btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });

        logBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            logout();
        });

        document.addEventListener('click', function (e) {
            if (wrap && !wrap.contains(e.target)) {
                wrap.classList.remove('open');
                if (btn) btn.setAttribute('aria-expanded', 'false');
            }
        });
    }

    function escHtml(str) {
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    /* ── Active nav link ─────────────────────────────── */

    function applyActiveNav() {
        var page = window.location.pathname.split('/').pop().split('?')[0] || 'home_screen.html';
        var hash = window.location.hash;  /* e.g. '#promotions' or '' */
        var links = document.querySelectorAll('.nav-links a');

        links.forEach(function (l) { l.classList.remove('dm-nav-active'); });

        /* 1. Exact hash match — handles same-page section links like href="#promotions" */
        if (hash) {
            var hashMatched = false;
            links.forEach(function (link) {
                if ((link.getAttribute('href') || '') === hash) {
                    link.classList.add('dm-nav-active');
                    hashMatched = true;
                }
            });
            if (hashMatched) return;
        }

        /* 2. File-based mapping for cross-page links */
        var map = {
            'home_screen.html':    'home_screen.html',
            'search_screen.html':  'search_screen.html',
            'res_brown.html':      'search_screen.html',
            'res_kfc.html':        'search_screen.html',
            'res_texas.html':      'search_screen.html',
            'asian_dish.html':     'asian_dish.html',
            'khmer_dish.html':     'asian_dish.html',
            'pastry_dish.html':    'asian_dish.html',
            'coffee_dish.html':    'asian_dish.html',
            'cart_screen.html':    'cart_screen.html',
            'profile_screen.html': 'profile_screen.html'
        };
        var activeHref = map[page];
        if (!activeHref) return;

        links.forEach(function (link) {
            var href = link.getAttribute('href') || '';
            /* Only match plain file links (no hash), so Promotions/About/Contact
               don't accidentally light up when the file name happens to match */
            if (href.split('#')[0] === activeHref && href.indexOf('#') === -1) {
                link.classList.add('dm-nav-active');
            }
        });
    }

    function markActiveNavLink() {
        if (!document.getElementById('dm-nav-active-styles')) {
            var ns = document.createElement('style');
            ns.id = 'dm-nav-active-styles';
            ns.textContent =
                '.nav-links a.dm-nav-active{color:#0077c8 !important;' +
                'background:rgba(0,119,200,0.1);' +
                'padding:0.3em 0.75em;border-radius:999px;' +
                'box-shadow:0 3px 10px rgba(0,119,200,0.15);' +
                'display:inline-block;}';
            document.head.appendChild(ns);
        }
        applyActiveNav();
        /* Update pill when user clicks a section link (hash changes without page reload) */
        window.addEventListener('hashchange', applyActiveNav);
    }

    document.addEventListener('DOMContentLoaded', mountNavAuth);
    document.addEventListener('DOMContentLoaded', markActiveNavLink);

    /* ── Public API ──────────────────────────────────── */
    window.DirkAuth = {
        getUser:      getUser,
        isLoggedIn:   isLoggedIn,
        login:        login,
        logout:       logout,
        updateUser:   updateUser,
        mountNavAuth: mountNavAuth
    };

}(window));
