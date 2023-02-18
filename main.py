# Página inicial

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3

#Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[-2].id)

def speak(text):
  engine.say(text)
  engine.runAndWait()

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

while True:
  data = stream.read(4000)
  if len(data) == 0:
    break
  if rec.AcceptWaveform(data):
    result = rec.Result()

    print(type(result))