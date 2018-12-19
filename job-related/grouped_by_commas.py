#6kyu

'''
#https://www.codewars.com/kata/grouped-by-commas/train/python

Best Practices
def group_by_commas(n):
    return "{:,}".format(n)
'''

#citation: https://mkaz.tech/code/python-string-format-cookbook/
def group_by_commas(n):
    #your code here
    return "{:,}".format(n)


print(group_by_commas(35235235))