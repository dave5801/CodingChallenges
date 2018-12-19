class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        if length < 1:
            return length

        longest = 1
        seenSubstrings = [s[0]]

        for i in range(len(s)):
            current = s[i]

            while current in seenSubstrings:
                seenSubstrings = seenSubstrings[1:]

            seenSubstrings.append(current)

            if len(seenSubstrings) > longest:
                longest = len(seenSubstrings)

        return longest
        




if __name__ == '__main__':
    s = Solution()
    x = s.lengthOfLongestSubstring("au")
    print(x)