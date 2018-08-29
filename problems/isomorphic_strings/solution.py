class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_mapping = {}
        marked = set()
        
        for i in xrange(len(s)): # runs n times
            if char_mapping.has_key(s[i]): # constant
                if char_mapping[s[i]] != t[i]: # constant
                    return False
            else:
                if t[i] in marked: # constant because sets are actually dicts pointing to None
                    return False
                else:
                    char_mapping[s[i]] = t[i] #constant
                    marked.add(t[i]) #constant
        return True        