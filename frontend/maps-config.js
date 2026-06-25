// Google Maps API Configuration
// Replace 'YOUR_GOOGLE_MAPS_API_KEY_HERE' with your actual key
// Get a key at: https://console.cloud.google.com/ → APIs & Services → Credentials
const MAPS_CONFIG = {
    apiKey: 'YOUR_GOOGLE_MAPS_API_KEY_HERE',
    // Delivery coordinates (Phnom Penh area)
    restaurant: { lat: 11.5656, lng: 104.9282 },   // KFC TK Avenue
    customer:   { lat: 11.5450, lng: 104.9100 },   // Customer location
    driver:     { lat: 11.5580, lng: 104.9205 }    // Driver initial position
};
