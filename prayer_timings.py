import requests

def get_prayer_timings(city, country="Pakistan"):
    api_url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        timings = data['data']['timings']
        return timings
    return None 
    



 
