'''https://www.programiz.com/python-programming/recursion
Python Recursive Function(পুনরাবৃত্তিমূলকভাবে)
In Python, we know that a function can call other functions


'''

def a (paramenet):
    if paramenet == 1:
        return 1
    else:
        return (paramenet * a(paramenet-1))

    pae = 3
    print("then number is ",paramenet, "is", a(pae))

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))