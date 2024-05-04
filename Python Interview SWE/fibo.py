#fibo series 0 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    f_list = [0,1]
    for i in range(2,n):
        f_list.append(f_list[-1]+f_list[-2])

    return f_list


if __name__ ==  "__main__":

    n = 20
    fibonacci_series = fibonacci(n)
    print(fibonacci_series)