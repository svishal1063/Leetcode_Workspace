s = "A man, a plan, a canal: Panama"
alphanum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
l = 0
r = len(s)-1
isPalindrome = False

while l < r:
    if s[l] not in alphanum:
        l +=1 
    elif s[r] not in alphanum:
        r -= 1
    elif s[l].lower() == s[r].lower():
            isPalindrome = True
            l += 1
            r -= 1
    else:
        isPalindrome = False
        break

print(isPalindrome)

##This solutions employs two-pointer solution where two pointers are used to traverse the string from left and right.
##If the character at left pointer is not alphanumeric, increment the left pointer.
##If the character at right pointer is not alphanumeric, decrement the right pointer.
##If the characters at left and right pointers are alphanumeric and equal, increment the left pointer and decrement the right pointer.
##If the characters at left and right pointers are alphanumeric and not equal, break the loop and return False.
##If the loop completes without breaking, return True.
##This solution has O(n) time complexity where n is the length of the string.