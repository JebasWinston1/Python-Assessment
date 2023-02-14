''' Find the number of spaces in the provided string '''

def total_space(my_string):
    return len(my_string.split(" ")) -1

my_string = "Hi! How are you?"
print(f"Number of spaces in the string ({my_string}) is : {total_space(my_string)}")
