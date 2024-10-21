# from tkinter import *
# root=Tk()
# root.title("hello")

# name=Label(root,text="Name")
# name.pack()

# entry=Entry(root)
# entry.pack()

# exit=Button(root,text="Exit",fg="blue", command=exit)
# exit.pack(side=LEFT)

# def clear():
#     entry.delete(0,END)

# clear_button=Button(root,text="Clear",command=clear)
# clear_button.pack(side=RIGHT)

# def submit():
#     name = entry.get()
#     print(name)
# submit_button=Button(root,text="Submit",command=submit).pack()
# root.mainloop()

#chess board
# from tkinter import *
# root=Tk()
# root.title("chess board ")
# color1="black"
# color2="white"
# for j in range( 0,8):
#     color1,color2=color2,color1
#     for i in range(0,8):
#         board=Label(root, bg=color2,width=3)
#         board.grid(row=j, column=i)
#         color1,color2=color2,color1
# root.mainloop()


# fahrenheit to celsius

# from tkinter import *
# root=Tk()
# root.title("temperature converter")

# def fahtocel():
#     fahrenheit = float(entryfah.get())
#     celsius = (fahrenheit - 32) * 5.0/9.
#     entrycel.insert(0,celsius)

# def cls():
#     entryfah.delete(0,END)
#     entrycel.delete(0,END)

# fah=Label(root,text="Fahrenheit")
# fah.grid(row=0,column=0)

# cel=Label(root,text="Celsius")
# cel.grid(row=1,column=0)

# entryfah=Entry(root)
# entryfah.grid(row=0,column=1)

# entrycel=Entry(root)
# entrycel.grid(row=1,column=1)

# calc=Button(root,text="Calculate",width=10, command=fahtocel).grid(row=2,column=0,columnspan=1)
# clear=Button(root,text="Clear",width=10, command=cls).grid(row=2,column=1,columnspan=3)
# root.mainloop()

# jumbled words

# from tkinter import *
# from tkinter import messagebox
# import random
# root=Tk()
# root.title("jumbled words")
# l=["python","jumble","elephant","rhinoceros"]
# jumble=" "
# message="Click to start"
# def start_game():
#     global jumble
#     global w
#     w=random.choice(l)
#     listy=list(w)
#     random.shuffle(listy)
#     jumble="".join(listy)
#     print(jumble)
#     global message
#     message="Guess the jumbled word"
#     start.config(text=message)
#     word.config(text=jumble)      # to update a label or button with new text

# def check():
#     ans=answer.get()
#     if ans==w:
#         m1=messagebox.showinfo("congrats","You got 1 point")
#         start_game()
#     else:
#         m2=messagebox.showwarning("try again","You got 0 points")

# start=Button(root, text=message, bg="orange", width=30, command=start_game)
# start.grid(row=0, column=0, columnspan=2)

# word=Label(root,text= jumble)
# word.grid(row=1,column=0)
# answer=Entry(root)
# answer.grid(row=1,column=1)
# submit=Button(root,text="Submit",comman=check).grid(row=2,column=1)
# root.mainloop()

#Stopwatch

# from tkinter import *
# import time
# root=Tk()
# root.title("Stopwatch")
# hms=StringVar()
# timelabel=Label(root,textvariable=hms, width=30)
# timelabel.grid(row=0,column=0, columnspan=3)
# show=True
# h,m,s=0,0,0
# def start_time():
#     global h,m,s 
#     while show==True:
#         s+=1
#         hms.set("{h}:{m}:{s}".format(h=h,m=m,s=s))
#         time.sleep(1)
#         root.update()
#         if s==60:
#             m+=1
#             s=0
#         if m==60:
#             h+=1
#             m=0
# def stop_time():
#     global h,m,s
#     global show
#     show=False

# def reset_time():
#     global h,m,s,show
#     h,m,s=0,0,0
#     hms.set("{h}:{m}:{s}".format(h=h,m=m,s=s))
#     show=True
#     root.update()

# start=Button(root, text="START", command=start_time)
# start.grid(row=1,column=0)

