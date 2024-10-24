import numpy as np
import src.stringMethod as sm
import math
# create char code 
char_string = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM 1234567890`~!@#$%^&*()[]<>,./?\'\"\\*-=+_\r\n:;"
char_code = {}
code_char = {}
for i in range(len(char_string)):
    char_code[char_string[i]] = i
    code_char[i] = char_string[i]
# ====================================================================================================================

#print(char_code, "\n\n\n", code_char)
def encryption(txt, key):
    key_arr = sm.split(key, "")
    txt_arr = sm.split(txt, "")
    key_len = len(key_arr)
    txt_len = len(txt_arr)
    if(key_len == 0):
        return sm.join(key_arr)
    for i in range(key_len):
        key_arr[i] = char_code[key_arr[i]]
    
    for i in range(txt_len):
        txt_arr[i] = char_code[txt_arr[i]]


    total_block = math.floor(txt_len/key_len)
    block_size = key_len

    encrypted_txt = ""
    index = 0
    for i in range(total_block):
        for j in range(block_size):
            index = block_size*i + j
            encrypted_txt += str(key_arr[j] + txt_arr[block_size*i + j]) + " "
    index+=1
    while(index < txt_len):
        encrypted_txt += str(txt_arr[index]) + " "
        index += 1
    return encrypted_txt
    #print("total block", total_block, txt_len, key_len)

    
def decryption(cipher, key):
    key_arr = sm.split(key, "")
    cipher_arr = sm.split(cipher, " ")
    key_len = len(key_arr)
    cipher_len = len(cipher_arr)-1
    if(key_len == 0):
        return sm.join(key_arr)
    for i in range(key_len):
        key_arr[i] = char_code[key_arr[i]]
    
    for i in range(cipher_len):
        cipher_arr[i] = int(cipher_arr[i])
    
    total_block = math.floor(cipher_len/key_len)
    block_size = key_len
    decrypted_txt = ""
    index = 0
    for i in range(total_block):
        for j in range(block_size):
            index = block_size*i + j
            # print(decrypted_txt)
            decrypted_txt += code_char[abs(cipher_arr[index] - key_arr[j])]
    

    # print(index, cipher_len)
    index += 1
    while(index < cipher_len):
        decrypted_txt += code_char[cipher_arr[index]]
        index += 1
    return decrypted_txt


x = encryption("", "12345")

print(x)


y = decryption(x, "12345")