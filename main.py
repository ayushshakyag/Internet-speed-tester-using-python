from tkinter import *
from tkinter import font
from turtle import color
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    dn = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_dn.config(text=dn)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet speed test")
sp.geometry("530x530")
sp.config(bg="Black")

lab = Label(sp,text="Internet speed test",font=("Time New Roman",32,"italic"),bg="Black",fg="White").place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Time New Roman",30,"bold"),fg="White",bg="Green").place(x=60,y=130,height=50,width=380)
lab_dn = Label(sp,text="00",font=("Time New Roman",30,"bold"),fg="White",bg="Red")
lab_dn.place(x=60,y=200,height=50,width=380)
lab = Label(sp,text="Upload Speed",font=("Time New Roman",30,"bold"),fg="White",bg="Green").place(x=60,y=290,height=50,width=380)
lab_up = Label(sp,text="00",fg="White",font=("Time New Roman",30,"bold"),bg="Red")
lab_up.place(x=60,y=360,height=50,width=380)
button = Button(sp,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)
sp.mainloop()