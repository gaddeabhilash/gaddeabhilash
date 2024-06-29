def palindrome(s):
    if s == s[::-1]:
        return True
    return False


for k in range(5):
    st = "".join(input("Enter a string : ").split())
    li = ""
    for i in st:
        if i.isalnum():
            li.join(i)
    print(palindrome(li))
