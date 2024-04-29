def IncDec(arr, n):
    k = int(n/2)

    arr = sorted(arr)
    arr[:k] = sorted(arr[:k])
    arr[k:] = sorted(arr[k:],reverse=True)
    print(arr)


if __name__ == "__main__":
    arr = [8,7,1,6,5,9]
    n = len(arr)
    IncDec(arr, n)

#     Example 1:
# Input: 8 7 1 6 5 9
# Output: 1 5 6 9 8 7
# Explanation: First three elements are in the ascending order and next three elements are in the descending order.

# Example 2:
# Input: 4 2 8 6 15 5 9 20
# Output: 2 4 5 6 20 15 9 8