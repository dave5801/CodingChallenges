#https://www.codewars.com/kata/first-non-repeating-character/train/python

def first_non_repeating_letter(string):
    #your code here
    letters_by_count = {}

    non_repeating_letter = ""

    for char in string:
        if char.upper() in letters_by_count:
            char = char.upper()
            letters_by_count[char] = letters_by_count[char]+1
        elif char.lower() in letters_by_count:
            char = char.lower()
            letters_by_count[char] = letters_by_count[char]+1
        else:
            letters_by_count[char] = 1

    for k, v in letters_by_count.items():
        if letters_by_count[k] == 1:
            non_repeating_letter = k
            break


    return non_repeating_letter


if __name__ == '__main__':
   x = first_non_repeating_letter('a')
   print(x)
