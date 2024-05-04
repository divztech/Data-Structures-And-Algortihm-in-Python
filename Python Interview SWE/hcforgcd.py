def hcforgcd(num1, num2):
    hcf = 1
    for i in range(1,min(num1,num2)):
        if num1%i == 0 and num2%i == 0:
            hcf = i
    return hcf

if __name__ == "__main__":
    a,b = 36,60
    hcf = hcforgcd(a,b)
    print(f"Highest common factor or greatest common divisor for {a} and {b} is {hcf}")