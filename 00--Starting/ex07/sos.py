import sys

MORSE_CODE_DICT = { ' ' : '/',
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

            
def translate(message):
    result = ''
    for letter in message:
        if letter in MORSE_CODE_DICT:
            result += MORSE_CODE_DICT[letter]
    return result


def main():
    try:
        message  = sys.argv[1]
        print(message)
        res = translate(message.upper())
        print(res)
    except():
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()