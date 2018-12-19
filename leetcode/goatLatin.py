class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = S.split()

        result = []

        for i in range(len(words)):

            if words[i][0].lower() in vowels:
                words[i] += "ma"
            else:
                tmp = words[i][0]
                words[i] = words[i][1:] + tmp + "ma"
            words[i] += (i+1)*"a"
            result.append(words[i])

        return " ".join(result)

if __name__ == '__main__':
    s = Solution()
    x = s.toGoatLatin("The quick brown fox jumped over the lazy dog")
    print(x)

'''
"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
'''