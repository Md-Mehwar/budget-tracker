// docs/frontend/app.js

const BASE_URL = "https://congenial-space-chainsaw-7v64r99x9943w67q-8001.app.github.dev";

async function fetchCategoryTotals() {
    try {
        const response = await fetch(`${BASE_URL}/stats/by-category?month=2025-12&user_id=1`);
        const data = await response.json();
        console.log("Fetched data:", data);

        if (data.length === 0) {
            document.getElementById("categoryChart").remove();
            document.body.insertAdjacentHTML("beforeend",
                "<p>No spending data found for this month.</p>");
            return;
        }

        drawPieChart(data);

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function drawPieChart(data) {
    const ctx = document.getElementById("categoryChart");
    const labels = data.map(i => i.category);
    const totals = data.map(i => i.total);

    new Chart(ctx, {
        type: "pie",
        data: {
            labels,
            datasets: [{ data: totals }]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: "bottom" } }
        }
    });
}

fetchCategoryTotals();
