# https://pypi.org/project/SpeechRecognition/
# pip install SpeechRecognition
# pip install PyAudio
# Microsof Visual C++ 14.0
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# pip install --upgrade setuptools 
#
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Say something fool!")
	audio = r.listen(source)

	try:
		text =  r.recognize_google(audio)
		print(f'You Said: {text}')
	except:
		print("Sorry I couldn't understand you...")