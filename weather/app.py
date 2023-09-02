import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
API_KEY = '0f8c88146a435b8db9d6af1cacbbc02a'

# Cache to store weather data for a limited time
weather_cache = {}

def get_weather_data(city):
    if city in weather_cache:
        return weather_cache[city]
    
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            "city": data["name"],
            "temperature": f"{data['main']['temp']}°C",
            "description": data["weather"][0]["description"].capitalize()
        }
        weather_cache[city] = weather_data
        return weather_data
    else:
        return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather_data(city)
            if weather_data is not None:
                return render_template('weather.html', weather_data=weather_data)
            else:
                error_message = "Weather data not available for the specified city."
                return render_template('weather.html', error_message=error_message)
        else:
            error_message = "Please enter a city."
            return render_template('weather.html', error_message=error_message)

    return render_template('weather.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
