"""
File: Encrypt.py
Author: David W. Juedes
Purpose:

A Python program to encrypt a file.
The file is plaintext located in your current directory.

The program asks for a password string.
It then encrypts the plaintext file (with the password) and creates an encrypted version in a file called ciphertext.

This file is a list of integers, since many of the encrypted characters may be unprintable.

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

Encrypt a list of integers using a list of integers from the password.

Here, we use the XOR function (^ in Python) to encrypt the list.


""" 

def encrypt(X,password):
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
Convert unprintable characters to underscores (_).

"""
def list_to_string(X):
    output_str=""
    for i in range(len(X)):
        c = chr(X[i])
        if c.isalpha():
            output_str += c
        elif string.punctuation.rfind(c)>=0: 
            output_str +=c
        elif c.isdecimal():
            output_str +=c
        elif c.isspace():
            output_str +=" "
        else:
            output_str += "_"
    return output_str


f=open("plaintext","r")
data=f.read()
print("Data in file:")
print(data)
print("File as a list of integers:")
data_list = string_to_int_list(data)
print(data_list)
print(" ")
password=input("Enter a password:")
password_list=string_to_int_list(password)
print("Password as a list of integers:")
print(password_list)
encrypted = encrypt(data_list,password_list)
print("Encrypted data a list:")
print(encrypted)
print("Encrypted data as string ")
print(list_to_string(encrypted))

### Write the data to a file.
f1=open("ciphertext","w")
for i in encrypted:
    f1.write(str(i)+" ")
    
#print("Decryption is the same as encryption for this type of algorithm")
#decrypted=encrypt(encrypted,password_list)
#print(decrypted)


