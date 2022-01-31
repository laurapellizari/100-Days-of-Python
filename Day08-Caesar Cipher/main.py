#Day 08 - Caesar Cipher
import art as a

alfab = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@',
         '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', ',', '/', '<', '>', '.', ';', ':', ' ']

def crypt (text, message, shift):
    result = ''
    if(text == 'encode'):
        for txt in message:
            pos = alfab.index(txt)
            new_pos = pos + shift
            if(new_pos > 26):
                result += alfab[new_pos - len(alfab)]
            else:
                result += alfab[new_pos]

    elif (text == 'decode'):
        for txt in message:
            pos = alfab.index(txt)
            new_pos = pos - shift
            if (new_pos > 26):
                result += alfab[new_pos - len(alfab)]
            else:
                result += alfab[new_pos]
    else:
        print("Chose encode or decode. Can't find the word typed.")
    return print(f"Here's the encoded result: {result}")

print(a.logo)
text = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
message = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))
crypt(text, message, shift)
again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
while again != 'no':
    text = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    message = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    crypt(text, message, shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")








