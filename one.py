# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME Is the input of the function. The first line of cide has been defined as below.

def hello_name(user_name):
    """Display a simple greeting."""
    print("Hello_" + user_name.upper() + "!")

hello_name("USERNAME")

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    first_odds = list(range(1,100))
    print(first_odds)

# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of code has been defined as below.
def max_num_in_list(a_list):
    highest = a_list[0]
    for number in a_list:
        if number > highest:
            highest = number
    return highest
    
a_list = [2, 5, -5, -21, 23, 10]
highest_num = max_num_in_list(a_list)
print(highest_num)

# Question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    leap = False
    if a_year % 4 == 0:
        leap == False
    elif a_year % 4 == 0:
        if a_year % 100 == 0 and a_year %400 == 0:
            leap = False
    else:
        leap == False
    return leap
print(bool(is_leap_year))

# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
d_list = [25,16,18,17,24]
sorted_list = sorted(a_list)
#sorted(l) ==
range_list=list(range(min(a_list), max(a_list)+1))
if sorted_list == range_list:
   print("True")
else:
   print("False")

