#Write a program in Python to swap two numbers using the third variable
def swapnum(a,b):
    print(f"Before swapping a: {a} and b: {b}")
    z = 0
    z = a
    a = b
    b = z

    return "Swapped a: " + str(a)+ " and b: " + str(b)


if __name__ == "__main__":

    a, b = 5,7
    print(swapnum(a,b))