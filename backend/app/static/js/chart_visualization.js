async function fetchData() {
    const response = await fetch('/plot-data');
    const data = await response.json();

    const timestamps = data.map(d => new Date(d.timestamp).toLocaleString());
    const temperatures = data.map(d => d.temperature);
    const pressures = data.map(d => d.pressure);

    new Chart(document.getElementById('temperatureChart'), {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Temperature (°C)',
                data: temperatures,
                borderColor: 'red',
                fill: false
            }]
        },
        options: {
            scales: {
                x: { display: true, title: { display: true, text: 'Time' }},
                y: { display: true, title: { display: true, text: 'Temperature' }}
            }
        }
    });

    new Chart(document.getElementById('pressureChart'), {
        type: 'line',
        data: {
            labels: timestamps,
            datasets: [{
                label: 'Pressure (hPa)',
                data: pressures,
                borderColor: 'blue',
                fill: false
            }]
        },
        options: {
            scales: {
                x: { display: true, title: { display: true, text: 'Time' }},
                y: { display: true, title: { display: true, text: 'Pressure' }}
            }
        }
    });
}

fetchData();
