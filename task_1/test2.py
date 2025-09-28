#take input of a str and check for palindrome
string = input("enter the word: ")
x = 0
for i in string:
    if (i == string(len(string)-i-1)):
        print("ok")
    else:
        break



