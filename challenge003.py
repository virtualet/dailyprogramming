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