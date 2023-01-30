class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            com = strs[0][i]
            for word in strs:
                try:
                    if word[i] != com:
                        return strs[0][:i]
                except IndexError:
                    return strs[0][:i]
                    
        return strs[0]







    
        
