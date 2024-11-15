from tkinter import *
from tkinter import ttk
import requests


# city_name = "jaipur"
# data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=da67ceb77507e6b7267dd221705f610d").xml()
# print(data)

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=da67ceb77507e6b7267dd221705f610d").json()
     
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    
    wp_label1.config(text=data["main"]["pressure"])

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
win = Tk()

win.title("Weather App")
win.config(bg="yellow") 
win.geometry("500x500")

name_label = Label(win,text="Weather App",font=("Time New Romen",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name= StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather App",values=list_name, font=("Time New Romen",20,"bold"),textvariable=city_name)
com.place(x=90,y=120,height=50,width=300)


# done_button = Button(win,text="Done",font=("Time New Romen",20,"bold"))
# done_button.place(x=200,y=190,height=50,width=100) 


w_label = Label(win,text="Weather climate",font=("Time New Romen",15,"bold"))
w_label.place(x=5,y=260,height=35,width=190)
w_label1 = Label(win,text="",font=("Time New Romen",15,"bold"))
w_label1.place(x=205,y=260,height=35,width=190)
 
wb_label = Label(win,text="Weather Descryption",font=("Time New Romen",13,"bold"))
wb_label.place(x=5,y=300,height=35,width=190)
wb_label1 = Label(win,text="",font=("Time New Romen",13,"bold"))
wb_label1.place(x=205,y=300,height=35,width=190)

wt_label = Label(win,text="Temperature",font=("Time New Romen",15,"bold"))
wt_label.place(x=5,y=340,height=35,width=190)
wt_label1 = Label(win,text="",font=("Time New Romen",15,"bold"))
wt_label1.place(x=205,y=340,height=35,width=190)

wp_label = Label(win,text="Pressure",font=("Time New Romen",15,"bold"))
wp_label.place(x=5,y=380,height=35,width=190)
wp_label1 = Label(win,text="  ",font=("Time New Romen",15,"bold"))
wp_label1.place(x=205,y=380,height=35,width=190)

done_button = Button(win,text="Done",font=("Time New Romen",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100) 


win.mainloop()