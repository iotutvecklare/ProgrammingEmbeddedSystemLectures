def first_fibonacci(digit_amount):
    f1 = 1
    f2 = 1
    i = 2

    while len(str(f2)) < digit_amount:
        f1, f2 = f2, f1+f2
        i += 1

    return i

if __name__ == '__main__':
    print(first_fibonacci(3))


"""
f1 = 1
f2 = 1

length = 0
index = 2

while length < 3:
    f1, f2 = f2, f1+f2
    index += 1

    length = len(str(f2))

if __name__ == '__main__':
    print(index)
    print(f2)

f1 = 1
f2 = 1

length = 0
index = 2

while length < 3:
    temp = f1
    f1 = f2
    f2 = f2+temp
    index += 1

    length = len(str(f2))

if __name__ == '__main__':
    print(index)
"""
