class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        res = []
        for num in range(left,right+1):
            num_str = str(num)
            if '0' not in num_str:
                for x in list(map(int, str(num))):
                    if num % x != 0:
                        isSelfDividing = False
                        res.append(num)

                    else:
                        isSelfDividing = True
                        
            else:
                continue
        return sorted(set([x for x in range(left,right+1) if '0' not in str(x)]) - set(res))


