# write a program that can encrypt texts with an alphabetical caesar cipher.
# This cipher can ignore numbers, symbols, and whitespace.
# For extra credit, add a "decrypt" function to your program!
__author__ = 'echoecho'

option = ''
text = raw_input("what's the text\n")

while 1:
    option = raw_input("Do you want to encode or decode? e or d\n")
    if option == 'e':
        print text.encode('rot13')
        break
    elif option == 'd':
        print text.decode('rot13')
        break