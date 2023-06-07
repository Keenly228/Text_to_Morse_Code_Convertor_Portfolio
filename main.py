from art import logo

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

#Translator
def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse_code += ' '
    return morse_code

print(logo)

#Brain
while True:
    answer = input("Do you want to translate text into Morse code? Type 'y' or 'n' ").lower()

    if answer.lower() == "y":
        user_input = input("Enter the string you want to translate: ")
        morse_output = text_to_morse(user_input)
        print("Your morse code: ", morse_output)
    else:
        print("Goodbye! Thank you for using our translator.")
        break
