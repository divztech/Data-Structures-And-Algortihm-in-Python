def rotatebyk(arr, n,k):
    for i in range (0,k):
        temp = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    print(arr)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    k = 2
    rotatebyk(arr, n,k)

# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5} K=3
# Output: 
#After Rotating the k elements to left 3 4 5 6 7 1 2