# stop=Button(root,text="STOP",command=stop_time)
# stop.grid(row=1,column=1)

# reset=Button(root,text="RESET",command=reset_time)
# reset.grid(row=1,column=2)

# root.mainloop()

# from tkinter import *
# import webcolors
# root=Tk()
# root.title("Color picker")

# value=webcolors.rgb_to_hex((255,255,255))
# red_var=IntVar()
# green_var=IntVar()
# blue_var=IntVar()
# red_scale=Scale(root,label="red",variable=red_var,from_=255, to=0, orient=VERTICAL)
# red_scale.grid(row=0,column=0)

# green_scale=Scale(root,label="green",variable=green_var,from_=255, to=0, orient=VERTICAL)
# green_scale.grid(row=0,column=1)

# blue_scale=Scale(root,label="blue",variable=blue_var,from_=255, to=0, orient=VERTICAL)
# blue_scale.grid(row=0,column=2)

# colorlabel=Label(root,bg=value, width=60)
# colorlabel.grid(row=1,column=0,columnspan=3)

# while True:
#     red=red_var.get()
#     green=green_var.get()
#     blue=blue_var.get()
#     value=webcolors.rgb_to_hex((red,green,blue))
#     colorlabel.config(bg=value)
#     root.update()
# root.mainloop()

#Timezone

# from tkinter import *
# import pytz
# import pygame
# from datetime import datetime

# indiaflag=pygame.image.load("D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\indiaflag.png")
# indiaflag=pygame.transform.scale(indiaflag,(100,80))
# pygame.image.save(indiaflag,"D:\Study Stuff\Wonksknow\level 3 oops\Tkinter\indiaflag.png")
# root=Tk()
# frame1=Frame(root, width=150, height =100)
# frame1.grid(row=0,column=0)
# indiatime=StringVar()
# Indialabel=Label(frame1,text="India")
# Indialabel.grid(row=0,column=0)
# flag1=PhotoImage(file="D:\\Study Stuff\\Wonksknow\\level 3 oops\\Tkinter\\indiaflag.png")
# Indiaflag=Label(frame1,image=flag1)
# Indiaflag.grid(row=1,column=0)
# time1=Label(frame1,textvariable=indiatime)
# time1.grid(row=2,column=0)
# while True:
#     now = datetime.now(pytz.timezone('Asia/Kolkata'))
#     final_time=now.strftime("%y-%m-%d %H:%M:%S %p %Z")
#     indiatime.set(final_time)
#     root.update()
# root.mainloop()


# from tkinter import *
# import random
# root=Tk()
# password=StringVar()
# root.title("Password generator")

# def generate():
    
#     r=radio_variable.get()
#     str=""
#     p=password_length.get()
#     if r==0:
#         for _ in range(int(p)):
#             str= str+chr(random.randint(97,122))
#         password.set(str)
# frame1=Frame(root)
# frame1.grid(row=0,column=0)
# label1=Label(frame1, text="GENERATED PASSWORD")
# label1.grid(row=0, column=0)
# label2=Label(frame1, textvariable=password)
# label2.grid(row=0, column=1)
# frame2=Frame(root)
# frame2.grid(row=1,column=0)
# label3=Label(frame2, text="Password Strength")
# label3.grid(row=1,column=0)
# radio_variable=IntVar()
# radio1=Radiobutton(frame2,text="Low", variable=radio_variable,value=0)
# radio1.grid(row=1,column=1)
# radio2=Radiobutton(frame2,text="Medium", variable=radio_variable, value=1)
# radio2.grid(row=1,column=2)
# radio3=Radiobutton(frame2,text="High", variable=radio_variable, value=2)
# radio3.grid(row=1,column=3)
# frame3=Frame(root)
# frame3.grid(row=2,column=0)
# label4=Label(frame3, text="Password Length:")
# label4.grid(row=2,column=0)
# password_length=Spinbox(frame3, from_=6 , to=12)
# password_length.grid(row=2,column=1)
# frame4=Frame(root)
# frame4.grid(row=3,column=0)
# button1=Button(frame4, text="SUBMIT", command=generate)
# button1.grid(row=3,column=0)

