#gemstones
def gemstones(arr):
    #declare dictionary
    gems = {}

    #initialize count
    gem_count = 0


    #loop array
    for i in range(len(arr)):
        #use set() to eliminate duplicate letters in each string
        curr = "".join(set(arr[i]))
        for i in curr:
            if i not in gems:
                #if letter not in dictionary add with value of 1
                gems[i] = 1
            else:
                #else lettter in dictionary increment value
                gems[i] = gems[i] + 1

    #loop dictionary 
    for k in gems:
        #if key is greater value than one
        if gems[k] == len(arr):
            #increment count
            gem_count += 1

    return gem_count

if __name__ == '__main__':
    x = gemstones(['abcdde', 'baccd', 'eeabg']);
    print(x)