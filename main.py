from kivymd.app import MDApp
from tkinter.ttk import Style
from kivy.app import App
from kivy.lang.builder import Builder 
import requests
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.toast import toast

Window.size = (350,600)

class request(MDApp):
    def build(self):
        '''location = ObjectProperty()
        temperature = ObjectProperty()
        weather = ObjectProperty()'''
        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Tehran&appid=44e44e807c21dbce14c4cbcc02723dcc')                
            json = response.json()
            style = Builder.load_file("mykivy.kv")
            print(json) 
            if json['cod']!= '404':
                style.location.text = str(json['name']+","+json['sys']['country'])
                style.temperature.text = str(round(json['main']['temp']-273) )+ "°" #temperature in degrees
                style.weather.text = str(json['weather'][0]['main'])
                style.humidity.text = str(json['main']['humidity'])+"%"
                style.wind.text = str(json['wind']['speed'])
            else : 
                style.location.text = str(json['code']+","+json['message'])
            return style
        except requests.ConnectionError :
            toast("Couldn't connect to server")


request().run()