from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
import speedtest

root=Tk()
root.title("Internet Speed Tester")
root.geometry("350x300")
root.resizable(False,False)
root.iconbitmap("Speedtest_41127.ico")



class internet_speed_meter:
    def __init__(self,root):
        main_frame=Frame(root)
        main_frame.pack()
        self.label1=Label(root,text="INTERNET SPEED TESTER", background="#6789c7",foreground="#5e3d47",font="Calibri 20 bold underline")
        self.label1.place(y=10,x=20)
        self.label1.config(padx=15,pady=5)
        self.Button1 = Button(root,text="Start Testing",background='Yellow',font='Times 15',command=internet_speed_meter.view_message)
        self.Button1.place(y=170,x=110)
        self.Button1.config(padx=8,pady=5)
        self.Button2 = Button(root,text="Exit",background='#ab3933',font='Times 12',command=root.destroy)
        self.Button2.place(y=235,x=150)
        self.Button2.config(padx=8,pady=5)


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
        Thread(target=internet_speed_meter.internet_speed_calc).start()

object=internet_speed_meter(root)
root.mainloop()