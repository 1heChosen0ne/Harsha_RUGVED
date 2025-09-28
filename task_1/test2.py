#take input of a str and check for palindrome
string = input("enter the word: ")
reverse_string = string[::-1]
if string == reverse_string:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

