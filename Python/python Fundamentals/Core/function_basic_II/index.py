
#! 1)Countdown - Create a function that accepts a number as an input. 
#                Return a new list that counts down by one, 
#                from the number (as the 0th element) down to 0 (as the last element).
#                Example: countdown(5) should return [5,4,3,2,1,0]



def countdown(number):
    my_list = []
    for i in range(number, -1, -1):
        my_list.append(i)
    # print(my_list)
    return my_list

# print(countdown(6))
# print(countdown(5))


#!  2)Print and Return - Create a function that will receive a list with two numbers. 
#                        Print the first value and return the second.
#                        Example: print_and_return([1,2]) should print 1 and return 2


def print_and_return(new_list):
    print("My First value in list",new_list[0])
    return new_list[1]

# print(print_and_return([3,4]))
# print(print_and_return([1,2]))


#! 3) First Plus Length - Create a function that accepts a list 
#                         and returns the sum of the first value in the list plus the list's length.
#                         Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


def first_plus_length(number):
    return number[0] + len(number)


# print(first_plus_length([4,6,5]))
# print(first_plus_length([10,2,8]))


#! 4)Values Greater than Second - Write a function that accepts a list and creates 
#                                 a new list containing only the values 
#                                 from the original list that are greater than its 2nd value. 
#                                 Print how many values this is and then return the new list. 
#                                 If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]


def values_greater_than_secund(list):
    if len(list) < 2:
        return False
    my_list = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            my_list.append(list[i])

    print(len(my_list))
    return my_list


# print(values_greater_than_secund([5,2,3,2,1,4]))
# print(values_greater_than_secund([3]))


# size = 5
# value = 2

# this_list = [2,2,2,2,2]


#!  5)This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
#                               The function should create and return a list whose length is equal to the given size, 
#                               and whose values are all the given value.
#                                Example: length_and_value(4,7) should return [7,7,7,7]
#                                Example: length_and_value(6,2) should return [2,2,2,2,2,2]


def lenght_and_value(size, value):
    this_list = []
    for i in range(0, size):
        this_list.append(value)
    
    return this_list


# print(lenght_and_value(4,7))
print(lenght_and_value(6,8))
print(lenght_and_value(4,0))