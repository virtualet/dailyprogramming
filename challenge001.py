# create a program that will ask the users name, age, and reddit username.
# have it tell them the information back, in the format:
# your name is (blank), you are (blank) years old, and your username is (blank)
# for extra credit, have the program log this information in a file to be accessed later

__author__ = 'echoecho'

name = raw_input("What's your real name?\n")
age = raw_input("What's your age?\n")

# Checking if age is a number
while age.isdigit() == 0:
    age = raw_input("That's not a number. What's your age?\n")

reddit_handle = raw_input("What's your reddit handle?\n")

print "Your name is %r, you are %r years old, and your username is %r" % (name, age, reddit_handle)

print "Writing variables to file /Users/echoecho/PycharmProjects/dailyprogrammer/userdata.txt"
to_file = "/Users/echoecho/PycharmProjects/dailyprogrammer/userdata.txt"
out_file = open(to_file, 'w')

out_file.write(name)
out_file.write("\n")
out_file.write(age)
out_file.write("\n")
out_file.write(reddit_handle)
out_file.write("\n")

out_file.close()

print "Reading userdata file"
userdata_file = open(to_file)
print userdata_file.read()
userdata_file.close()