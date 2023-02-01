class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # here we create two hash maps / dictionaries and map characters from both the strings to each other if 
        # they are not already mapped
        # if we find a character in the string which is new we add it to our dictionary and if a character 
        # is repeated then we check if it is correctly mapped, if it does not equall to the mapped value then 
        # we return false
        
        if len(s) != len(t):
            return False
        else:
            m1, m2 = {} , {}
            for i in range(len(s)):
                ch1, ch2 = s[i], t[i]
                if ch1 not in m1: # e : a, g:d 
                    m1[ch1] = ch2
                if ch2 not in m2: # a : e, d:g
                    m2[ch2] = ch1
                
                if m1[ch1] != ch2 or m2[ch2] != ch1:
                    return False
                
        return True 
