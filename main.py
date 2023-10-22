import speech_recognition as sr
import PIL
# from model import charToArray, asciicodes, brailles

braille_dict = {
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'm': '⠍',
    'n': '⠝',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'y': '⠽',
    'z': '⠵',
    ' ': ' ',
}




rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)

    print('Pode falar que já estou gravando')

    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    # print(texto)
    

def text_to_braille(texto):
    braille_text = ""
    for char in texto:
        char = char.lower()
        if char in braille_dict:
            braille_text += braille_dict[char] + ' '
        else:
            braille_text += char + ' '  # Mantém caracteres não mapeados no texto final
    return braille_text


print('Você disse:', texto) #Printando o texto falado

braille_result = text_to_braille(texto)

print("Texto em Braille:", braille_result) #exibindo o texto em braile numerico
