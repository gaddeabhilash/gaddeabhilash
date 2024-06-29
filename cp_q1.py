def palindrome_substr(s):
    right_str = left_str = 0
    str_ln = 0
    lent = len(s)
    for i in range(lent):
        left, right = i, i
        while left >= 0 and right < lent and s[left] == s[right]:
            if str_ln < right-left+1:
                right_str = right
                left_str = left
                str_ln = right-left+1
            left -= 1
            right += 1
    for i in range(lent):
        left, right = i, i+1
        while left >= 0 and right < lent and s[left] == s[right]:
            if str_ln < right-left+1:
                right_str = right
                left_str = left
                str_ln = right - left + 1
            left -= 1
            right += 1
    return s[left_str:right_str+1]


for j in range(5):
    st = input("enter a string with palindrome in its substring : ")
    print(palindrome_substr(st))
