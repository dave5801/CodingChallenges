'''
best practices 
def find_dup(arr):
    return sum(arr) - sum(range(1, max(arr)+1))
'''

def find_dup(arr):
    #your code here
    return[i for i in arr if arr.count(i)>1][0]