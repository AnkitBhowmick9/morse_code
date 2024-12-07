# Dictionary to map characters to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ' '
}

def text_to_morse(text):
    """
    Convert the given text to Morse code.
    :param text: Input text as a string
    :return: A list of Morse code strings
    """
    # Convert each character to uppercase and find its Morse code
    morse_code = [MORSE_CODE_DICT[char.upper()] for char in text]
    return morse_code

# Get input from the user
text = input("Please enter the text for Morse code: ")

# Convert the input text to Morse code
morse_result = text_to_morse(text)

# Display the result
print(list(text))  # Original text as a list of characters
print(morse_result)  # Morse code as a list of strings
