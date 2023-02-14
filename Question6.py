''' Print the elements in reverse order '''
def reverse(my_list):
    return my_list[::-1]

my_list = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
print(f"Old List: {my_list}")
print(f"Reversed List: {reverse(my_list)}")