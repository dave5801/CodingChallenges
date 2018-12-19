#add one to given array, and factor in carry
def addOneToArray(anArray):

    if not anArray:
        return [1]

    #initialize carry
    carry = 1
    results = []
    carried = False

    #loop array
    for i in range(len(anArray)-1,-1,-1):
        #if less then 9 add one, no carry
        if anArray[i] < 9:
            anArray[i] += carry
            carry = 0
            carried = True
        # if 9 add one, then carry
        elif anArray[i] == 9 and carried is False:
            anArray[i] = 0
            carry = 1

        #add to results list
        results.append(anArray[i])

    #add carried one to start of list
    if carry:
        results.append(carry)

    #list has to be reversed then returned
    return results[::-1]

if __name__ == '__main__':
    x = addOneToArray([9])
    print(x)