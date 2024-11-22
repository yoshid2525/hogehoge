import requests

def weather_command(command):
    base_url= 'https://weather.tsukumijima.net/api/forecast'
    city_code='410020'
    url= '{}?city={}'.format(base_url,city_code)
    r = requests.get(url) 
    weather_data=r.json()

    city=weather_data["location"]["city"]
    label=weather_data["forecasts"][0]["dateLabel"]
    telop=weather_data["forecasts"][0]["telop"]
    response = "今日の天気は{}にゃ。".format(weather_data)
    return response


