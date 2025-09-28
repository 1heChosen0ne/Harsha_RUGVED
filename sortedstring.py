string = "harsha"
sorted_string = sorted(string)
print(sorted_string)
counts = {}
for char in sorted_string:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
for char, count in counts.items():
    print(char, count)