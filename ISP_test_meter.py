from tkinter import *
from tkinter import messagebox
from threading import Thread
import speedtest

def internet_speed_calc():
    st=speedtest.Speedtest()
    st.get_best_server()
    download=st.download()/1024/1024
    upload=st.upload()/1024/1024
    ping_status=st.results.ping
    details=(f'Download Speed: {download:.2f} Mb/s \nUpload Speed: {upload:.2f} Mb/s \n Ping Status: {ping_status} ms')
    messagebox.showinfo("SPEED TEST", details)


def view_message():
    label=Label(root,text="Wait for couple of Seconds",font="Times 15 bold")
    label.place(y=70,x=40)
    Thread(target=internet_speed_calc).start()


root=Tk()
root.title("Speed Test Meter")
root.geometry("300x300")
label1=Label(root,text="SPEED TEST", background="#6789c7",foreground="#5e3d47",font="Calibri 20 bold underline")
label1.place(y=10,x=70)
label1.config(padx=20,pady=5)
Button1 = Button(root,text="Start Testing",background='Yellow',font='Times 15',command=view_message)
Button1.place(y=170,x=90)
Button1.config(padx=8,pady=5)
Button2 = Button(root,text="Exit",background='#ab3933',font='Times 12',command=root.destroy)
Button2.place(y=235,x=130)
Button2.config(padx=8,pady=5)
root.mainloop()