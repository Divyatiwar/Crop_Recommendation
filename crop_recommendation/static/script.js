// Get the input elements
const nitrogenInput = document.getElementById('N');
const phosphorusInput = document.getElementById('P');
const potassiumInput = document.getElementById('K');
const temperatureInput = document.getElementById('temperature');
const humidityInput = document.getElementById('humidity');
const phInput = document.getElementById('ph');
const rainfallInput = document.getElementById('rainfall');

// Initialize the chart
const ctx = document.getElementById('soilChart').getContext('2d');
const soilChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Nitrogen (N)', 'Phosphorus (P)', 'Potassium (K)', 'Temperature', 'Humidity', 'pH', 'Rainfall'],
        datasets: [{
            label: 'Soil & Environmental Factors',
            data: [50, 30, 20, 25, 75, 6, 300],  // Initial dummy data
            backgroundColor: ['#2d6a4f', '#40916c', '#52b788', '#74c69d', '#95d5b2', '#b7e4c7', '#d8f3dc'],
            borderColor: ['#1b4332'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { beginAtZero: true }
        }
    }
});

// Function to update the chart data based on input values
function updateChart() {
    // Get the current values from the input fields
    const nitrogenValue = nitrogenInput.value || 0;
    const phosphorusValue = phosphorusInput.value || 0;
    const potassiumValue = potassiumInput.value || 0;
    const temperatureValue = temperatureInput.value || 0;
    const humidityValue = humidityInput.value || 0;
    const phValue = phInput.value || 0;
    const rainfallValue = rainfallInput.value || 0;

    // Update the chart data
    soilChart.data.datasets[0].data = [
        nitrogenValue,
        phosphorusValue,
        potassiumValue,
        temperatureValue,
        humidityValue,
        phValue,
        rainfallValue
    ];

    // Update the chart to reflect the new values
    soilChart.update();
}