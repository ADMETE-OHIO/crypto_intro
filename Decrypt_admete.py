"""
File: Decrypt.py
Author: David W. Juedes
Purpose:

A Python program to decrypt a file.
The file is ciphertext located in your current directory.

The program asks for a password string.
It then decrypts the ciphertext file (a list of integers) using the password and prints the decrypted version.

"""

import string
"""

Convert the string to a list of integers using the ord function.

"""
def string_to_int_list(X):
    output_list = []
    for i in range(len(X)):
        output_list.append(ord(X[i]))
    return output_list


"""

decrypt a list of integers using a list of integers from the password.

Here, we use the XOR function (^ in Python) to encrypt the list.


""" 

def decrypt(X,password):
    output_list = []
    counter=0
    for i in range(len(X)):
        char_val = X[i]
        encrypted_val = char_val ^ password[counter]
        output_list.append(encrypted_val)
        counter = (counter+1)%len(password)
    return output_list

"""

Convert list of ints to a string.
Make all unprintable characters into _

"""
def list_to_string(X):
    output_str=""
    for i in X:
        c = chr(i)
        if c.isalpha():
            output_str += c
        elif string.punctuation.rfind(c)>=0: 
            output_str +=c
        elif c.isdecimal():
            output_str +=c
        elif c.isspace():
            output_str +=c
        else:
            output_str += "_"
            
            
    return output_str



f=open("ciphertext","r")
data=f.read()
print("Data in file:")
data_list = []
for i in data.split():
    data_list.append(int(i))

#print("File as a list of integers:")
#print(data_list)
password=input("Enter a password:")
password_list=string_to_int_list(password)
#print("Password as a list of integers:")
#print(password_list)

decrypted = decrypt(data_list,password_list)
#print(decrypted)
print("The decrypted text as a string:")
print(list_to_string(decrypted))


#print(decrypted)


