S = {}

def findIntersection(l1,l2):

    addtoSet(l1)
    addtoSet(l2)

    intersect = []

    for k in S:
        if S[k] > 1:
            intersect.append(k)

    return intersect

def addtoSet(arr):

    for i in range(len(arr)):
        if arr[i] in S:
            S[arr[i]] = S[arr[i]] + 1
        else:
            S[arr[i]] = 1

    return None

if __name__ == '__main__':
    l1 = [1,1,7,8,11]
    l2 = [5,4,1,11]

    x = findIntersection(l1,l2)
    print(x)