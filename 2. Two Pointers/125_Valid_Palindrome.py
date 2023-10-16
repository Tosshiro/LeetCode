'''
Description
LeetCode solution to 125. Valid Palindrome

@author: Jw
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890')
        # Creating string without non-alphanumeric characters from s
        string = (("".join(filter(whitelist.__contains__, s))).replace(" ", '')).lower()
        # Check if is palindrome
        if string == string[::-1]:
            return True
        else:
            return False

'''
Second solution: Two pointer solution

class Solution:
    def alphaNum(self,c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
        
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        
        while l < r:
            #Check if left index element is alphanumeric
            while l < r and not alphaNum(s[l]):
                l += 1
            #Check if right index element is alphanumeric
            while l < r and not alphaNum(s[r]):
                r += 1
            if s[l].lower() != s[r].lower():
                return False
        return True

#Time Complexity: O(n)
#Memory Complexity: O(1)
'''