"""
python3 output.py

@Author Andreas
	Fall 2018

Scope:
	This makes a tkinter pop up window with two buttons.
	Click the first button and the System prompts you for voice input.
		The system should then give output in another pop up window.
	Click the second button to quit.
	
References:
The simple gui from: https://docs.python.org/3/library/tkinter.html
"""

import os
import tkinter as tk
import speech_recognition as sr
#quiet the endless 'insecurerequest' warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer
mixer.init()

import listener as lr
#possibly not needed in This file anymore
import interpreter as ii					
import output as op
from translator import translator as tr

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "click here\nTo give Voice Input"
		self.hi_there["command"] = self.theListenr
		self.hi_there.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.pack(side="bottom")

	def theListenr(self):
		voiceString = (lr.listener())		
			
root = tk.Tk()
app = Application(master=root)
app.mainloop()
