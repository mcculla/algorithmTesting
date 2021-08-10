def mergeSort(arr):

    if len(arr) > 1:
        midpoint = len(arr)//2
        L = arr[:midpoint]
        R = arr[midpoint:]

        mergeSort(L)
        mergeSort(R)

        indL = indR = ind = 0

        while indL < len(L) and indR < len(R):
            if L[indL] < R[indR]:
                arr[ind] = L[indL]
                indL+=1
            else:
                arr[ind] = R[indR]
                indR+=1
            ind+=1

        while indL < len(L):
            arr[ind] = L[indL]
            indL+=1
            ind+=1

        while indR < len(R):
            arr[ind] = R[indR]
            indR+=1
            ind+=1



def printArray(arr):

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()



if __name__ == '__main__':

    arr = list(map(int, input("Enter numbers separated by a space: ").split()))
    print("Initial array: ", end="\n")
    printArray(arr)
    mergeSort(arr)
    print("mergeSort Result: ", end="\n")
    printArray(arr)