def checkBinary(number):
    string_format = str(number)
    is_it_binary = True
    statement =""
    for i in range(0,len(string_format)):
        if string_format[i] == "0" or string_format[i] == "1":
           is_it_binary = True
           print(string_format[i])
        else:
            is_it_binary = False

    if is_it_binary == False:
        statement = "Not a binary number"
    else:
        statement = "Yeah its a binary number"
    
    return statement
    

if __name__ == "__main__":
    number = 11010101224
    bin = checkBinary(number)
    print(bin)