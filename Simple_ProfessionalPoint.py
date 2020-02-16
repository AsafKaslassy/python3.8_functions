from tkinter.simpledialog import *
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button
# import dualInputGUI


class SimpleDialog(Frame):

    def __init__(self):
        super().__init__()
        self.output1 = ""
        self.output2 = ""
        self.initUI()

    def initUI(self):

        self.master.title("Length Calc")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="x Value", width=8)
        lbl1.pack(side=LEFT, padx=5, pady=10)

        self.entry1 = Entry(frame1, textvariable=self.output1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="y Value", width=8)
        lbl2.pack(side=LEFT, padx=5, pady=10)

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btn = Button(frame3, text="Calc", command=self.onClick)
        btn.pack(padx=10, pady=10)

    def onClick(self):

        self.output1 = self.entry1.get()
        self.output2 = self.entry2.get()
        self.quit()


def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = SimpleDialog()
    root.mainloop()
    user_input = (app.output1, app.output2)

    try:
        root.destroy()
    except:
        pass
    return user_input


class Point:
    def __init__(self,xVal,yVal):
        self.xVal = xVal
        self.yVal = yVal


class FindLength(Point):
    def __init__(self,xVal,yVal):
        super().__init__(xVal,yVal)

    def length(self):
        """
        returns: the distance from the point to the (0,0) point.
        """
        ###   size of vector = √(x^2+y^2)
        distance = (self.xVal**2 + self.yVal**2)**0.5
        # distance =  math.sqrt(math.pow(self.xVal,2)+math.pow(self.yVal,2))
        return distance

# received_inputs = dualInputGUI.main()
received_inputs = main()
xVal = int(received_inputs[0])
yVal = int(received_inputs[1])

ob = FindLength(xVal,yVal)
message2 = "The distance from (0,0) to ({0},{1}) is: {2} units".format(xVal,yVal,int(ob.length()))
print("(0,0)"," _"*int(ob.length()),"(",xVal,",",yVal,")\n",message2)

window = Tk()
window.withdraw()
output2 = messagebox.showerror(title="Length Calc App",message=message2)
