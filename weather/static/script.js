function getWeather() {
    // ... (existing code to fetch weather data)

    // Determine the weather condition (you might need to adjust this logic)
    let weatherCondition = 'sunny';
    if (weatherData.description.includes('rain')) {
        weatherCondition = 'rainy';
    }

    // Display the weather information with appropriate styling
    const weatherInfo = document.getElementById('weatherInfo');
    weatherInfo.innerHTML = `
        <div class="weather-card">
            <h2>${weatherData.city}</h2>
            <div class="weather-icon ${weatherCondition}">&#9733;</div>
            <p class="weather-description">${weatherData.description}</p>
            <p class="temperature">${weatherData.temperature}</p>
        </div>
    `;

    weatherInfo.classList.add('show');
}
