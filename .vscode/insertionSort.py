def insertionSort(list):

    for sortIndex in range(2, len(list)):
        keyValue = list[sortIndex]
        compareIndex = sortIndex - 1

        while compareIndex > 0 and list[compareIndex] > keyValue
            list[compareIndex + 1] = list[compareIndex]
            compareIndex = compareIndex - 1
        
        list[compareIndex + 1] = key