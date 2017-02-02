#Mathew Thomas - N15690387
#Music Software Projects, NYU Courant, Fall 2016
#Front End of the HarpsiComp app. Creates a Tkinter window which calls PyGame functions
#The HelpTip section was added rather hastily. Credit for the approach goes to Michael Foord of Voidspace 

from Tkinter import *
import tkMessageBox
import Tkinter
from MiddleMan import middleman
from GenerateScale import genscale
import ImageTk, Image
import re
 
class HelpTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createHelpTip(widget, text):
    tip = HelpTip(widget)
    def enter(event):
        tip.showtip(text)
    def leave(event):
        tip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

scale = 'EvenTempered'

def donothingE():
   global scale
   scale = 'EvenTempered'

def donothingM():
   global scale
   scale = 'MeanTone'

def donothingPt():
   global scale
   scale = 'Ptolemy'

def donothingPy():
   global scale
   scale = 'PythagDodec'

def callback():
	numlist = []
	#denomlist = []
	if E2.get() != "":
		numlist.append(float(E2.get()))
		#denomlist.append(float(E3.get()))
	if E4.get() != "":
		numlist.append(float(E4.get()))
		#denomlist.append(float(E5.get()))
	if E6.get() != "":
		numlist.append(float(E6.get()))
		#denomlist.append(float(E7.get()))
	if E8.get() != "":
		numlist.append(float(E8.get()))
		#denomlist.append(float(E9.get()))
		
	middleman(float(E1.get()),numlist,E3.get(),scale)
   	

def callback1():
	genscale(EBF.get())

def help():
	filewin = Toplevel(top)
	#filewin.geometry("1000x750")
   	text = Text(filewin)
	text.insert(INSERT, "Welcome to HarpsiComp!\n-Enter a fundamental frequency for the 5 octave scale you wish to generate.\n-Click Generate to produce the notes of the scale.\n-Once generated, you can change the scale type using the Scale Options menu (Default Scale => EvenTempered).The\nstandard notes will be mapped to the keys highlighted in green below, and the\nsharps will be mapped to the keys marked in yellow.\n-Enter the desired tempo (number of quarter notes per minute), and enter the\nnumber of notes per measure in TimeSigNum, and the subdivision of those notes inTimeSigDenom.\n-You can enter as many as 4 different Time Signatures in this manner to create\npolyrhythms as well. Polyrhythmic measures will default to a subdivision of 4.\n-Then press Start and enjoy!")
	load = Image.open("keyboardhighlight.png")
	load = load.resize((440, 150), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(filewin, image=render)
        img.image = render
        img.place(x=60, y=185)
	text.pack(side = LEFT)
	
top = Tk()
top.title("HarpsiComp")


Time4 = Frame(top)

Time3 = Frame(top)

Time2 = Frame(top)

Time1 = Frame(top)
ScaleFrame = Frame(top)
ScaleFrame.pack()
Tempo = Frame(top)
Tempo.pack()
Time1.pack()
Time2.pack()
Time3.pack()
Time4.pack()



L1 = Label(Tempo, text="Tempo")
L2 = Label(Time1, text="TimeSigNum1")
L3 = Label(Time1, text="TimeSigDenom1")
L4 = Label(Time2, text="TimeSigNum2")
L5 = Label(Time2, text="TimeSigDenom2")
L6 = Label(Time3, text="TimeSigNum3")
L7 = Label(Time3, text="TimeSigDenom3")
L8 = Label(Time4, text="TimeSigNum4")
L9 = Label(Time4, text="TimeSigDenom4")
#L1.pack( side = LEFT)
#v = StringVar()
E1 = Entry(Tempo, width = 20)
E2 = Entry(Time1, width = 20)
E3 = Entry(Time1, width = 20)
E4 = Entry(Time2, width = 20)
E5 = Entry(Time2, width = 20)
E6 = Entry(Time3, width = 20)
E7 = Entry(Time3, width = 20)
E8 = Entry(Time4, width = 20)
E9 = Entry(Time4, width = 20)
L1.pack(side = LEFT)
E1.pack(side = LEFT)
L2.pack( side = LEFT)
E2.pack(side = LEFT)
L3.pack( side = LEFT)
E3.pack(side = LEFT)
L4.pack(side = LEFT)
E4.pack(side = LEFT)
L5.pack( side = LEFT)
E5.pack(side = LEFT)
L6.pack( side = LEFT)
E6.pack(side = LEFT)
L7.pack(side = LEFT)
E7.pack(side = LEFT)
L8.pack( side = LEFT)
E8.pack(side = LEFT)
L9.pack( side = LEFT)
E9.pack(side = LEFT)


LBF = Label(ScaleFrame, text = "Base Frequency")
EBF = Entry(ScaleFrame, width = 20)
LBF.pack ()
EBF.pack ()

#tempo = str(E1.get())
#print tempo

StartMetronome = Button(Tempo, text="Start", width=10, command= callback)
StartMetronome.pack()
GenerateScales = Button(ScaleFrame, text="Generate Scales", width=10, command= callback1)

GenerateScales.pack()
createHelpTip(GenerateScales, "Generate .wav files for all four scales with the set base frequency")
createHelpTip(StartMetronome, "Start the metronome and HarpsiComp!")
createHelpTip(E2, "Enter the numerator of the time signature here")
createHelpTip(E3, "Enter the denominator of the time signature here")
createHelpTip(E1, "Enter the tempo in bpm (the number of quarter notes per minute) here")
#top.mainloop()

#
   
#top = Tk()
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Even Tempered", command=donothingE)
filemenu.add_command(label="Mean Tone", command=donothingM)
filemenu.add_command(label="Ptolemy", command=donothingPt)
filemenu.add_command(label="Pythagorean", command=donothingPy)
#filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="Scale Options", menu=filemenu)

menubar.add_command(label = "Help", command = help)
#menubar.add_cascade(label="Drum Kits", menu=editmenu)


top.config(menu=menubar)
top.mainloop()
