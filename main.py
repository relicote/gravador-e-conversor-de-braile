import speech_recognition as sr
import PIL
# from model import charToArray, asciicodes, brailles

braille_dict = {
    'a': '100000',
    'b': '101000',
    'c': '110000',
    'd': '110100',
    'e': '100100',
    'f': '111000',
    'g': '111100',
    'h': '101100',
    'i': '011000',
    'j': '011100',
    'k': '100010',
    'l': '101010',
    'm': '110010',
    'n': '110110',
    'o': '100110',
    'p': '111010',
    'q': '111110',
    'r': '101110',
    's': '011010',
    't': '011110',
    'u': '100011',
    'v': '101011',
    'w': '011101',
    'x': '110011',
    'y': '110111',
    'z': '100111',
    ' ': '000000',
}

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)

    print('Pode falar que já estou gravando')

    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    print(texto)
    

def text_to_braille(texto):
    braille_text = ""
    for char in texto:
        char = char.lower()
        if char in braille_dict:
            braille_text += braille_dict[char] + ' '
        else:
            braille_text += char + ' '  # Mantém caracteres não mapeados no texto final
    return braille_text

braille_result = text_to_braille(texto)
print("Texto em Braille:", braille_result)