# request helps you to get some details through network

import requests
import json
import win32com.client as wincom


city = input(" Enter thr city for which  weather is required")
url = f"https://api.weatherapi.com/v1/current.json?key=af90996496c24b1ca50183550230307&q={city}"

r = requests.get(url)

wdict = json.loads(r.text)
w = (wdict["current"]["temp_c"])
e = (wdict["current"]["humidity"])
f = (wdict['current']['precip_in'])
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(f"The current weather in{city} is {w} degrees ")
speak.Speak(f"Current precipitation in{city} is {f} percent")
speak.Speak(f"Humidity in{city} is {e}")


