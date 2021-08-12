def maxCrossingSum(arr, low, mid, high):

    currSum = 0
    leftSum = -10000

    for i in range(mid, low-1, -1):
        currSum = currSum + arr[i]

        if(currSum > leftSum):
            leftSum = currSum

    currSum = 0
    rightSum = -10000

    for i in range(mid+1, high+1):
        currSum = currSum + arr[i]

        if(currSum > rightSum):
            rightSum = currSum

    return max(leftSum + rightSum, leftSum, rightSum)



def maxSubarraySum(arr, low, high):

    if(low == high):
        return arr[low]

    mid = (low + high) // 2

    return max(maxSubarraySum(arr, low, mid), maxSubarraySum(arr, mid+1, high), maxCrossingSum(arr, low, mid, high))



if __name__ == '__main__':

    arr = list(map(int, input("Enter numbers separated by a space: ").split()))
    print("Initial array: ", end="\n")

    n = len(arr)
    totSum = maxSubarraySum(arr, 0, n-1)

    print("Maximum contiguous sum: ", totSum)