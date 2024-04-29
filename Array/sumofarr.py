def sumofarr(arr, n):
    sum_of_arr = 0
    for a in arr:
        sum_of_arr += a
    print(sum_of_arr)


if __name__ == "__main__":
    arr = [1,2,1,1,5,1]
    n = len(arr)
    sumofarr(arr, n)

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 15
# Explanation: Sum of all the elements is 1+2+3+4+5 = 15

# Example 2:
# Input:  N=6, array[] = {1,2,1,1,5,1}
# Output: 11
# Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11