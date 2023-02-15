''' Write a Python program to convert the given lists into a dictionary in a
way that item from list1 is the key and item from list2 is the value. '''

def create_dictionary(keys, values):
    my_dictionary = {}
    for key,value in zip(keys, values):
        my_dictionary[key] = value
    return my_dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(create_dictionary(keys, values))

''' Write a program to rename a key "city" to "location" in the following
dictionary. '''

sample_dict = { "name": "Kelly", "age":25, "salary": 8000, "city": "Newyork" }
sample_dict["location"] = sample_dict["city"]
del sample_dict["city"]
print(sample_dict)

''' Concatenate two lists in the following order using list comprehension. 
Expected output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] '''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(f"{i} {j}")
print(list3)

''' Use .format string method and f-string to print the statement 
“The value of pi is 3.143”. '''

pi = 3.1428571428
print("The value of pi is {}".format(pi.__round__(3)))
print(f"The value of pi is {pi.__round__(3)}")

''' Write a python program to find the even length words in the given
string. '''

s = "We are taking the python assignment."
print(s)
words = s.split(" ")
final = ""
for word in words:
    if "." in word and len(word) % 2 != 0:
        final += word + " "
    elif len(word)%2 == 0:
        final += word + " "
    else:
        pass
print(str(final))

''' Using list comprehension, form a new list by concatenating the given 2
lists.
Expected output:
['My', 'name', 'is', 'Kelly'] '''

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"] 
print([i+j for i,j in zip(list1,list2)])

''' Reverse the below string using string slicing. '''

Mystring = "Python Program"
print(Mystring[::-1])

''' You have given a Python list. Write a program to find value 20 in the list,
and if it is present, replace it with 200. Only update the first occurrence of
an item. '''

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)

''' Write an example to handle the “IOError” that occurs while opening and
appending some content into a file “sample.txt” in python using
exception handling? '''

try:
    file = open('sampletext.txt','r+')
    file.write("Hello, World")
    file.seek(0)
    print(file.read())
except IOError:
    print("IO Error Occurred!")
else:
    file.close()

''' You are given with a list. Create a new list that is having only the even
number in the given list, using lambda and filter function. '''

list1 = [10,11,12,13,14,15,16]
print(list(filter(lambda x: x%2 == 0, list1)))

''' Write a program to find the factorial of a number n using python function
recursion. '''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

''' Write a python program to find the given mac address is valid or not
using regular expressions. '''

import re
def validate_mac(mac_address):
    # regex = "[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}"
    regex = r"[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}:[^0][0-f]{2}"
    if re.search(regex, mac_address) != None:
        print("Valid")
    else: 
        print("Invalid")
validate_mac("00:01:23:a1:1f:20")