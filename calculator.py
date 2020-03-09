from tkinter import *
from math import *
class cal:
    def press(self,n):
        self.text.insert(INSERT,n)

    def dl(self):
        self.text.delete(1.0,2.0)

    def equal(self):
        self.exp=self.text.get(1.0,END)
        try:
            self.result=eval(self.exp)
            self.text.delete(1.0,2.0)
            self.text.insert(INSERT,self.result)
        except:
            self.text.delete(1.0,2.0)
            self.text.insert(INSERT,"Invalid syntax")

    def __init__(self,root):
        root.geometry("350x350")
        root.title("GJ calculator")
        self.frame1=Frame(root)
        self.frame1.pack(side=TOP)
        self.text=Text(self.frame1,width=50,height=4)
        self.text.pack()
        self.frame2=Frame(root)
        self.frame2.pack()
        self.button1=Button(self.frame2,width=4,height=4,text="1",command=lambda:self.press(1))
        self.button1.grid(row=0)
        self.button2 = Button(self.frame2, width=4, height=4, text="2",command=lambda:self.press(2))
        self.button2.grid(row=0,column=1)
        self.button3=Button(self.frame2,width=4,height=4,text="3",command=lambda:self.press(3))
        self.button3.grid(row=0,column=2)
        self.button4= Button(self.frame2, width=4, height=4, text="4",command=lambda:self.press(4))
        self.button4.grid(row=1,column=0)
        self.button5 = Button(self.frame2, width=4, height=4, text="5",command=lambda:self.press(5))
        self.button5.grid(row=1, column=1)
        self.button6 = Button(self.frame2, width=4, height=4, text="6",command=lambda:self.press(6))
        self.button6.grid(row=1, column=2)
        self.button7 = Button(self.frame2, width=4, height=4, text="7",command=lambda:self.press(7))
        self.button7.grid(row=2, column=0)
        self.button8 = Button(self.frame2, width=4, height=4, text="8",command=lambda:self.press(8))
        self.button8.grid(row=2, column=1)
        self.button9 = Button(self.frame2, width=4, height=4, text="9",command=lambda:self.press(9))
        self.button9.grid(row=2, column=2)
        self.button0 = Button(self.frame2, width=4, height=4, text="0",command=lambda:self.press(0))
        self.button0.grid(row=3, column=0)
        self.button10 = Button(self.frame2, width=4, height=4, text="=",command=self.equal)
        self.button10.grid(row=3, column=1)
        self.button11 = Button(self.frame2, width=4, height=4, text="Clear",command=self.dl)
        self.button11.grid(row=3, column=2)
        self.button12 = Button(self.frame2, width=4, height=4, text="+",command=lambda:self.press("+"))
        self.button12.grid(row=0, column=3)
        self.button13 = Button(self.frame2, width=4, height=4, text="-",command=lambda:self.press("-"))
        self.button13.grid(row=1, column=3)
        self.button14 = Button(self.frame2, width=4, height=4, text="x",command=lambda:self.press("*"))
        self.button14.grid(row=2, column=3)
        self.button15 = Button(self.frame2, width=4, height=4, text="/",command=lambda:self.press("/"))
        self.button15.grid(row=3, column=3)


root=Tk()
start=cal(root)
root.mainloop()
