class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_map = {}
        words = str.split(" ")
        visited = set()
        
        if len(words) <> len(pattern): # no chance for a match if there are too many words or the pattern is too long
            return False
        for i in xrange(len(words)):
            if pattern_map.has_key(words[i]):
                if pattern[i] != pattern_map[words[i]]:
                    return False
            else:
                if pattern[i] not in visited:
                    pattern_map[words[i]] = pattern[i]
                    visited.add(pattern[i])
                else:
                    return False
        return True
        