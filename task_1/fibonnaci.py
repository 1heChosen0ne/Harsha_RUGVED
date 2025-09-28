
n = int(input("Enter the number of terms: "))
first, second = 0, 1
print("Fibonacci Sequence:", end=" ")
for i in range(n):
    print(first, end=" ")
    next = first + second
    first = second
    second = next
