from tkinter import *
from tkinter import messagebox
from time import strftime
import tkinter as Tkinter 
from datetime import datetime


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x600+500+200')
ws.title('ToDo List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)# 할일쓰는곳 위치

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'do homework',
    'drink water',
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


#CLOCK


def time():
    string = strftime('%H:%M:%S %p') 
    lbl.config(text=string)
    lbl.after(1000, time)
 
lbl = Label(ws, font=('calibri', 40, 'bold'),
            background='white',
            foreground='black')
 
lbl.pack(side=TOP)


#스톱워치
counter = 54000
running = False
def counter_label(label): 
    def count(): 
        if running: 
            global counter 

            if counter==54000:             
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string 
   
            label['text']=display   
            label.after(1000, count)  
            counter += 1
   
    count()      
   

def Start(label): 
    global running 
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label): 
    global counter 
    counter=54000
   

    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
   

    else:                
        label['text']='Starting...'
   

   

ws.minsize(width=250, height=70) 
label = Tkinter.Label(ws, text="START!", fg="black", font="Verdana 30 bold") 
label.pack() 
f = Tkinter.Frame(ws)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label)) 
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop) 
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label)) 
f.pack(anchor = 'center',pady=5)
start.pack(side="left") 
stop.pack(side ="left") 
reset.pack(side="left")

time()
ws.mainloop()
mainloop()