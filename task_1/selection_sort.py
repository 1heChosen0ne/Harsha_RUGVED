x = input("enter a string: ")
def selection_sort_string(s):
    s = list(s)
    n = len(s)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if s[j] < s[min_index]:
                min_index = j
        s[i], s[min_index] = s[min_index], s[i]
    return ''.join(s)
print(selection_sort_string(x))
