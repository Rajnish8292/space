# format year-month-date
import numpy as np
def split(s, ch):
    str_array = [] # splitted string 
    str_length = len(s) # length of string
    word = "" # collection of char before every "ch" 
    if(ch == "") :
        for x in s:
            str_array.append(x)
        return str_array
    

    for i in range(str_length):
        c = s[i]
        if(c == ch):
            str_array.append(word)
            word = ""
        else  :
            word += c
    
    str_array.append(word)
    return str_array


def replace(s, ch_a, ch_b):
    str_length = len(s)
    str_dup = ""
    for i in range(str_length):
        c = s[i]
        if(c == ch_a):
            str_dup += ch_b
        else :
            str_dup += c
    
    return str_dup

def join(arr):
    arr_len = len(arr)
    joined_str = ""
    for i in range(arr_len):
        joined_str+=arr[i]



