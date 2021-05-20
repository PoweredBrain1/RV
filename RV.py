#Install
# pip3 install SpeechRecognition pydub


import speech_recognition as sr
filename = "audio.wav"

# initialize the recognizer
r = sr.Recognizer()
#The below code is responsible for loading the audio file, and converting the speech into text using Google Speech Recognition:

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language='pt-PT')
    print(text)