import speech_recognition as sr
import PIL
from model import charToArray, asciicodes, brailles

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)

    print('Pode falar que já estou gravando')

    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    print(texto)

ascii_braille = {}

texto = len(asciicodes)
counter = 0

while counter < texto:
    ascii_braille[asciicodes[counter]] = brailles[counter]
    counter = counter + 1

print(texto)