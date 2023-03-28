from tkinter import *
import math

def Bmitk(event):
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    Bmitk = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))

    if Bmitk >= 30.0 :
        labelResult.config(text="อ้วนมาก") 
    elif Bmitk >=25.0 :
        labelResult.config(text="อ้วน")
    elif Bmitk >=23.0 :
        labelResult.config(text="น้ำหนักเกิน") 
    elif Bmitk >=18.6 :
        labelResult.config(text="น้ำหนักปกติ(เหมาะสม)") 
    elif Bmitk <=18.5 :
        labelResult.config(text="ผอมเกินไป") 

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง:cm")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=2)

labelWeigth = Label(MainWindow, text="น้ำหนัก:kg")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=2)

calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.bind('<Button-1>', Bmitk)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="  :  ดัชนีมวลกาย(BMI)")
labelResult.grid(row=2,column=1)

labelResult = Label(MainWindow,text="")
labelResult.grid(row=3,column=1)

MainWindow.mainloop()
