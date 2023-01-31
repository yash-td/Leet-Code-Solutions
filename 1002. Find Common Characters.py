class Solution(object):
    '''
    
getting minimum frequency of each character from the first word and finally multipling that frequency with     characters from first word

    '''
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_word = set(words[0])
        res = []
        
        for char in first_word:
            n = min([word.count(char) for word in words]) 

            if n:
                res += [char] * n
        
        return res
