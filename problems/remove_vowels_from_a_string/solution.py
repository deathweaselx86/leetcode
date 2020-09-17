import re

class Solution:
    def removeVowels(self, S):
        r =  re.compile(r'[aeiou]+')
        return r.sub('', S)