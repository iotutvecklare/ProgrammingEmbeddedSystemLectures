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

if __name__ == '__main__':
    # print(first_fibonacci(3))
    max_value = 4000000
    print("The sum of the even-valued terms is:", sum_of_even_valued_terms(max_value))