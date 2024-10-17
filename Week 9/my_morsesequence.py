morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.',
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..',
 '0': '-----', '1': '.----', '2': '..---',
 '3': '...--', '4': '....-', '5': '.....',
 '6': '-....', '7': '--...', '8': '---..',
 '9': '----.'
 }

def translateText(userStr):
    newStr = ""
    for char in userStr:
        if char == " ":
            newStr += "    "
        else:
            keyValue = char.upper()
            newStr += morse_code[keyValue]
    return newStr

print(translateText("SOS"))
print(translateText("MORSE CODE"))
print(translateText("Hello World"))