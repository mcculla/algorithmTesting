from insertionSort import *

input = list(map(int, input("Enter numbers separated by a space: ").split()))

print("Numbers to sort: ", input)
print("Initializing insertionSort...")

result = insertionSort(input)

print("Result: ", result)