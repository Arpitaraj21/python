from tkinter import *
import speedtest 

def speedchecker():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download_speed = str(round(sp.download() / (10**6),3)) + "Mbps"
    uploading_speed = str(round(sp.upload() / (10**6),3)) + "Mbps"
    lab_down.config(text=download_speed)
    lab_up.config(text=uploading_speed)

sp = Tk()
sp.title(" Internet Speed Test")
sp.geometry("400x700")
sp.config(bg="lightgreen")

lab = Label(sp, text = " Internet Speed Test", font=("Time New Roman", 20, "bold") )
lab.place(x=40, y=40, height=50, width=300)


lab_down = Label(sp, text = " Download Speed ", font=("Time New Roman", 20, "bold") )
lab_down.place(x=40, y=130, height=50, width=300)


lab = Label(sp, text = " 00", font=("Time New Roman", 20, "bold") )
lab.place(x=40, y=200, height=50, width=300)


lab = Label(sp, text = " Upload Speed", font=("Time New Roman", 20, "bold") )
lab.place(x=40, y=290, height=50, width=300)

lab_up = Label(sp, text = " 00", font=("Time New Roman", 20, "bold") )
lab_up.place(x=40, y=360, height=50, width=300)


button = Button(sp, text="CHECK SPEED", font=("Time New Roman", 30, "bold"), relief=RAISED, command=speedchecker)
button.place(x= 40, y=460, height=50,width=300)



sp.mainloop()
