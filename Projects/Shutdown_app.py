from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")
    
    
def restore_time():
    os.system("shutdown /r /t 20")
  
  
def logout():
    os.system("shutdown -l")  
    
def shutdown():
    os.system("shutdown /s /t 20")    
    
shutdown = Tk()
shutdown.title("ShutDown App")
shutdown.geometry("500x500")
shutdown.config(bg="skyblue")

restart_button = Button(shutdown, text="Restart", font=("Time New Roman", 25, )
                        ,relief=RAISED, cursor="plus",command=restart)
restart_button.place(x=150, y=60, height=40, width=200)

restart_Time_button = Button(shutdown, text="Restore Time", font=("Time New Roman", 25, )
                             ,relief=RAISED, cursor="plus", command=restore_time)
restart_Time_button.place(x=150, y=170, height=40, width=200)

logout_button = Button(shutdown, text="Logout", font=("Time New Roman", 25, )
                       ,relief=RAISED, cursor="plus", command=logout)
logout_button.place(x=150, y=270, height=40, width=200)

st_button = Button(shutdown, text="Shutdown", font=("Time New Roman", 25, )
                   ,relief=RAISED, cursor="plus", command=shutdown)
st_button.place(x=150, y=370, height=40, width=200)

shutdown.mainloop()
