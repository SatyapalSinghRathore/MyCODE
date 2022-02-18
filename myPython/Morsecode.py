code={'.-': 'A', '-...': 'B','-.-.': 'C',
   '-..': 'D', '.': 'E', '..-.': 'F',
   '--.': 'G', '....': 'H', '..': 'I',
   '.---': 'J', '-.-': 'k', '.-..': 'L',
   '--': 'M', '-.': 'N', '---': 'O',
   '.--.': 'P', '--.-': 'Q', '.-.': 'R',
   '...': 'S', '-': 'T', '..-': 'U',
   '...-': 'V', '.--': 'W', '-..-': 'X',
   '-.--': 'Y', '--..': 'Z'}

def change(morse_code):
    morse_code=morse_code.split(' ')
    for no in range(0,len(morse_code)):
        print(code[morse_code[no]],end='')
    print(' ',end='')

def text_to_morse(morse):
    pass

def morse_to_text(morse):
    if '     ' in morse:
        m=morse.split('     ')
        for value in range(0,len(m)):
            change(m[value])
    elif '  ' in morse:
        m=morse.split('  ')
        for value in range(0,len(m)):
            change(m[value])
    elif '/' in morse:
        m=morse.split('/')
        for value in range(0,len(m)):
            change(m[value])
    else:
        change(morse)


if __name__=='__main__':
    morse=input('ENTER THE MORSE CODE:')
    morse_to_text(morse)