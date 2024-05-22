import logging
import sys
import argparse

def first_fibonacci(digit_amount):
    f1 = 1
    f2 = 1
    i = 2


    while len(str(f2)) < digit_amount:
        f1, f2 = f2, f1+f2
        i += 1

    return i


# values do not exceed four million
def sum_of_even_valued_terms(max_term_value):
    first_previous_term = 0
    second_previous_term = 1

    sum_of_evens = 0

    logging.error("Before while loop")
    while first_previous_term < max_term_value:

        if first_previous_term % 2 == 0:
            sum_of_evens += first_previous_term

        first_previous_term, second_previous_term = second_previous_term, first_previous_term + second_previous_term

        """
        temp = first_previous_term
        first_previous_term = second_previous_term
        second_previous_term = temp + second_previous_term
        """
    return sum_of_evens

def sys_argv_sum():
    if len(sys.argv) < 2:
        print("Provide at least one number as an argument.")
        sys.exit(1)

    summa = 0
    for arg in sys.argv[1:]:
        try:
            tal = int(arg)
            summa += tal
        except ValueError:
            print(f"'{arg}' is not a valid number.")

    print("The sum is:", summa)


def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines from the file into a list
            line_count = len(lines)  # Get the length of the list to count lines
            print("Number of lines:", line_count)
    except FileNotFoundError:
        print(f"The file '{filename}' could not be found.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

def sys_argv_file_linecount():
    print("Script name:", sys.argv[0])

    """
    The line filename = sys.argv[1] is assigning the value of the second command-line argument (index 1) 
    to the variable filename. sys.argv is a list that contains the command-line arguments 
    passed to the script. sys.argv[0] is the script name itself, and subsequent elements 
    (starting from index 1) are the arguments passed when the script is invoked. So, sys.argv[1] 
    refers to the first argument after the script name, which in this case, is expected to be a file name.
    """

    # Check if there is an argument (file name)
    # if len(sys.argv) != 2:
    #     print("Specify the file name as an argument.")
    #     sys.exit(1)    # Check if there is an argument (file name)

    # Check if a filename is provided as a command-line argument

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        # If no command-line argument is provided, prompt the user for the filename
        print("File name not provided as a command-line argument.")
        filename = input("Please enter the file name: ")

    count_lines_in_file(filename)


def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()  # Read the file and split it into words
            word_count = len(words)      # Count the number of words
            print("Number of words:", word_count)
    except FileNotFoundError:
        print(f"The file '{filename}' could not be found.")
    except Exception as e:
        print("An error occurred:", e)

def argparse_find_max_number():
    pass


if __name__ == '__main__':
    # print(first_fibonacci(3))
    # max_value = 4000000
    # print("The sum of the even-valued terms is:", sum_of_even_valued_terms(max_value))
    # sys_argv_sum()
    # sys_argv_file_linecount()

    parser = argparse.ArgumentParser(description='Count the number of words in a file.')
    parser.add_argument('filename', nargs='?', help='The name of the file to count words in.')

    args = parser.parse_args()

    if args.filename:
        count_words_in_file(args.filename)
    else:
        # If no command-line argument is provided, prompt the user for the filename
        print("File name not provided as a command-line argument.")
        filename = input("Please enter the file name: ")
        count_words_in_file(filename)
