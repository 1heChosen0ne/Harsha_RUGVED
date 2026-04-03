#take str input and count number of words
string = str(input("enter the sentence: "))
x = 0
for i in string:
    if (i==" "):
        x += 1
print("the number of words are ", x+1)