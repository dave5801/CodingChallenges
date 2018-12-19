'''
best practices
def find_dup(arr):
    return (i for i in arr if arr.count(i) > 1).next()
'''

def find_dup(arr):
    return[i for i in arr if arr.count(i)>1][0]


print(find_dup([10,10,1,1]))