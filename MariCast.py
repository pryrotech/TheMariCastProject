#imports
import numpy as np
import requests
import asyncio
from env_canada import ECWeather
from tkinter import *
import webbrowser
from pyowm import OWM

''''Initiate window and dimensions, display title and description'''
window = Tk()


window.geometry("650x500")
window.title("MariCast")
window.config(bg="white")

title = Label(window, text="MariCast")
title.config(font=('Arial Bold',40),bg=("white"),fg=("grey"))
title.pack()

sub_text = Label(window,text="An application for marine weather reports")
sub_text.config(font=('Kozuka Gothic Pro M',20),bg=("white"),fg=("blue"))
sub_text.pack() #pack the window for display


def mainMenu():

    '''Retrieve user's coordinates from IP and city'''
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()

    latitude = float(geo_data['latitude'])
    longitude = float(geo_data['longitude'])
    city = str(geo_data['city'])
    #province = str(geo_data['province'])
    print(geo_data)

    '''Print latitude and longitude'''
    print(latitude,longitude)

    owm = OWM('')
    mgr = owm.weather_manager()
    one_call = mgr.one_call(lat=latitude, lon=longitude)

    temperature = one_call.forecast_daily[0].temperature('celsius').get('min','max')

    winds = one_call.forecast_daily[0].wind().get('speed')
    
    waves = 0 #variable for waves
    
    visibility = 0 #variable for visibility
    
    sunset = 0 #variable for sunset
    
    sunrise = 0 #variable for sunrise
    
    humidex = 0
    
    humidity = one_call.current.humidity #variable for humidity
    
    pressure = one_call.current.pressure.get('press') #variable for pressure
    
    conditions = 0


    
    forecast = "Mostly cloudy skies tonight, tapering off to clear skies around 00:00." #variable for forecast
    
    frame = Frame(window)
    frame.pack(side="top", expand=True, fill="both") #pack the window for display

    #label for current marine weather
    Label(frame,text="Current Marine Weather for: ", font=('Helvetica',15)).place(x=3,y=10)
    Label(frame,text=city, font=('Helvetica',15),fg=("blue")).place(x=260,y=10)

    #label for winds variable
    Label(frame,text="Winds:", font=('Arial Bold',10)).place(x=3,y=50)
    Label(frame,text=str(winds)+' knots [STRONG]', font=('Arial Bold',12),fg=("red")).place(x=50,y=48)


    #label for winds with IF statement to gauge level of winds   

    #label for atmospheric conditions
    Label(frame,text="Conditions: ", font=('Arial Bold',10)).place(x=400,y=50)
    Label(frame,text=conditions, font=('Arial Bold',12)).place(x=480,y=47)

    #label for atmospheric pressure
    Label(frame,text="Atmospheric Pressure: ", font=('Arial Bold',10)).place(x=400,y=70)
    Label(frame,text=str(pressure)+" kPa", font=('Arial Bold',12)).place(x=550,y=68)

    #label for temperature
    Label(frame,text="Temperature: ", font=('Arial Bold',10)).place(x=400,y=90)
    Label(frame,text=str(temperature)+"°C", font=('Arial Bold',12)).place(x=500,y=90)

    #label for humidity
    Label(frame,text="Humidity: ", font=('Arial Bold',10)).place(x=400,y=110)
    Label(frame,text=str(humidity)+"%", font=('Arial Bold',12)).place(x=500,y=110)
    

    #label for visibility
    Label(frame,text="Visibility:", font=('Arial Bold',10)).place(x=3,y=90)
    Label(frame,text=str(visibility)+' (km)', font=('Arial Bold',12)).place(x=66,y=89)

    #label for forecast
    Label(frame,text="Forecast:", font=('Arial Bold',10)).place(x=3,y=220)
    Label(frame,text=forecast, font=('Arial',8)).place(x=66,y=220)
    
    #label for risk assessment (good to go?)
    Label(frame,text="Good to go?*: ", font=('Arial Bold',10)).place(x=3,y=280)
    Label(frame,text="*MariCast will factor in winds, waves, and visibility to determine if it is safe for mariners to depart.* ", font=('Arial Italic',10)).place(x=3,y=300)
    

        


    Button(frame, text="View Maps", command = viewChart, font=('Helvetica bold', 10),bg=("blue"),fg=("white")).place(x=270,y=350) #button for nautical charts

    alert = Button(frame, text="View Alerts", command= viewAlerts,  font=('Helvetica bold', 10),bg=("yellow"),fg=("black")).place(x=430,y=350) #button for alerts

def viewChart():
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()

    latitude = float(geo_data['latitude'])
    longitude = float(geo_data['longitude'])
    
    url = 'https://fishing-app.gpsnauticalcharts.com/i-boating-fishing-web-app/fishing-marine-charts-navigation.html#12.5/'+str(latitude)+'/'+str(longitude)
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

def viewAlerts():
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    province = str(geo_data['region'])
    if(province == 'Newfoundland and Labrador'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=nl'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Nova Scotia'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=ns'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'New Brunswick'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=nb'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Prince Edward Island'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=pei'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Quebec'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=sqc'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province =='Ontario'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=son'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Manitoba'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=mb'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Saskatchewan'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=sk'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Alberta'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=ab'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'British Columbia'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=bc'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Yukon'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=yt'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Northwest Territories'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=nt'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif(province == 'Nunavut'):
        url = 'https://weather.gc.ca/warnings/index_e.html?prov=nu'
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)
        
#button to continue to main interface
title_button_image = PhotoImage(file = "C:/Users/colby/OneDrive/Desktop/Programming Language Research Project/MariCast/title_button.png") 

title_button = Button(window,image = title_button_image, borderwidth = 0,command= mainMenu)

title_button.place(x=225,y=150)



window.mainloop() #loop window
