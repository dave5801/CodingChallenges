#https://www.codewars.com/kata/arithmetic-progression/train/python
#7kyu

'''
Best Practices
def arithmetic_sequence_elements(a, r, n):
    return ', '.join(str(a + b * r) for b in xrange(n))
'''

def arithmetic_sequence_elements(a, r, n):

    ret = ""
    index = 0
    while(index<n):
        if index == n-1:
            ret += str(a)
        else:
            ret += str(a) + ", "
        a+= r
        index += 1
    return ret

print(arithmetic_sequence_elements(1, -3, 10))

