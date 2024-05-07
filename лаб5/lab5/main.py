import requests
import matplotlib.pyplot as plt
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if "main" in data:
        return data
    else:
        print("Failed to fetch weather data. Check your city name or API key.")
        return None

def visualize_weather(weather_data, city):
    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        weather_description = weather_data["weather"][0]["description"]

        plt.figure(figsize=(8, 6))
        plt.title(f"Current Weather in {city}")

        plt.text(0.5, 0.9, f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_description}",
                 horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.axis('off')
        plt.show()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        return redirect(url_for('weather', city=city, login='is-23fiot-22-112'))  # Redirect with login parameter
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    login = request.args.get('login', '')

    if not city:
        return redirect(url_for('index'))

    api_key = "a6d5f2eaa08ad11b9daf96341ead5d82"  # OpenWeatherMap API key
    weather_data = get_weather(api_key, city)
    visualize_weather(weather_data, city)

    if login == 'is-23fiot-22-112':
        student_info = "Шимків Мирослав Віталійович, 3 курс, група ІС-23"
        return f'<h1>{student_info}</h1>'
    else:
        return "Invalid login."

@app.route('/student-info', methods=['GET'])
def display_student_info():
    login = request.args.get('login', '')
    if login == 'is-23fiot-22-112':
        student_info = "Шимків Мирослав Віталійович, 3 курс, група ІС-23"
        return f'<h1>{student_info}</h1>'
    else:
        return "Invalid login."

if __name__ == "__main__":
    app.run(debug=True)