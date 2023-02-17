# Página inicial

import speech_recognition as sr

#Cria um reconhecedor
r = sr.Recognizer()

#Abrir o microfone ara captura
with sr.Microphone() as source:
  while True:
     audio = r.listen(source) #Define o microfone como fonte de áudio

     print(r.recognize_google(audio, language="pt-BR")) #Acessa o reconhecedor e retorna o texto

