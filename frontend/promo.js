/*!
 * DirkMhob — Promo Module  v1.0
 * ─────────────────────────────────────────────────────
 * Single source of truth: localStorage key  "activePromo"
 *
 * Promotion types:
 *   PERCENT_OFF   — x% off subtotal, optional dollar cap
 *   FREE_DELIVERY — delivery fee becomes $0
 *   FLAT_OFF      — fixed dollar amount off subtotal
 *
 * Load this file on every page that shows prices.
 * Call DirkPromo.calculateDiscount(subtotal, baseDelivery)
 * instead of DirkCart.calculateDiscount().
 */
(function (window) {
    'use strict';

    var PROMO_KEY = 'activePromo';

    /* ── Promotion catalog ───────────────────────────── */
    var CATALOG = {
        'WEEKEND50': {
            code: 'WEEKEND50',
            label: 'Weekend Deal',
            type: 'PERCENT_OFF',
            value: 50,
            cap: 7.62,
            minOrder: 0,
            freeDelivery: false,
            expires: '2026-12-31',
            description: '50% OFF your order'
        },
        'FREEDEL': {
            code: 'FREEDEL',
            label: 'Lunch Rush',
            type: 'FREE_DELIVERY',
            value: 0,
            cap: 0,
            minOrder: 0,
            freeDelivery: true,
            expires: '2026-12-31',
            description: 'Free Delivery on your order'
        },
        'DIRK50': {
            code: 'DIRK50',
            label: '50% OFF Voucher',
            type: 'PERCENT_OFF',
            value: 50,
            cap: 7.62,
            minOrder: 0,
            freeDelivery: false,
            expires: '2026-12-31',
            description: '50% OFF on your order'
        },
        'SAVE50': {
            code: 'SAVE50',
            label: '50% OFF Voucher',
            type: 'PERCENT_OFF',
            value: 50,
            cap: 7.62,
            minOrder: 0,
            freeDelivery: false,
            expires: '2026-12-31',
            description: '50% OFF on your order'
        },
        'TEXAS10': {
            code: 'TEXAS10',
            label: 'Texas Chicken 50% OFF',
            type: 'PERCENT_OFF',
            value: 50,
            cap: 7.62,
            minOrder: 10,
            restaurantId: 'texas_chicken',
            freeDelivery: false,
            expires: '2026-12-31',
            description: '50% OFF at Texas Chicken (min. order $10)'
        },
        'NEWUSER': {
            code: 'NEWUSER',
            label: 'New User Discount',
            type: 'PERCENT_OFF',
            value: 50,
            cap: 10.00,
            minOrder: 0,
            freeDelivery: false,
            expires: '2026-12-31',
            description: '50% OFF for new users (up to $10)'
        }
    };

    /* ── Core read / write ───────────────────────────── */

    function getActivePromo() {
        try {
            return JSON.parse(localStorage.getItem(PROMO_KEY)) || null;
        } catch (e) {
            return null;
        }
    }

    function setActivePromo(promo) {
        localStorage.setItem(PROMO_KEY, JSON.stringify(promo));
        console.log('[PROMO] Stored active promo:', promo.code, promo.label);
    }

    function clearPromo() {
        localStorage.removeItem(PROMO_KEY);
        console.log('[PROMO] Active promotion cleared');
    }

    function isExpired(promo) {
        if (!promo || !promo.expires) return false;
        return new Date(promo.expires + 'T23:59:59') < new Date();
    }

    /* ── Apply by catalog key (promo card clicks) ────── */

    function applyByKey(key) {
        var promo = CATALOG[key];
        console.log('[PROMO] applyByKey()', key, '→', promo ? 'found' : 'not found');
        if (!promo) {
            return { success: false, message: 'Unknown promotion.' };
        }
        if (isExpired(promo)) {
            console.warn('[PROMO] Promo expired:', key, 'expires:', promo.expires);
            return { success: false, message: 'This promotion has expired.' };
        }
        setActivePromo(promo);
        return { success: true, promo: promo, message: promo.description + ' applied!' };
    }

    /* ── Apply by coupon code string (text input) ────── */

    function applyByCode(code) {
        code = (code || '').trim().toUpperCase();
        console.log('[PROMO] applyByCode()', JSON.stringify(code));
        if (!code) {
            return { success: false, message: 'Please enter a promo code.' };
        }
        var promo = CATALOG[code];
        if (!promo) {
            console.warn('[PROMO] Invalid code:', code);
            return { success: false, message: 'Invalid promo code "' + code + '".' };
        }
        if (isExpired(promo)) {
            console.warn('[PROMO] Expired code:', code, 'expires:', promo.expires);
            return { success: false, message: 'Promo code "' + code + '" has expired.' };
        }
        setActivePromo(promo);
        return { success: true, promo: promo, message: promo.description + ' applied!' };
    }

    /* ── Price calculation ───────────────────────────── */

    /**
     * Returns { discount, delivery, label, promoCode, type }.
     * Always call this instead of DirkCart.calculateDiscount().
     *
     * @param {number} subtotal      - sum of item prices
     * @param {number} baseDelivery  - normal delivery fee (DirkCart.DELIVERY_FEE)
     */
    function calculateDiscount(subtotal, baseDelivery) {
        var promo = getActivePromo();
        console.log('[PROMO] calculateDiscount() subtotal=$' + subtotal.toFixed(2),
                    'baseDelivery=$' + baseDelivery.toFixed(2),
                    'activePromo:', promo ? promo.code : 'none');

        if (!promo) {
            console.log('[PROMO] No active promo → discount $0');
            return { discount: 0, delivery: baseDelivery, label: null, promoCode: null, type: null };
        }

        if (isExpired(promo)) {
            console.warn('[PROMO] Stored promo expired, clearing');
            clearPromo();
            return { discount: 0, delivery: baseDelivery, label: null, promoCode: null, type: null };
        }

        if (promo.minOrder && subtotal < promo.minOrder) {
            console.log('[PROMO] Subtotal $' + subtotal + ' below minOrder $' + promo.minOrder + ' → promo not applied');
            return {
                discount: 0, delivery: baseDelivery, label: null, promoCode: null, type: null,
                belowMin: true, minOrder: promo.minOrder
            };
        }

        var discount = 0;
        var delivery = baseDelivery;

        if (promo.type === 'PERCENT_OFF') {
            discount = subtotal * (promo.value / 100);
            if (promo.cap) discount = Math.min(discount, promo.cap);
            console.log('[PROMO] PERCENT_OFF ' + promo.value + '% → discount=$' + discount.toFixed(2));

        } else if (promo.type === 'FREE_DELIVERY') {
            delivery = 0;
            discount = 0;
            console.log('[PROMO] FREE_DELIVERY → delivery fee $0');

        } else if (promo.type === 'FLAT_OFF') {
            discount = Math.min(promo.value, subtotal);
            console.log('[PROMO] FLAT_OFF $' + promo.value + ' → discount=$' + discount.toFixed(2));
        }

        console.log('[PROMO] Result: delivery=$' + delivery.toFixed(2) + ' discount=$' + discount.toFixed(2));
        return {
            discount:  discount,
            delivery:  delivery,
            label:     promo.label,
            promoCode: promo.code,
            type:      promo.type
        };
    }

    /* ── Public API ──────────────────────────────────── */
    window.DirkPromo = {
        CATALOG:           CATALOG,
        getActivePromo:    getActivePromo,
        setActivePromo:    setActivePromo,
        clearPromo:        clearPromo,
        isExpired:         isExpired,
        applyByKey:        applyByKey,
        applyByCode:       applyByCode,
        calculateDiscount: calculateDiscount
    };

}(window));
