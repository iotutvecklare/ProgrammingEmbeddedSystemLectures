import pprint
import numpy
import math

def remove_duplicates_pprint():
    pass

def remove_duplicate_dict(mylist):
    mylist = list(dict.fromkeys(mylist))
    pprint.pprint(mylist)

def remove_duplicate_set(mylist):
    mylist = list(set(mylist))
    pprint.pprint(mylist)

def calculate_product_numpy(numbers):
    return numpy.prod(numbers)

def calculate_product_math(numbers):
    return math.prod(numbers)

def divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False
def even_add_number(num):
    if (num % 2) == 0:
        print("The number is even")
        return True

    else:
        print("The provided number is odd")
        return False

def prime_number():
    pass

def get_winner(dictionary):
    max_value = max(dictionary.values())
    max_keys = [k for k, v in dictionary.items() if v == max_value]  # getting all keys containing the `maximum`
    print(max_keys, max_value)
    # print(f"{max_keys}: {max_value}")

def recursive_seconds_countdown(time_in_seconds):
    if time_in_seconds == 0:
        print("Blast Off")
    else:
        print(time_in_seconds)
        recursive_seconds_countdown(time_in_seconds - 1)


if __name__ == '__main__':
    list_of_ints = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8]
    remove_duplicate_dict(list_of_ints)
    remove_duplicate_set(list_of_ints)
    product_numpy = calculate_product_numpy(list_of_ints)
    product_math = calculate_product_math(list_of_ints)

    pprint.pprint(product_numpy)
    pprint.pprint(product_math)

    print(divisible(9, 2))

    even_add_number(9)

    dic = {"Simon": 13, "Patryk": 20, "April": 30}
    get_winner(dic)

    recursive_seconds_countdown(5)
