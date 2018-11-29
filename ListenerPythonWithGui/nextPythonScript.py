# python3
# nextPythonScript.py
# @Author: Andreas
# @see: https://www.python-course.eu/tkinter_text_widget.php			#part of the code was taken and modified from this page

#if called from the Java file this doesn't print to the command line
#it does print of course if the python script is run from the command line by itself
print("python script...")


#Question: How about making a pop up window in python... ?
from tkinter import *
from sys import argv

root = Tk()
T = Text(root, height=40, width=100)
T.pack()

if (len(sys.argv) >= 2):
	passedInputArgument = (argv[1])
	T.insert(END, "First Line\nSecond Line\nThe passed String is: " + passedInputArgument)
else:
	T.insert(END, "First Line\nSecond Line\nThere was no passed String!")
	
mainloop()	#?

"""
Notes on usage:
This input
	python3 nextPythonScript.py
Gives output
	There was no passed String!

This input
	python3 nextPythonScript.py oneWordParameter
Gives output
	The passed String is: oneWordParameter
	
This input
	python3 nextPythonScript.py "Multiple Words Separated by Spaces"
Gives output
	The passed String is: Multiple Words Separated by Spaces			#My point is that if you pass a string with spaces in it, it needs to be surrounded by Quotes	
"""
#Answer: This might work, but the way the "passedInputArgument" is handled must be different so that the "passedInputArgument" can span over multiple lines
#The way it is now it prints everything on one single line.  (Problem 1of2)

