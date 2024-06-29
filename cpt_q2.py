def sum0f_k(a, k):
    d = dict()
    for i, j in enumerate(a):
        x = k - j
        if x in d:
            return [d[x], i]
        d[j] = i
    return  
s = list(map(int, input("Enter the list value : ").split()))
y = int(input("Enter the target : "))
print(sum0f_k(s, y))
print(int())