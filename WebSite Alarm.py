import time
import webbrowser
import tkinter
from tkinter import *
from tkinter import messagebox
input_time=""
website_url=""

window=tkinter.Tk()
window.title("User Input")
window.geometry("400x200")

def websiteAlarm():
    t=time.localtime()
    current_time=time.strftime("%H:%M:%S",t)
    try:
        temp=(int(input_time[:2])-int(current_time[:2]))*3600+(int(input_time[3:5])-int(current_time[3:5]))*60+(int(input_time[6:8])-int(current_time[6:8]))
    except:
        print("Please input the right value:")
    while(temp>-1):
        mins,secs=temp//60,temp%60
        hrs=0
        if mins>60:
            hrs,mins=mins//60,mins%60
        hours.set("{0:2d}".format(hrs))
        minutes.set("{0:2d}".format(mins))
        seconds.set("{0:2d}".format(secs))
        window.update()
        time.sleep(1)
        if(temp==0):
            messagebox.showinfo("ALARM","It's time to open"+website_url)
            window.destroy()
            webbrowser.open(website_url)
        temp-=1

def fun1():
    global input_time
    global website_url
    input_time=input1.get()
    website_url=input2.get()
    websiteAlarm()

label=tkinter.Label(window,text="OpenTime(HH:MM:SS)(24hrformat):")
input1=tkinter.Entry(window)
label2=tkinter.Label(window,text="Website_URL:")
input2=tkinter.Entry(window)
t=time.localtime()
current_time=time.strftime("%H:%M:%S",t)
label3=tkinter.Label(window,text="Current_Time"+current_time)
label3.pack()
label.pack()
input1.pack()
label2.pack()
input2.pack()
input_time=input1.get()
website_url=input2.get()
button=tkinter.Button(window,text="OK",command=fun1)
button.pack()

lab3=tkinter.Label(window,text="Time Remaining:")
lab3.pack()
hours=StringVar()
minutes=StringVar()
seconds=StringVar()
hours.set("00")
minutes.set("00")
seconds.set("00")
hourEntry=tkinter.Entry(window,width=3,font=("Arial",18,""),textvariable=hours)
minuteEntry=tkinter.Entry(window,width=3,font=("Arial",18,""),textvariable=minutes)
secondEntry=tkinter.Entry(window,width=3,font=("Arial",18,""),textvariable=seconds)
hourEntry.place(x=140,y=150)
minuteEntry.place(x=190,y=150)
secondEntry.place(x=240,y=150)
window.mainloop()

def websiteAlarm():
    t=time.localtime()
    current_time=time.strftime("%H:%M:%S",t)
    print(current_time)
    print(input_time)
    try:
        temp=(int(input_time[:2])-int(current_time[:2]))*3600+(int(input_time[3:5])-int(current_time[3:5]))*60+(int(input_time[6:8])-int(current_time[6:8]))
    except:
        print("Please input the right value:")
    while(temp>-1):
        mins,secs=temp//60,temp%60
        hours=0
        if mins>60:
            hrs,mins=mins//60,mins%60
        hours.set("{0:2d}".format(hrs))
        minutes.set("{0:2d}".format(mins))
        seconds.set("{0:2d}".format(secs))
        window.update()
        time.sleep(1)
        if(temp==0):
            tkinter.messagebox.showinfo("ALARM","It's time to open"+website_url)
            window.destroy()
        temp-=1
