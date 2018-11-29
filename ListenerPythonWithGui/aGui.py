#The simple gui from: https://docs.python.org/3/library/tkinter.html

import os
import tkinter as tk
import speech_recognition as sr
#quiet the endless 'insecurerequest' warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer
mixer.init()

import interpreter as ii
import output as op

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
		while (True == True):
			# obtain audio from the microphone
				r = sr.Recognizer()
				with sr.Microphone() as source:
					#print("Please wait. Calibrating microphone...")
					# listen for 1 second and create the ambient noise energy level
					r.adjust_for_ambient_noise(source, duration=1)
					print("Say something!")
					audio = r.listen(source,phrase_time_limit=None)		#set to 55 instead?
				 
			# recognize speech using Sphinx/Google
				try:
					#response = r.recognize_sphinx(audio)
					response = r.recognize_google(audio)
					#print(type (response))								#for debugging. response is, of course, a string.
					print("I think you said '" + response + "'")

					if (len(response) > 10):
						#execfile('file.py', input )
						#os.system("interpreter.py " + response)
						op.output(ii.interpret(response))				#this line became interesting
						return response	

				except sr.UnknownValueError:
					print("Sphinx could not understand audio")
				except sr.RequestError as e:
					print("Sphinx error; {0}".format(e))
			
root = tk.Tk()
app = Application(master=root)
app.mainloop()
