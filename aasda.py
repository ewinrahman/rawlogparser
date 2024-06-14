# Python code to demonstrate
# First Non-Empty String in list
# using filter()

# initializing list
test_list = ["", "", "Akshat", "Nikhil"]

# printing original list 
print("The original list : " + str(test_list))

# using filter()
# First Non-Empty String in list
res = filter(None, test_list)

# printing result
print("The first non empty string is : " + str(res))
