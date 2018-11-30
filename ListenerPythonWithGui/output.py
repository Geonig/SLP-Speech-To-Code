"""
python3 output.py

@Author Andreas
	Fall 2018

Scope:
	This makes a tkinter pop up window that displays the output of our whole system
	
References:
https://www.python-course.eu/tkinter_text_widget.php			#part of the code was taken and modified from this page
https://gordonlesti.com/use-tkinter-without-mainloop/
"""

# A pop up window in python.  To display the results.
from tkinter import *
from sys import argv

##-Main----------------------------------------------------
def output(passedInputArgument):
	root = Tk()
	T = Text(root, height=40, width=75)
	T.pack()
	T.insert(END, passedInputArgument)
	mainloop()
	
#output("while death is not true live")			#for debugging
