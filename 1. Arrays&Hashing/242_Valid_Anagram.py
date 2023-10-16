'''
Description
LeetCode solution to 242. Valid Anagram

@author: Jw
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Check if number of letters of s and t is the same
        if len(s) != len(t):
            return False

        lis = [i for i in t]
        for i in s:
            if i in lis:   #check if every letter in s is in t
                lis.remove(i)  #remove checked letter
            else:
                return False   #if letter in s not in t, s & t not valid anagram
        return True

    #Time Complexity: O(n^2)