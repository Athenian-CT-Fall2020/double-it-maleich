# Collaborators: A period!

def double_it(x):
    x = int(x)
    product =  x * 2
    return product


if __name__ == '__main__':
    # print(double_it(5))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    v = input("Value to double: ")
    print(double_it(v))
