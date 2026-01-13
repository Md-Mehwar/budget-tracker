// frontend/app.js
// Fetches analytics data from FastAPI and logs it for testing.

// 1. Replace this with your actual Codespaces URL:
const BASE_URL = "https://humble-fiesta-7v57pp95595q37x7-8001.app.github.dev";

// 2. Function to fetch category totals from your FastAPI API
async function fetchCategoryTotals() {
    try {
        const response = await fetch(`${BASE_URL}/stats/by-category?month=2025-12&user_id=1`);
        const data = await response.json();
        console.log("Fetched data:", data);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// 3. Call the function when the page loads
fetchCategoryTotals();