# root.mainloop()

# QUIZ using OOPS

# from tkinter import *
# import random,time
# root=Tk()
# class Question:
#     def __init__(self, question,answer,options):
        
#         self.frame2=Frame(root)
#         self.radio_variable=IntVar()
#         self.question_var=StringVar()
#         self.question_var.set(question)
       
#         self.questionLabel=Label(self.frame2,textvariable=self.question_var)
#         self.answer=answer
#         self.options=options
      
#         self.option1=Radiobutton(self.frame2,text=self.options[0], variable=self.radio_variable, value=0)
#         self.option2=Radiobutton(self.frame2,text=self.options[1], variable=self.radio_variable, value=1)
        
#     def display(self):
#         self.frame2.pack()
#         self.questionLabel.pack()
#         self.option1.pack()
#         self.option2.pack()

#     def highlight_correct(self):
#         selected = self.radio_variable.get()
#         if self.options[selected] == self.answer:
#             if selected == 0:
#                 self.option1.config(fg="green")
#             else:
#                 self.option2.config(fg="green")
#         else:
#             if selected == 0:
#                 self.option1.config(fg="red")
#             else:
#                 self.option2.config(fg="red")
#         if self.answer == self.options[0]:
#             self.option1.config(fg="green")
#         else:
#             self.option2.config(fg="green")
        
#     def check(self):
        
#         selected=self.radio_variable.get()
#         if self.options[selected]==self.answer:
#             print("correct")
#             self.highlight_correct()
#             return True
#         else:
#             print("incorrect", self.options[selected], self.answer)
#             self.highlight_correct()
#             return False
        
#     def hide(self):
#         self.frame2.pack_forget()
       

# q1=Question("What is the capital of India?","Delhi",["Mumbai","Delhi"])   
# q2=Question("What is the capital of USA?","WashingtonDC",["WashingtonDC","California"]) 
# q3=Question("What is the capital of China?","Beijing",["Beijing","Shanghai"])    


# Q=[q1,q2,q3]
# qcount=0
# frame1=Frame(root)
# frame1.pack()
# scorecount=IntVar(value=0)
# Scoretext=Label(frame1,text="Score")
# Score=Label(frame1,textvariable=scorecount)
# Scoretext.pack()
# Score.pack()
# frame3=Frame(root)

       
# def hide_and_display_next():
#     global qcount
#     if qcount<len(Q)-1:
#         Q[qcount].hide()
#         qcount+=1
#         Q[qcount].display()

#         # Update the submit button command for the new question
#         submit.config(command=submit_answer)
#     else:
#         print("Quiz done")

# def submit_answer():
#     if Q[qcount].check():  # If the answer is correct
#         scorecount.set(scorecount.get() + 1)  # Increment the score
#         Score.config(textvariable=scorecount)
    
# Q[qcount].display()


# frame3.pack(side=BOTTOM, pady=20)
# submit=Button(frame3,text="Submit", command=submit_answer)
# submit.pack()
# next=Button(frame3,text="Next",command=hide_and_display_next)
# next.pack()
# root.title("Quiz")
# root.geometry("400x300")
# root.mainloop()


# Text Widget

# import wikipedia
# from tkinter import *
# root=Tk()

# root.title("Wikipedia info")


# search=Label(root,text="Search")
# search.grid(row=0,column=0)

# entry=Entry(root)
# entry.insert(0,"Enter topic to search")
# entry.grid(row=0,column=1)

# def searchinfo():
#     search_term = entry.get()
#     info=wikipedia.summary(search_term, sentences=2)
#     text_box.delete(1.0, END)
#     text_box.insert(INSERT, info)

# submit=Button(root, text="Submit", command=searchinfo)
# submit.grid(row=0,column=2)

# text_box=Text(root)
# text_box.grid(row=1,column=0,columnspan=3)


# root.mainloop()


# Listbox and Scrollbar

# import time
# from tkinter import *
# root=Tk()

