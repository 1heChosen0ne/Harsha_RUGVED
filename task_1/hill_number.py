num = int(input("Enter a number: "))
def is_hill_number(n):
    digits = [int(d) for d in str(n)]
    if len(digits) < 3:
        return False
    i = 0
    while i + 1 < len(digits) and digits[i] < digits[i + 1]:
        i += 1
    if i == 0 or i == len(digits) - 1:
        return False
    while i + 1 < len(digits) and digits[i] > digits[i + 1]:
        i += 1
    return i == len(digits) - 1
if is_hill_number(num):
    print(f"{num} is a hill number")
else:
    print(f"{num} is NOT a hill number")
#132 and 121 are they hill numbers check