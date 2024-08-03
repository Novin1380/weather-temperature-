from kivymd.app import MDApp
from kivy.app import App
from kivy.lang.builder import Builder 
import requests
from kivy.core.window import Window
# from kivy.properties import ObjectProperty
# from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.label import MDLabel
import sqlite3


Window.size = (350,600)

class request(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """ Creating DataBase or connect to one """
        conn = sqlite3.connect("city.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists city (   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city VARCHAR(255) NOT NULL
        )""")
        conn.commit()
        conn.close()
        
        
    
    def show(self):
        self.dialog = MDDialog( 
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="information",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="About me",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(markup=True,
                text= """Designed by: [b]Novin Nekuee[/b]
                contact: [b]Novini.n1380@gmail.com[/b]
Powered by: openwweather api
written with: python-kivy
Just enjoy
made with ❤️"""
                    
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
            ),
            # ---------------------Button container------------------------
            MDDialogButtonContainer(
                MDButton(
                    MDButtonText(text="ok"),
                    style="text",
                    on_release=lambda x: self.dialog.dismiss(),
                ),
                spacing="8dp",
                
            ),)
        self.dialog.open()



    def search_weather(self):
        style = ""
        print(self.root.ids.city_name.text)
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={self.root.ids.city_name.text}&appid=44e44e807c21dbce14c4cbcc02723dcc")                
            json = response.json()
            print(json) 
            print(json['cod'])
            # if json['cod']!= '404' and self.root.ids.city_name.text!="":
            #     self.style.location.text = str(json['name']+","+json['sys']['country'])
            #     self.style.temperature.text = str(round(json['main']['temp']-273) )+ "°" #temperature in degrees
            #     self.style.weather.text = str(json['weather'][0]['main'])
            #     self.style.humidity.text = str(json['main']['humidity'])+"%"
            #     self.style.wind.text = str(json['wind']['speed'])
            #     self.style.weather_Image.source = "files/" + str(json['weather'][0]['icon']) + "@2x.png"
            # else : 
            #     self.style.location.text = str(json['cod']+","+json['message'])
            # return self.style
        except requests.ConnectionError :
            # toast("Couldn't connect to server")
            pass


    def build(self):
        '''location = ObjectProperty()
        temperature = ObjectProperty()
        weather = ObjectProperty()'''
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"
        self.theme_cls.primary_hue = "200"
        self.style = Builder.load_file("main.kv")
        return self.style
        # try:
        #     response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Tehran&appid=44e44e807c21dbce14c4cbcc02723dcc')                
        #     json = response.json()
        #     self.style = Builder.load_file("main.kv")
        #     print(json) 
        #     if json['cod']!= '404':
        #         self.style.location.text = str(json['name']+","+json['sys']['country'])
        #         self.style.temperature.text = str(round(json['main']['temp']-273) )+ "°" #temperature in degrees
        #         self.style.weather.text = str(json['weather'][0]['main'])
        #         self.style.humidity.text = str(json['main']['humidity'])+"%"
        #         self.style.wind.text = str(json['wind']['speed'])
        #         self.style.weather_Image.source = "files/" + str(json['weather'][0]['icon']) + "@2x.png"
        #     else : 
        #         self.style.location.text = str(json['code']+","+json['message'])
        #     return self.style
        # except requests.ConnectionError :
        #     toast("Couldn't connect to server")


request().run()