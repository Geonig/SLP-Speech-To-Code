@Author Andreas

The Listener.py file is the listener module
I am still working on properly importing the listener module into the GUI .py 
for now the method is in the aGui.py file.

Next I intend to add an output window for the code.



------------------------------------------------------------------------
Researching how to make the input strings longer:

In the python3 interpreter:
>>>import speech_recognition 
>>>help()
>>>speech_recognition 

Gets you to the help file for speech_recognition.
In it the listen method is described like this:

listen(self, source, timeout=None, phrase_time_limit=None, snowboy_configuration=None)
     |      Records a single phrase from ``source`` (an ``AudioSource`` instance) into an ``AudioData`` instance, which it returns.
     |      
     |      This is done by waiting until the audio has an energy above ``recognizer_instance.energy_threshold`` (the user has started 
     speaking), and then recording until it encounters ``recognizer_instance.pause_threshold`` seconds of non-speaking or there is no more 
     audio input. The ending silence is not included.
     |      
     |      The ``timeout`` parameter is the maximum number of seconds that this will wait for a phrase to start before giving up and throwing 
     an ``speech_recognition.WaitTimeoutError`` exception. If ``timeout`` is ``None``, there will be no wait timeout.
     |      
     |      The ``phrase_time_limit`` parameter is the maximum number of seconds that this will allow a phrase to continue before stopping and 
     returning the part of the phrase processed before the time limit was reached. The resulting audio will be the phrase cut off at the time 
     limit. If ``phrase_timeout`` is ``None``, there will be no phrase time limit.
     |      
     |      The ``snowboy_configuration`` parameter allows integration with `Snowboy <https://snowboy.kitt.ai/>`__, an offline, high-accuracy, 
     power-efficient hotword recognition engine. When used, this function will pause until Snowboy detects a hotword, after which it will 
     unpause. This parameter should either be ``None`` to turn off Snowboy support, or a tuple of the form ``(SNOWBOY_LOCATION, 
     LIST_OF_HOT_WORD_FILES)``, where ``SNOWBOY_LOCATION`` is the path to the Snowboy root directory, and ``LIST_OF_HOT_WORD_FILES`` is a list 
     of paths to Snowboy hotword configuration files (`*.pmdl` or `*.umdl` format).
     |      
     |      This operation will always complete within ``timeout + phrase_timeout`` seconds if both are numbers, either by returning the 
     audio data, or by raising a ``speech_recognition.WaitTimeoutError`` exception.
     |  
