import requests


API_key = "aab2877070aee99f712d919c3a0af574"

def get_data(city, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    new_days = 8 * days
    filtered_data = filtered_data[:new_days]
    return filtered_data


