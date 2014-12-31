# You're challenge for today is to create a random password generator!
# For extra credit, allow the user to specify the amount of passwords to generate.
# For even more extra credit, allow the user to specify the length of the strings
# he wants to generate!
#
# there are 2 main ways to do this. either with ''.join or with pw += char(randint(min, max)).
# both are done in loops
from random import randint, choice

length = ''
complexity = ''

def check_int(var, prompt):
    while (not var.isdigit()):
        var = raw_input(prompt)
    return var

def password_gen(pw_length, how_complex):
    j = 0
    passwd = ''
    if (how_complex == '1'):
        numbers = range(65, 90) + range(97, 122)
        while (j < int(pw_length)):
            passwd += chr(choice(numbers))
            j += 1
        print passwd
    elif (how_complex == '2'):
        numbers = range(48, 57) + range(65, 90) + range(97, 122)
        while (j < int(pw_length)):
            passwd += chr(choice(numbers))
            j += 1
        print passwd
    elif (how_complex == '3'):
        numbers = range(33, 125)
        while (j < int(pw_length)):
            passwd += chr(choice(numbers))
            j += 1
        print passwd
    else:
        complexity = ''
        complexity = check_int(complexity, "Please select a complexity level between 1-3 (3 is more complex)\n")
        password_gen(length, complexity)

length = check_int(length, "How long do you want your password (Ints only)\n")
complexity = check_int(complexity, "How complex do you want your passwords? 1-3 (3 is more complex)\n")

password_gen(length, complexity)