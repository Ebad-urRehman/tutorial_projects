api_key = "5434f3963f045eff9b0a68daa4b365d3"

def get_data(place, days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"