from tkinter import *
root=Tk()
root.title("Hello World")
root.geometry("1000x800")

def clicked():
    value=entry.get()
    label.config(text=value)

label=Label(root,text="Label", font=("Arial", 12 , "bold"))
label.grid(row=0,column=0)

entry=Entry(root)
entry.grid(row=4,column=0)
# entry.insert(0,"hello")
# entry.delete(3,END)  # parameters are starting index and ending index

button= Button(root, text="click here", command=clicked)
button.grid(row=1,column=0)
root.mainloop()
