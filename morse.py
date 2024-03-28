from playsound import playsound
import time


# The \u25CF is indicate the black circle and \u2014 is indicate the em dash
letter = {
    "A": ['\u25CF \u2014', 'letter/A_morse_code.ogg'],
    "B": ['\u2014 \u25CF \u25CF \u25CF', 'letter/B_morse_code.ogg'],
    "C": ['\u2014 \u25CF \u2014 \u25CF', 'letter/C_morse_code.ogg'],
    "D": ['\u2014 \u25CF \u25CF', 'letter/D_morse_code.ogg'],
    "E": ['\u25CF', 'letter/E_morse_code.ogg'],
    "F": ['\u25CF \u25CF \u2014 \u25CF', 'letter/F_morse_code.ogg'],
    "G": ['\u2014 \u2014 \u25CF', 'letter/G_morse_code.ogg'],
    "H": ['\u25CF \u25CF \u25CF \u25CF', 'letter/H_morse_code.ogg'],
    "I": ['\u25CF \u25CF', 'letter/I_morse_code.ogg'],
    "J": ['\u25CF \u2014 \u2014 \u2014', 'letter/J_morse_code.ogg'],
    "K": ['\u2014 \u25CF \u2014', 'letter/K_morse_code.ogg'],
    "L": ['\u25CF \u2014 \u25CF \u25CF', 'letter/L_morse_code.ogg'],
    "M": ['\u2014 \u2014', 'letter/M_morse_code.ogg'],
    "N": ['\u2014 \u25CF', 'letter/N_morse_code.ogg'],
    "O": ['\u2014 \u2014 \u2014', 'letter/O_morse_code.ogg'],
    "P": ['\u25CF \u2014 \u2014 \u25CF', 'letter/P_morse_code.ogg'],
    "Q": ['\u2014 \u2014 \u25CF \u2014', 'letter/Q_morse_code.ogg'],
    "R": ['\u25CF \u2014 \u25CF', 'letter/R_morse_code.ogg'],
    "S": ['\u25CF \u25CF \u25CF', 'letter/S_morse_code.ogg'],
    "T": ['\u2014', 'letter/T_morse_code.ogg'],
    "U": ['\u25CF \u25CF \u2014', 'letter/U_morse_code.ogg'],
    "V": ['\u25CF \u25CF \u25CF \u2014', 'letter/V_morse_code.ogg'],
    "W": ['\u25CF \u2014 \u2014', 'letter/W_morse_code.ogg'],
    "X": ['\u2014 \u25CF \u25CF \u2014', 'letter/X_morse_code.ogg'],
    "Y": ['\u2014 \u25CF \u2014 \u2014', 'letter/Y_morse_code.ogg'],
    "Z": ['\u2014 \u2014 \u25CF \u25CF', 'letter/Z_morse_code.ogg'],
}

numb = {
    "0": ['\u2014 \u2014 \u2014 \u2014 \u2014', 'number/0_number_morse_code.ogg'],
    "1": ['\u25CF \u2014 \u2014 \u2014 \u2014', 'number/1_number_morse_code.ogg'],
    "2": ['\u25CF \u25CF \u2014 \u2014 \u2014', 'number/2_number_morse_code.ogg'],
    "3": ['\u25CF \u25CF \u25CF \u2014 \u2014', 'number/3_number_morse_code.ogg'],
    "4": ['\u25CF \u25CF \u25CF \u25CF \u2014', 'number/4_number_morse_code.ogg'],
    "5": ['\u25CF \u25CF \u25CF \u25CF \u25CF', 'number/5_number_morse_code.ogg'],
    "6": ['\u2014 \u25CF \u25CF \u25CF \u25CF', 'number/6_number_morse_code.ogg'],
    "7": ['\u2014 \u2014 \u25CF \u25CF \u25CF', 'number/7_number_morse_code.ogg'],
    "8": ['\u2014 \u2014 \u2014 \u25CF \u25CF', 'number/8_number_morse_code.ogg'],
    "9": ['\u2014 \u2014 \u2014 \u2014 \u25CF', 'number/9_number_morse_code.ogg'],
}


def letter_sound(character):
    if character in letter:
        # play morse code if the character is in letter dictionary
        playsound(letter.get(character)[1])
        time.sleep(0.1)
    elif character in numb:
        # play morse code if the character is in numb dictionary
        playsound(numb.get(character)[1])
        time.sleep(0.1)


def morse_symbol(character):
    if character in letter:
        print(letter.get(character)[0])
    elif character in numb:
        print(numb.get(character)[0])


flg = True
print('If you want to exit the program, type "exit"')
while flg:
    entire = str(input('Please enter your text: ')).upper().strip()
    letter_list = [char for char in entire]
    if entire == 'exit'.upper():
        flg = False
    else:
        for char in letter_list:
            if char == ' ':
                time.sleep(0.4)
                continue
            else:
                morse_symbol(char)
                letter_sound(char)
