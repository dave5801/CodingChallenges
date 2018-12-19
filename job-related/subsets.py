subs = {}

def getSubsets(anArray):

    if len(anArray) < 1:
        return []
    elif len(anArray) == 1 and repr(anArray) not in subs:
        subs[repr(anArray)] = 1
        return anArray

    '''
    if len(anArray) <= 1 and repr(anArray) not in subs:
        subs[repr(anArray)] == 1
        return anArray'''

    m = len(anArray)//2

    right = anArray[m: len(anArray)]
    left = anArray[0:m+1]

    return anArray + getSubsets(right) + getSubsets(left)