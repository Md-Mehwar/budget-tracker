// docs/frontend/app.js
// Fetch category data from FastAPI and draw a pie chart.

// Your FastAPI public URL:
const BASE_URL = "https://congenial-space-chainsaw-7v64r99x9943w67q-8001.app.github.dev/api";



// Fetch data from FastAPI
async function fetchCategoryTotals() {
    try {
        const response = await fetch(`${BASE_URL}/stats/by-category?month=2025-12&user_id=1`);
        const data = await response.json();
        console.log("Fetched data:", data);

        // Pass data to chart function
        drawPieChart(data);

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

// Draw pie chart using Chart.js
function drawPieChart(data) {
    const ctx = document.getElementById("categoryChart");

    // Extract labels and values from JSON
    const labels = data.map(item => item.category);
    const totals = data.map(item => item.total);

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: totals
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

// Run the fetch when the page loads
fetchCategoryTotals();
