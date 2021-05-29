import matplotlib.pyplot as plt

"""
File: hack.py
Author: David W. Juedes
Purpose: To uncover the secret message stored in the file "ciphertext"
by doing a brute force search of all possible 3 letter passwords.

"""
import math
import string

def count_chars(X,c1,c2):
    sum=0
    for i in range(len(X)):
        if (X[i]==c1):
            sum=sum+1
        elif (X[i]==c2):
            sum=sum+1
    return sum
def count_char(X,c1):
    sum=0
    for i in range(len(X)):
        if (X[i]==c1):
            sum=sum+1
    return sum


"""

Convert the string to a list of integers using the ord function.

"""
def string_to_int_list(X):
    output_list = []
    for i in range(len(X)):
        output_list.append(ord(X[i]))
    return output_list



"""
Compute the distance between two lists.
The assumption is that the lists have the same number of elements.
The last value is the total number of characters in the same.

The rest are character counts.

"""



def distance(X1,X2):
    total_chars_X1 = X1[len(X1)-1]
    total_chars_X2 = X2[len(X2)-1]
    sum=0
    for i in range(len(X1)-1):
        sum = sum + ((X1[i]/total_chars_X1)-(X2[i]/total_chars_X2))**2
    return math.sqrt(sum)

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


f=open("ciphertext")
data=f.read()
#print("Data in file:")
data_list = []
for i in data.split():
    data_list.append(int(i))


english_list = [7187, 11606, 7026, 8506, 3672, 19122, 125185]

best_dist = 10000000
best_password = ""

progress = 0
print("Progress on trying all 17576 passwords")
# Try all possible (17,536) passwords of length 3
counter = 0
x = []
y = []
for c1 in "abcdefghijklmnopqrstuvwxyz":
    for c2 in "abcdefghijklmnopqrstuvwxyz":
        for c3 in "abcdefghijklmnopqrstuvwxyz":
            password=c1+c2+c3
            password_list=string_to_int_list(password)
            decrypted = decrypt(data_list,password_list)
            #print(decrypted)
            progress=progress+1
            if (progress%500 ==0):
                print(progress)
            #print("The decrypted text as a string:")
            ds=list_to_string(decrypted)

            char_vector = [count_chars(ds,"A","a"),count_chars(ds,"E","e"),
               count_chars(ds,"I","i"),count_chars(ds,"O","o"),
               count_chars(ds,"U","u"),count_char(ds," "),len(data)]
            dist = distance(english_list,char_vector)
            x.append(counter)
            counter = counter + 1
            y.append(dist)
            if (dist<best_dist):
                best_dist = dist
                best_password = password
    
print("Winning password = "+best_password)

plt.figure(0,figsize=(12,6))
plt.plot(x,sorted(y))

plt.figure(1, figsize=(12,6))
plt.plot(x[0:26],sorted(y)[0:26])

plt.figure(2, figsize=(12,6))
plt.plot(x,y)

