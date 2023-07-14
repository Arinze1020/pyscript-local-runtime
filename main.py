# IP = 54f3e373ec3d3556c41a462d6ab1d3c9

#OPENWARED = 47e28d589c912d35b8aed44a6681c3c2

from js import XMLHttpRequest
import json
from time import gmtime, strftime

today_time = strftime("%a, %H:%M, %d %b", gmtime())
document.getElementById("time").innerText = today_time

#display(today_time, target="time")

def make_request(url):
    req = XMLHttpRequest.new(url)
    req.open("GET", url, False)
    req.send(None)
    output = str(req.response)
    return output

def get_ip():
    out_put = make_request('https://api.ipgeolocation.io/ipgeo?apiKey=c5353e5225f64d51895f9dde3389ca97')
    ip_address = json.loads(out_put)
    #display(IP['ip'], target="location")
    return(ip_address)


def get_weather():
    lat = get_ip()['latitude']
    lon =  get_ip()['longitude']
    API_key =  '47e28d589c912d35b8aed44a6681c3c2'
    out_put = make_request(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
    weather = json.loads(out_put)
    return weather

def display_parameters():
    document.getElementById("temp").innerText = str(round(get_weather()['main']['temp_min']-273.15))+'°'
    document.getElementById("location").innerText = get_weather()['name']
    document.getElementById("cloud_info").innerText = str(get_weather()['weather'][0]['description']).title()
    document.getElementById("wind_speed").innerText = str(get_weather()['wind']['speed'])+' '+'km/h'
    document.getElementById("pressure").innerText = str(get_weather()['main']['pressure'])+' '+'hPa'
    document.getElementById("hummdity").innerText = str(get_weather()['main']['humidity'])+' '+'%'
    #document.getElementById("location").innerText = get_weather()['name']
    #display(get_weather()['name'], target="location")
    #display(str(get_weather()['weather'][0]['description']).title(), target="cloud_info")
    #display(str(get_weather()['wind']['speed'])+' '+'km/h', target="wind_speed")
    #display(str(get_weather()['main']['humidity'])+' '+'%', target="hummdity")
    #display(str(get_weather()['main']['pressure'])+' '+'hPa', target="pressure")
    #display(str(round(get_weather()['main']['temp_min']-273.15))+'°',target="temp")


if __name__ == "__main__":
    display_parameters()
    

