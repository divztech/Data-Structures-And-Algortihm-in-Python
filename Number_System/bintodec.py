from math import pow
def bintodec(num):
    num_str = str(num)
    binary = 0
    num_str = num_str[::-1]
  
    
    for i in range(0,len(num_str)):
        binary += int(num_str[i]) * int(pow(2,i))
        
    print(binary)
   


if __name__ == "__main__":
    #arr = [1,2,3,4,5,6,7]
   
    number = 111
    bintodec(number)


# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.

# Example 2:
# Input: 100
# Output: 4
# Explanation: 100 when converted to decimal number is “4”.




# Example 1:
# Input: N = 1011
# Output: 11
# Explanation: 1011 when converted to decimal number is “11”.

# Example 2:
# Input: 100
# Output: 4
# Explanation: 100 when converted to decimal number is “4”.