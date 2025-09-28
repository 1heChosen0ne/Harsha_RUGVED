n = int(input("Enter n: "))
def divide_string(string, n):
    length = len(string)
    if length % n != 0:
        print("Error: String length is not divisible by given n.")
        return
    parts = [string[i:i+n] for i in range(0, length, n)]

    if all(part == parts[0] for part in parts):
        print("Output:", ', '.join(f'"{part}"' for part in parts))
    else:
        print("Error: Parts are not of the same sequence.")
string = "abcdabcdabcdabcd"
divide_string(string, n)