# basic_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Yellow",
#     "Orange",
#     "Purple",
#     "Pink",
#     "Black",
#     "White",
#     "Gray",
#     "Brown",
#     "Turquoise",
#     "Silver",
#     "Lime",
#     "Cyan",
#     "Magenta",
#     "Coral",
#     "Navy",
#     "Olive",
#     "Teal"
# ]

# COLORS=Label(root,text="Colors")
# COLORS.pack()
# scrollbar1=Scrollbar(root,orient=VERTICAL)
# colorlist=Listbox(root,yscrollcommand=scrollbar1.set)
# for color in basic_colors:
#     colorlist.insert(END,color)

# scrollbar1.config(command=colorlist.yview)
# colorlabel=Label(root, width=20, height=2)
# scrollbar1.pack(side=RIGHT,fill=Y, expand=True)
# colorlist.pack()
# colorlabel.pack()



# def update():
#     selection=colorlist.curselection()
#     if len(selection)>0:
#         index=selection[0]
#         actual_value=colorlist.get(index)
#         colorlabel.config(bg=actual_value)
#     root.after(100,update)   #Schedule this function to run again after 100 milliseconds

# update()

# root.mainloop()
     

# Notebook

# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# root=Tk()
# notebook=ttk.Notebook(root)

# users = {
#     "john_doe": "password123",
#     "jane_smith": "ilovepython",
#     "admin_user": "admin123",
#     "test_user": "test123"
# }

# def add():
#     global users
#     username = userentry2.get()
#     password = passentry2.get()
#     if username not in users:
#         users[username] = password
#         messagebox.showinfo("Success", "User added successfully")
#     else:
#         messagebox.showerror("Error", "Username already exists")

# def login():
#     global users
#     username = userentry.get()
#     password = passentry.get()
#     if username in users and users[username] == password:
#         messagebox.showinfo("Success", "Login successful")
#     else:
#         messagebox.showerror("Error", "Invalid username or password")

# frame1=Frame(notebook)
# frame2=Frame(notebook)
# userlabel=Label(frame1,text="Username")
# userentry=Entry(frame1)
# passlabel=Label(frame1,text="Password")
# passentry=Entry(frame1,show="*")

# submit=Button(frame1,text="Submit", command=login)


# userlabel.pack()
# userentry.pack()
# passlabel.pack()
# passentry.pack()
# submit.pack()

# userlabel2=Label(frame2,text="Username")
# userentry2=Entry(frame2)
# passlabel2=Label(frame2,text="Password")
# passentry2=Entry(frame2,show="*")

# Register=Button(frame2,text="Register",command=add)


# userlabel2.pack()
# userentry2.pack()
# passlabel2.pack()
# passentry2.pack()
# Register.pack()


# notebook.add(frame1,text="login")
# notebook.add(frame2,text="register")
# notebook.pack()



# root.mainloop()

# Menu Widget

# from tkinter import *
# root=Tk()

# menubar=Menu(root)
# filemenu=Menu(menubar,tearoff=0)
# filemenu.add_command(label="New",command=lambda:print("New"))
# filemenu.add_command(label="Open...",command=lambda:print("Open..."))
# menubar.add_cascade(label="File",menu=filemenu)
# menubar.add_cascade(label="Help",menu=filemenu)
# #filemenu.add_separator()

# root.config(menu=menubar)     # to associate the root window to the menu
# root.mainloop()


from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
root=Tk()
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
def new():
    global file_name
    file_name=None
    textw.delete(1.0,END)
def save():
    global file_name
    file_name=fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    f=open(file_name,"w")
    f.write(textw.get(1.0,END))

def openfile():
    global file_name
    file_name=fd.askopenfilename()
    g=open(file_name,"r")
    textw.delete(1.0,END)
    textw.insert(1.0,g.read())
def about():
    messagebox.showinfo("About","This is a custom notepad")
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open...",command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=lambda:root.destroy())
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="file", menu=filemenu)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)

textw=Text(root)
textw.grid(row=1,column=0,columnspan=3)
root.mainloop()