import requests


API_key = ""

def get_data(city, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    new_days = 8 * days
    filtered_data = filtered_data[:new_days]
    return filtered_data


