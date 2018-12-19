#documentation just to stay in the habit
#this finds the first recurring character of string and outputs the char
def findFirstRecur(aString):
    #use dict for O(1) lookup, that what is? Isn't it? 
    #that's right I'm studying algos again
    S = {}

    #catch empty strings...if you can, that is.
    if len(aString) == 0:
        return 'Empty'

    #lets check every last one of those characeters
    for i in range(len(aString)):

        #if i find an existing key, I return it
        if aString[i] in S:
           return aString[i]
        else:
        #otherwise just do whatever, who cares
            S[aString[i]] = 1

    #hopefully this won't ever happen...why am I saying this?
    return "No recurring characters"

if __name__ == '__main__':
    s = ""
    print(findFirstRecur(s))