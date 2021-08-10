def insertionSort(arr):

    for sortIndex in range(1, len(arr)):
        keyValue = arr[sortIndex]
        compareIndex = sortIndex - 1

        while compareIndex >= 0 and arr[compareIndex] > keyValue:
            arr[compareIndex + 1] = arr[compareIndex]
            compareIndex = compareIndex - 1
        
        arr[compareIndex + 1] = keyValue



def printArray(arr):

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()



if __name__ == '__main__':

    arr = list(map(int, input("Enter numbers separated by a space: ").split()))
    print("Initial array: ", end="\n")
    printArray(arr)
    insertionSort(arr)
    print("Result: ", end="\n")
    printArray(arr)