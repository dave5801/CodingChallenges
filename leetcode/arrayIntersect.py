class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inters = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        seen = {}
        longer, shorter = [],[]
        
        if len(nums1) > len(nums2):
            longer = nums1
            shorter = nums2
        else:
            longer = nums2
            shorter = nums1
            
        for i in range(len(shorter)):
            if shorter[i] not in seen:
                seen[shorter[i]] = 1
                
        for j in range(len(longer)):
            if longer[j] in seen:
                inters.append(longer[j])
            else:
                seen[longer[j]] = 1
                
        return inters

if __name__ == '__main__':
    s = Solution()
    x = s.intersection([1,2,2,1], [2,2])
    print(x)