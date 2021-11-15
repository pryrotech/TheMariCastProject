import numpy as np
from tkinter import *


window = Tk()


window.geometry("650x500")
window.title("MariCast")
window.config(bg="white")

title = Label(window, text="MariCast")
title.config(font=('Arial Bold',40),bg=("white"),fg=("grey"))
title.pack()

sub_text = Label(window,text="An application for marine weather reports")
sub_text.config(font=('Kozuka Gothic Pro M',20),bg=("white"),fg=("blue"))
sub_text.pack()

 
def mainMenu():
    import asyncio
    from env_canada import ECWeather

    weather= ECWeather(coordinates=(47.584122, -53.281521))

    asyncio.run(weather.update())

    winds = str(weather.conditions)[594:597]
    waves = 0
    visibility = str(weather.conditions)[464:466]
    sunset = 0
    sunrise = 0
    humidex = 0
    humidity = 0
    temperature = str(weather.conditions)[50:52]
    pressure = 0
    conditions = str(weather.conditions)[1387:1393]
    forecast = "Mostly cloudy skies tonight, tapering off to clear skies around 00:00."
    
    frame = Frame(window)
    frame.pack(side="top", expand=True, fill="both")
    
    Label(frame,text="Current Marine Weather for: ", font=('Helvetica',15)).place(x=3,y=10)
    Label(frame,text="St. John's", font=('Helvetica',15),fg=("blue")).place(x=260,y=10)
    
    Label(frame,text="Winds:", font=('Arial Bold',10)).place(x=3,y=50)
    
    '''if(winds > 21):'''
    Label(frame,text=str(winds)+' knots [STRONG]', font=('Arial Bold',12),fg=("red")).place(x=50,y=48)
    '''elif(winds in range(15,21)):
        Label(frame,text=str(winds)+' knots [MODERATE]', font=('Arial Bold',12),fg=("orange")).place(x=50,y=48)
       elif(winds in range(1,14)):
        Label(frame,text=str(winds)+' knots [LIGHT]', font=('Arial Bold',12),fg=("green")).place(x=50,y=48)'''

        
    Label(frame,text="Waves:", font=('Arial Bold',10)).place(x=3,y=70)

    if(waves > 3):
        Label(frame,text=str(waves)+'m  [ROUGH]', font=('Arial Bold',12),fg=("red")).place(x=53,y=68)
    elif(waves in range(1,2)):
        Label(frame,text=str(waves)+'m  [MODERATE]', font=('Arial Bold',12),fg=("orange")).place(x=53,y=68)
    elif(waves in range(0,1)):
        Label(frame,text=str(waves)+'m  [LIGHT]', font=('Arial Bold',12),fg=("green")).place(x=53,y=68)
        

    Label(frame,text="Conditions: ", font=('Arial Bold',10)).place(x=400,y=50)
    Label(frame,text=conditions, font=('Arial Bold',12)).place(x=480,y=47)

    Label(frame,text="Atmospheric Pressure: ", font=('Arial Bold',10)).place(x=400,y=70)
    Label(frame,text=str(pressure)+" kPa", font=('Arial Bold',12)).place(x=550,y=68)

    Label(frame,text="Temperature: ", font=('Arial Bold',10)).place(x=400,y=90)
    Label(frame,text=str(temperature)+"°C", font=('Arial Bold',12)).place(x=500,y=90)

    Label(frame,text="Humidity: ", font=('Arial Bold',10)).place(x=400,y=110)
    Label(frame,text=str(humidity)+"%", font=('Arial Bold',12)).place(x=500,y=110)

    Label(frame,text="Humidex/Windchill: ", font=('Arial Bold',10)).place(x=400,y=130)
    Label(frame,text=humidex, font=('Arial Bold',12)).place(x=535,y=128)

    Label(frame,text="Sunset/Sunrise:  ", font=('Arial Bold',10)).place(x=400,y=150)
    Label(frame,text=str(sunset)+"/"+str(sunrise), font=('Arial Bold',12)).place(x=510,y=149)

    
    Label(frame,text="Visibility:", font=('Arial Bold',10)).place(x=3,y=90)
    Label(frame,text=str(visibility)+' (km)', font=('Arial Bold',12)).place(x=66,y=89)
    
    Label(frame,text="Forecast:", font=('Arial Bold',10)).place(x=3,y=220)
    Label(frame,text=forecast, font=('Arial',8)).place(x=66,y=220)
    
    Label(frame,text="Good to go?*: ", font=('Arial Bold',10)).place(x=3,y=280)
    Label(frame,text="*MariCast will factor in winds, waves, and visibility to determine if it is safe for mariners to depart.* ", font=('Arial Italic',10)).place(x=3,y=300)
    
    '''if(winds > 21 or waves > 3 or visibility < 10):
        Label(frame,text="DANGEROUS (Do not go) ", font=('Arial Bold',10),bg=("red"),fg=("white")).place(x=100,y=280)
    elif(winds > 15 or waves in range(1,2) or visibility < 20):
        Label(frame,text="CAUTION (Take caution, or avoid departing) ", font=('Arial Bold',10),bg=("orange"),fg=("white")).place(x=100,y=280)
    elif(winds < 15 or waves in range(0,1) or visibility in range(20,100)):
        Label(frame,text="GOOD (Good to go) ", font=('Arial Bold',10),bg=("green"),fg=("white")).place(x=100,y=280)
    else:
        Label(frame,text="GOOD (Good to go) ", font=('Arial Bold',10),bg=("green"),fg=("white")).place(x=100,y=280)'''
        
    Button(frame, text="Calculate ETA", font=('Helvetica bold', 10),bg=("blue"),fg=("white")).place(x=100,y=350)

    Button(frame, text="View Maps", font=('Helvetica bold', 10),bg=("blue"),fg=("white")).place(x=270,y=350)

    Button(frame, text="View Alerts", font=('Helvetica bold', 10),bg=("yellow"),fg=("black")).place(x=430,y=350)


title_button_image = PhotoImage(file = "C:/Users/colby/OneDrive/Desktop/Programming Language Research Project/MariCast/title_button.png")

title_button = Button(window,image = title_button_image, borderwidth = 0,command= mainMenu)

title_button.place(x=225,y=150)



window.mainloop()
