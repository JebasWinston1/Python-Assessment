''' From the dict created in the above task (7), add new kv pairs. 
    - if the keys is already present, throw exception "Key already present" '''

class KeyAlreadyPresentException(Exception):
    pass

def create_dict(names, marks, my_dictionary = {}):
    for name,mark in zip(names, marks):
        try:
            if name not in my_dictionary.keys():
                my_dictionary[f'{name}'] = mark
            else:
                raise KeyAlreadyPresentException              
        except KeyAlreadyPresentException:
            print("Key already present")
            break
    return my_dictionary

names1 = ["rahul", "aswin", "abi"]
marks1 = [80, 90, 70]
names2 = ["ravi", "abi", "ram"]
marks2 = [70, 60, 70]

print(f"Names are: {names1}")
print(f"Marks are: {marks1}")
my_dictionary = create_dict(names1, marks1)
print(f"The Old Dictionary is: {my_dictionary}")
my_dictionary = create_dict(names2, marks2, my_dictionary)
print(f"The New Dictionary is: {my_dictionary}")