from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxweight.get())/math.pow(float(textBox.get())/100,2))
    labelResult.config(text=float(textBoxweight.get())/math.pow(float(textBox.get())/100,2))
    if float(textBoxweight.get())/math.pow(float(textBox.get())/100,2) < 19:
        labelResult1.configure(text="ผอมเกินไป")
    elif float(textBoxweight.get()) / math.pow(float(textBox.get()) / 100, 2) < 23:
        labelResult1.configure(text="น้ำหนักปกติ")
    elif float(textBoxweight.get())/math.pow(float(textBox.get())/100,2) < 25:
        labelResult1.configure(text="น้ำหนักเกิน")
    elif float(textBoxweight.get())/math.pow(float(textBox.get())/100,2) < 29:
        labelResult1.configure(text="อ้วน")
    elif float(textBoxweight.get())/math.pow(float(textBox.get())/100,2) > 30:
        labelResult1.configure(text="อ้วนมาก")

mainWindow = Tk()
labelHeight = Label(mainWindow,text="Height (cm.)")
labelHeight.grid(row=0,column=0)
textBox = Entry(mainWindow)
textBox.grid(row=0,column=1)
labelweight = Label(mainWindow,text="Weight (kg.)")
labelweight.grid(row=1,column=0)
textBoxweight = Entry(mainWindow)
textBoxweight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text ="Calculate")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column = 0)
labelResult = Label(mainWindow,text="Result")
labelResult.grid(row=2,column = 1)
labelResult1 = Label(mainWindow)
labelResult1.grid(row=3,column = 1)
mainWindow.mainloop()
