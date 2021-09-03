stdIn = input("Enter a character: ")
if stdIn.islower():
    print(stdIn + " is a lower case letter.")
elif stdIn.isdigit():
    print(stdIn + " is a digit.")
elif stdIn.isupper():
    print(stdIn + " is an upper case letter.")
elif stdIn.isalnum() == False:
    print(stdIn + " is a non-alphanumeric character.")