''' Print the multiples of 7 from 147 to 210 '''
def seven_multiples():
    print("The multiples of seven from 147 to 210 are: ")
    for num in range(147,211,7):
        print(num)

seven_multiples()

''' Create a dictinary with whose keys are names and values are their marks. 
    Note 1. The names can be of any length 
         2. Assume name and marks provided will be of same length
         3. There are two lists name=[ "rahul", "aswin", "abi"] marks = [80, 90, 70]'''

def create_dict(names, marks):
    my_dictionary = {}
    for name,mark in zip(names, marks):
        my_dictionary[f'{name}'] = mark
    return my_dictionary

names = [ "rahul", "aswin", "abi"]
marks = [80, 90, 70]
print(f"Names are: {names}")
print(f"Marks are: {marks}")
print(f"The Dictionary is: {create_dict(names, marks)}")