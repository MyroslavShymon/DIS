import requests
import matplotlib.pyplot as plt

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
    else:
        print("No weather data to visualize.")

def main():
    api_key = "a6d5f2eaa08ad11b9daf96341ead5d82"  # API ключ OpenWeatherMap
    city = input("Enter city name: ")  # Запитуємо користувача ввести назву міста
    weather_data = get_weather(api_key, city)
    visualize_weather(weather_data, city)

if __name__ == "__main__":
    main()