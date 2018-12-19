class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        incline = 0
        decline = len(A) - 1

        if len(A) < 3:
            return False

        if A[0] > A[1]:
            return False

        
        for i in range(1, len(A)):
            if A[incline] < A[incline + 1]:
                incline += 1
            
            if A[decline] < A[decline-1]:
                decline -= 1

        return 0 < incline == decline < len(A)-1

if __name__ == '__main__':
    s = Solution()
    x = s.validMountainArray([0,3,2,1])
    print(x)
