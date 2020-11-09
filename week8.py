# from tkinter import *
#
# window = Tk()
# window.title("Hello")
# window.geometry('200x100')
# window.mainloop()


def string_input():
    return input('Please enter your countable list: ')

def count_strings(s):
    d = dict()
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] = d[char] + 1
    return d

s = string_input()
d = count_strings(s)
print(d)

