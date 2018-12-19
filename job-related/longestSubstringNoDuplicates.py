def lengthOfLongestSubstring(s):
    print(s)
    if len(s) <= 1:
        return s
    returnDict = {}
    nonDups = {}
    sub = ''
    for i in range(len(s)):
       # print(i)
        if s[i] not in nonDups:
            #print(sub, s[i])
            nonDups[s[i]] = 1
            sub += s[i]
            if len(sub) == len(s):
               # print(sub)
                returnDict[sub] = len(sub)
        elif s[i] in nonDups: 
            #print(sub, s[i])
            returnDict[sub] = len(sub)
            sub = ''
            sub += s[i]
    #print(returnDict)
    x = sorted(returnDict, key=returnDict.get)
    return ''.join(x)