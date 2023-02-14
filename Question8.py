''' Write a function remove_duplicate() - remove the duplicate elements in the list. 
The order of the elements should not be changed. 
input: a list output: return the new list '''

def remove_duplicate(my_list):
    temp = []
    for num in my_list:
        if temp.count(num) < 1:
            temp.append(num)
        else:
            pass
    return temp

my_list = [1,2,3,1,2,3,4,5,6,5,4,3,1,1,2,3,2,3,24,4,4,0,5,6,7,7,8,544,7,8,98,545,321,23,5637,54,6,324,523,563,52345345]
print(my_list)
print(remove_duplicate(my_list))