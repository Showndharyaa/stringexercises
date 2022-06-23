#Program to identify if a given string is a palindrome

def isPalindrome(s):
    #print (s == s[::-1])
    if (s == s[::-1]):
        return True

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("Yes a palindrome")
else:
    print("Not a palindrome")
