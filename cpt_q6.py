def palindrome(n):
    temp = n
    s = 0
    while n > 0:
        i = n % 10
        s = 10 * s + i
        n = int(n/10)
    if s == temp:
        return True
    else:
        return False


for j in range(5):
    num = int(input("Enter a number : "))
    print(palindrome(num))
