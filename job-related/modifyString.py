#this came from a google interview.

'''
You have a word and a dictionary of target words. Design an algorithm that can turn the word into all applicable target word with only by adding letters anywhere into the word. You cannot remove a letter. The format should encode the transformation in some way you decide.
Starting Word: CAT
target word CATD 
'''

#Going to try modfication of Longest Common Subsequence problem
def modifyString(start, target):
    
    changes = None
    change_count = 0

    longer = 0

    if len(start) <= len(target):
        longer = len(target)
    else:
        longer = len(start)


    m = [[0 for rows in range(longer)] for cols in range(longer)]
    print(m)
    for row in range(longer):
        if row < len(start):
            print(start[row])
        



    return [changes, change_count]

if __name__ == '__main__':
    modifyString("CAT", "CATD")