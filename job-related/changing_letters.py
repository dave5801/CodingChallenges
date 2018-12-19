vowels = ['a','e', 'i', 'o', 'u']


def swap(st):
    #your code here
    for i in st:
        if i in vowels:
            st = st.replace(i, i.upper())
    return st

print(swap("Hello World!"))