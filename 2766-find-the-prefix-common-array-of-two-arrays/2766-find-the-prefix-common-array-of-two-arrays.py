class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = [0] * (len(A))
        count = [0] * (len(A)+1)
        common = 0

        for i in range(len(A)):
            count[A[i]] += 1
            if count[A[i]] == 2:
                common += 1
            count[B[i]] += 1
            if count[B[i]] == 2:
                common += 1
            result[i] = common
        return result
            


        