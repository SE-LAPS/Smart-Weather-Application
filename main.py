from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("WEATHER APPLICATION")
root.geometry("1100x700+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text="WEATHER NOW")

#Weather Set

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=646824f2b7b86caffec1d0b16ea77f79"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = (json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']


    t.config(text=(temp,"°C"))
    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°C"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

except EXCEPTION as e:
messagebox.showerror("WEATHER APPLICATION", "Invalid Entry!")


#Search Box Set

Search_image=PhotoImage(file="3.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=19,font=("poppins",28,"bold"),bg="#f5f5f0",border=0,fg="black")
textfield.place(x=180,y=80)
textfield.focus()

Search_icon=PhotoImage(file="5.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#f0b3ff",command=getWeather)
myimage_icon.place(x=590,y=72)


#Logo Set

Logo_image=PhotoImage(file="6.png")
logo=Label(image=Logo_image)
logo.place(x=800,y=10)


#BottoM Box Set

Frame_image=PhotoImage(file="9.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=1,pady=25,side=BOTTOM)


#Time Set

name=Label(root,font=("arial",23,"bold"),fg="#b30000")
name.place(x=160,y=170)
clock=Label(root,font=("Helvetica",18),fg="#ff6666")
clock.place(x=300,y=210)


#Label Set

label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="orange",bg="#fff2e6")
label1.place(x=180,y=430)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="orange",bg="#fff2e6")
label2.place(x=350,y=430)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="orange",bg="#fff2e6")
label3.place(x=550,y=430)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="orange",bg="#fff2e6")
label4.place(x=800,y=430)

t=Label(font=("arial",22,"bold"),fg="#eb99ff")
t.place(x=450,y=270)

c=Label(font=("arial",16,'bold'),fg="#520066")
c.place(x=450,y=310)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=190,y=500)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=370,y=500)

d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=550,y=500)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=820,y=500)


root.mainloop()
