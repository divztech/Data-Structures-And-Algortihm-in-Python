def rotatebyk(arr, n,k):
    for i in range (0,k):
        temp = arr[n-1]
        for j in range(n-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] = temp
    print(arr)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    k = 4
    rotatebyk(arr, n,k)

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5} K=3
# Output: {3,4,5,1,2}
# Explanation: Rotate the array to right by 2 elements.

# Example 2:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} K=4
# Output: {4,5,6,7,1,2,3}
# Explanation: Rotate the array to right by 3 elements.