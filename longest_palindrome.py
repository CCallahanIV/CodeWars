def longest_palindrome(s):
    pal_length = 0
    for i in range(len(s)):
        for j in range(len(s)-i+1):
            sub_s = s[i:i+j]

            if sub_s == sub_s[::-1] and len(sub_s) > pal_length:
                pal_length = len(sub_s)

    return pal_length



print(longest_palindrome("a"))
print(longest_palindrome("baa"))
print(longest_palindrome("aa"))
print(longest_palindrome("aab"))
print(longest_palindrome("abcdefghba"))
print(longest_palindrome("baablkj12345432133d"))