/*!
 * DirkMhob — Global Cart Module  v1.0
 * ─────────────────────────────────────────────────────
 * Single source of truth: localStorage key  "cart"
 *
 * Every restaurant page and checkout page should load
 * this file and use window.DirkCart.* functions only.
 * Never write raw localStorage cart data elsewhere.
 */
(function (window) {
    'use strict';

    /* ── Constants ───────────────────────────────────── */
    var CART_KEY     = 'cart';
    var DELIVERY_FEE = 2.50;
    var DISCOUNT_CAP = 7.62;   // 50 % OFF voucher cap (matches demo order total)

    /* ── Core read / write ───────────────────────────── */

    /**
     * Return current cart array from localStorage.
     * Returns [] on any error so callers never need to null-check.
     *
     * Cart item schema:
     *   { restaurantId, restaurantName, name, price, quantity, emoji }
     */
    function getCart() {
        try {
            return JSON.parse(localStorage.getItem(CART_KEY)) || [];
        } catch (e) {
            return [];
        }
    }

    /** Persist the cart array to localStorage. */
    function saveCart(cart) {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
    }

    /** Remove the cart entry from localStorage entirely. */
    function clearCart() {
        localStorage.removeItem(CART_KEY);
    }

    /* ── Mutations ───────────────────────────────────── */

    /**
     * Add an item to the cart.
     * If an identical item (same restaurantId + name) already exists,
     * its quantity is incremented instead of duplicating the entry.
     *
     * @param {{ restaurantId:string, restaurantName:string, name:string,
     *            price:number, quantity:number, emoji:string }} item
     */
    function addToCart(item) {
        var cart = getCart();
        var idx  = findIndex(cart, item.restaurantId, item.name);
        if (idx > -1) {
            cart[idx].quantity += item.quantity;
        } else {
            cart.push({
                restaurantId:   item.restaurantId,
                restaurantName: item.restaurantName,
                name:           item.name,
                price:          Number(item.price),
                quantity:       Number(item.quantity),
                emoji:          item.emoji || '🍽️'
            });
        }
        saveCart(cart);
        return cart;
    }

    /**
     * Set the quantity of a cart item.
     * If quantity ≤ 0, the item is removed from the cart.
     */
    function updateQuantity(restaurantId, name, quantity) {
        quantity = Number(quantity);
        if (quantity <= 0) return removeFromCart(restaurantId, name);
        var cart = getCart();
        var idx  = findIndex(cart, restaurantId, name);
        if (idx > -1) {
            cart[idx].quantity = quantity;
            saveCart(cart);
        }
        return cart;
    }

    /** Remove a specific item from the cart entirely. */
    function removeFromCart(restaurantId, name) {
        var cart = getCart().filter(function (i) {
            return !(i.restaurantId === restaurantId && i.name === name);
        });
        saveCart(cart);
        return cart;
    }

    /* ── Calculations ────────────────────────────────── */

    /** Sum of (price × quantity) for all items. */
    function calculateSubtotal(cart) {
        return (cart || getCart()).reduce(function (s, i) {
            return s + i.price * i.quantity;
        }, 0);
    }

    /**
     * Discount = min(DISCOUNT_CAP, subtotal).
     * Represents the 50 % OFF promo coupon applied in the demo.
     */
    function calculateDiscount(subtotal) {
        return Math.min(DISCOUNT_CAP, subtotal);
    }

    /** Total = subtotal + delivery − discount. */
    function calculateTotal(cart) {
        var sub      = calculateSubtotal(cart);
        var discount = calculateDiscount(sub);
        return sub + DELIVERY_FEE - discount;
    }

    /** Total number of individual units across all items. */
    function getCartCount() {
        return getCart().reduce(function (s, i) { return s + i.quantity; }, 0);
    }

    /* ── Private helpers ─────────────────────────────── */
    function findIndex(cart, restaurantId, name) {
        for (var i = 0; i < cart.length; i++) {
            if (cart[i].restaurantId === restaurantId && cart[i].name === name) return i;
        }
        return -1;
    }

    /* ── Public API ──────────────────────────────────── */
    window.DirkCart = {
        DELIVERY_FEE:      DELIVERY_FEE,
        DISCOUNT_CAP:      DISCOUNT_CAP,
        getCart:           getCart,
        saveCart:          saveCart,
        clearCart:         clearCart,
        addToCart:         addToCart,
        updateQuantity:    updateQuantity,
        removeFromCart:    removeFromCart,
        calculateSubtotal: calculateSubtotal,
        calculateDiscount: calculateDiscount,
        calculateTotal:    calculateTotal,
        getCartCount:      getCartCount
    };

}(window));
