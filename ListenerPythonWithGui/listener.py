"""
python3 listener.py

@Author Andreas
	Fall 2018

Scope:
	The Method "listener" takes voice input then prints and returns the a string. 

References:
mostly taken from:
https://pythonspot.com/speech-recognition-using-google-speech-api/
but also:
http://portaudio.com/download.html
https://pypi.org/project/PyAudio/#files
https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error
https://stackoverflow.com/questions/28140972/importerror-no-module-named-pyaudio
https://stackoverflow.com/questions/44538746/cannot-install-pyaudio-0-2-11-in-ubuntu-16-04
https://github.com/Uberi/speech_recognition/issues/20
https://github.com/pndurette/gTTS/issues/98
https://github.com/pndurette/gTTS/issues/50
https://github.com/Uberi/speech_recognition/issues/298
https://www.linuxquestions.org/questions/programming-9/speech-recognition-microphone-needs-pyaudio-0-2-11-or-later-but-i-have-0-2-8-a-4175629060/
"""

import speech_recognition as sr
#from gtts import gTTS
#quiet the endless 'insecurerequest' warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
from pygame import mixer
mixer.init()

import interpreter as ii
import output as op
from translator import translator as tr

def listener(): 
	while True:
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
				print("The Listener returns: '" + response + "'")

				if (len(response) > 10):
					#execfile('file.py', input )				#not running the file this way since it's all python now
					#os.system("interpreter.py " + response)	#same here
					interpretation = (ii.interpret(response))					
					translation = tr(interpretation)  
					trResult = translation.translate2java()
					#print("The Translator returns")				#for debug consider throwing out
					#print(trResult)								#for debug consider throwing out	
					#print(type (trResult))							#for debugging. trResult is a list.
					str1 = ''.join(trResult)
					print("The Translator returns: '" + str1 + "'")
					op.output(str1)				#this line makes the output window pop up
					return response	

			except sr.UnknownValueError:
				print("The System could not understand the audio")
			except sr.RequestError as e:
				print("System error; {0}".format(e))
