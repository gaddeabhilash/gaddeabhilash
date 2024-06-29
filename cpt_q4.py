def remove_duplicate(b):
    s = list()
    for i in b:
        if i not in s:
            s.append(i)
    return len(s), s
a = list(map(int, input("Enter the list value : ").split()))
x, y = remove_duplicate(a)
print(f"{x}, nums = {y}")
print(f"{x}, nums = {y}")   
 