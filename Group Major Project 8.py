from tkinter import*
win=Tk()
win.geometry("350x250")
win.title("Pokemon Battle RPS Style")


btnMenu = Button(win,text="File").grid(row=0,column=0)
btnMenu = Button(win,text="Rules").grid(row=0,column=1)
btnMenu = Button(win,text="Restart").grid(row=0,column=2)
lblChoice = Label(win,text="Choice").grid(row=2,column=0,pady=8)


v = StringVar(win,"1")

values ={"Chartzard 1" : "1",
         "Blastoise 2" : "2",
         "Venusaur  3" : "3" }
for (text,value) in values.items():
    Radiobutton(win,text = text,variable = v,
                value = value).grid(padx=2,pady=15,column=0)


lblScore=Label(win,text="Score").grid(row=80,column=0)
lblHealth=Label(win,text="Health:").grid(row=100,column=0)






win.mainloop()
