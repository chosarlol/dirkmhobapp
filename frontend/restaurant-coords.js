/*!
 * DirkMhob — Known Restaurant Coordinates
 * Add real GPS coords here so maps don't rely on Nominatim guessing.
 * Keys are lowercase restaurant names (partial matches work via getKnownRestCoords).
 */
(function (window) {
    var COORDS = {
        'brown - tk avenue': { lat: 11.5832840, lng: 104.8986662 },
        'brown tk avenue':   { lat: 11.5832840, lng: 104.8986662 },
        'brown tk avenue':   { lat: 11.5832840, lng: 104.8986662 },
        'brown':             { lat: 11.5832840, lng: 104.8986662 },
    };

    /**
     * Returns { lat, lng } for a known restaurant name, or null if not found.
     * Tries exact lowercase match first, then substring match.
     */
    function getKnownRestCoords(name) {
        if (!name) return null;
        var key = name.toLowerCase().trim();
        if (COORDS[key]) return COORDS[key];
        /* substring fallback: "Brown - TK Avenue (Branch 2)" still matches "brown" */
        for (var k in COORDS) {
            if (key.indexOf(k) !== -1 || k.indexOf(key) !== -1) return COORDS[k];
        }
        return null;
    }

    window.KNOWN_RESTAURANT_COORDS = COORDS;
    window.getKnownRestCoords      = getKnownRestCoords;
}(window));
