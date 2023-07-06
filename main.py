from kivymd.app import MDApp
from kivy.app import App
from kivy.lang.builder import Builder 
import requests
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


Window.size = (350,600)

class request(MDApp):
    def show(self):
        self.dialog = MDDialog(
                title = "About",
                text="programmer: Novin Nekuee",
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        on_release = self.close,
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="More",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()
    def close(self , obj):
        self.dialog.dismiss()
    def search_weather(self):
        style = ""
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.style.city_name.text}&appid=44e44e807c21dbce14c4cbcc02723dcc")                
            json = response.json()
            print(json) 
            if json['cod']!= '404' and self.style.city_name.text!="":
                self.style.location.text = str(json['name']+","+json['sys']['country'])
                self.style.temperature.text = str(round(json['main']['temp']-273) )+ "°" #temperature in degrees
                self.style.weather.text = str(json['weather'][0]['main'])
                self.style.humidity.text = str(json['main']['humidity'])+"%"
                self.style.wind.text = str(json['wind']['speed'])
                self.style.weather_Image.source = "files/" + str(json['weather'][0]['icon']) + "@2x.png"
            else : 
                self.style.location.text = str(json['cod']+","+json['message'])
            return self.style
        except requests.ConnectionError :
            toast("Couldn't connect to server")


    def build(self):
        '''location = ObjectProperty()
        temperature = ObjectProperty()
        weather = ObjectProperty()'''
        try:
            response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Tehran&appid=44e44e807c21dbce14c4cbcc02723dcc')                
            json = response.json()
            self.style = Builder.load_file("mykivy.kv")
            print(json) 
            if json['cod']!= '404':
                self.style.location.text = str(json['name']+","+json['sys']['country'])
                self.style.temperature.text = str(round(json['main']['temp']-273) )+ "°" #temperature in degrees
                self.style.weather.text = str(json['weather'][0]['main'])
                self.style.humidity.text = str(json['main']['humidity'])+"%"
                self.style.wind.text = str(json['wind']['speed'])
                self.style.weather_Image.source = "files/" + str(json['weather'][0]['icon']) + "@2x.png"
            else : 
                self.style.location.text = str(json['code']+","+json['message'])
            return self.style
        except requests.ConnectionError :
            toast("Couldn't connect to server")


request().run()