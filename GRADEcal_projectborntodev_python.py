from tkinter import *
import math

#โปรแกรมคำนวณเกรด
def GRADEcal(event):

    #เกรดแต่ละวิชา * หน่วยกิตของวิชานั้น
    Cal1 = int(Textboxsubject1.get())*(int(Textboxcredit1.get()))
    Cal2 = int(Textboxsubject2.get())*(int(Textboxcredit2.get()))
    Cal3 = int(Textboxsubject3.get())*(int(Textboxcredit3.get()))
    Cal4 = int(Textboxsubject4.get())*(int(Textboxcredit4.get()))
    Cal5 = int(Textboxsubject5.get())*(int(Textboxcredit5.get()))
    Cal6 = int(Textboxsubject6.get())*(int(Textboxcredit6.get()))
    Cal7 = int(Textboxsubject7.get())*(int(Textboxcredit7.get()))
    Cal8 = int(Textboxsubject8.get())*(int(Textboxcredit8.get()))

    #ผลบวกCal1 ถึง Cal8 หารผลรวมของหน่วยกิต
    Caladd = int((Cal1)+(Cal2)+(Cal3)+(Cal4)+(Cal5)+(Cal6)+(Cal7)+(Cal8))
    Caldivide = int(Textboxcredit1.get())+int(Textboxcredit2.get())+int(Textboxcredit3.get())+int(Textboxcredit4.get())+int(Textboxcredit5.get())+int(Textboxcredit6.get())+int(Textboxcredit7.get())+int(Textboxcredit8.get())
    result = int(Caladd/Caldivide)
    labelResult.configure(text=round(Caladd/Caldivide))
      

    #เงื่อนไขเกรด
    if result >= 80:
        labelResult.config(text="grade A") 
    elif result >= 75:
        labelResult.config(text="grade B+")
    elif result >= 70:
        labelResult.config(text="grade B") 
    elif result >= 65:
        labelResult.config(text="grade C+") 
    elif result >= 60:
        labelResult.config(text="grade C")
    elif result >= 55:
        labelResult.config(text="grade D+")
    elif result >= 50:
        labelResult.config(text="grade D")
    elif result <= 49:
        labelResult.config(text="grade F")
    else:
        labelResult.config(text="error !!")

MainWindow = Tk()
MainWindow.title = ("โปรแกรมคำนวณเกรด")

#กรอกคะแนนแต่ละวิชาและหน่วยกิต
labelsubject1 = Label(MainWindow, text="วิชาที่1")
labelsubject1.grid(row=0,column=0)
Textboxsubject1 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject1.grid(row=0,column=1)

Textboxcredit1 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่1
Textboxcredit1.grid(row=0,column=2)

labelsubject2 = Label(MainWindow, text="วิชาที่2")
labelsubject2.grid(row=1,column=0)
Textboxsubject2 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject2.grid(row=1,column=1)

Textboxcredit2 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่2
Textboxcredit2.grid(row=1,column=2)

labelsubject3 = Label(MainWindow, text="วิชาที่3")
labelsubject3.grid(row=2,column=0)
Textboxsubject3 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject3.grid(row=2,column=1)

Textboxcredit3 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่3
Textboxcredit3.grid(row=2,column=2)

labelsubject4 = Label(MainWindow, text="วิชาที่4")
labelsubject4.grid(row=3,column=0)
Textboxsubject4 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject4.grid(row=3,column=1)

Textboxcredit4 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่4
Textboxcredit4.grid(row=3,column=2)

labelsubject5 = Label(MainWindow, text="วิชาที่5")
labelsubject5.grid(row=4,column=0)
Textboxsubject5 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject5.grid(row=4,column=1)

Textboxcredit5 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่5
Textboxcredit5.grid(row=4,column=2)

labelsubject6 = Label(MainWindow, text="วิชาที่6")
labelsubject6.grid(row=5,column=0)
Textboxsubject6 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject6.grid(row=5,column=1)

Textboxcredit6 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่6
Textboxcredit6.grid(row=5,column=2)

labelsubject7 = Label(MainWindow, text="วิชาที่7")
labelsubject7.grid(row=6,column=0)
Textboxsubject7 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject7.grid(row=6,column=1)

Textboxcredit7 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่7
Textboxcredit7.grid(row=6,column=2)

labelsubject8 = Label(MainWindow, text="วิชาที่8")
labelsubject8.grid(row=7,column=0)
Textboxsubject8 = Entry(MainWindow)#ช่องกรอกคะแนน
Textboxsubject8.grid(row=7,column=1)

Textboxcredit8 = Entry(MainWindow)#ระบุหน่วยกิตวิชาที่8
Textboxcredit8.grid(row=7,column=2)

CalculateButton = Button(MainWindow,text = "คำนวณ")
CalculateButton.bind('<Button-1>',GRADEcal)
CalculateButton.grid(row=10,column=0)

labelResult = Label(MainWindow,text="เกรดที่ได้")
labelResult.grid(row=10,column=1)

labelResult = Label(MainWindow, text="")
labelResult.grid(row=11, column=1)

MainWindow.mainloop()