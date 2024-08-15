#!/usr/bin/python3
# linear search
# searches for a target value within an array by checking each element with the target
def linearSearch(arr: list, target: int) -> int:
    for iteration in range(len(arr)):
        if arr[iteration] == target:
            return iteration 
    return -1

# binary search
# searches for a taget value within a SORTED array by repeatedly dividing the search intival by half
def binarySearch(arr: list, target: int) -> int:
    low: int = 0
    high: int = len(arr) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# bubble sort
# sorts the array by repeatedly going through the list, comparing it with the adjacent elements
# and swapping them if they are in the wrong order
def bubbleSort(arr: list) -> None:
    number: int = len(arr)
    for iteration in range(number):
        print(iteration)
        for j in range(0, number - iteration - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# insertion sort
# builds a sorted array one element at a time by repeatedly taking the next element from the 
# unsorted part and inserting it into its correct position in the sorted part
def insertionSort(arr: list) -> None:
    for i in range(1, len(arr)):
        key: int = arr[i]
        j: int = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# quick sort
# selects a pivot,rearranges the array so all the smaller elements are placed before it and
# all the greater elements are placed after. It recursively applys the process to the sub-arrays
# on either side of the pivot until the entire array is sorted.
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)    

def main() -> None:
    array = [1, 3, 5, 9, 11, 7, 64, 34, 25, 12, 22, 11, 90]
    targetNumber = 7

    print(f"Index of {targetNumber} is {linearSearch(array, targetNumber)} (unsorted)")

    bubbleSort(array)
    print(f"Sorted array: {array} (bubble sort)")

    array = [1, 3, 5, 9, 11, 7, 64, 34, 25, 12, 22, 11, 90]
    insertionSort(array)
    print(f"Sorted array: {array} (insertion sort)")

    array = [1, 3, 5, 9, 11, 7, 64, 34, 25, 12, 22, 11, 90]
    sortedArr = quickSort(array)
    print(f"Sorted array: {sortedArr} (quick sort)")

    print(f"Index of {targetNumber} is {binarySearch(sortedArr, targetNumber)} (sorted)")

if __name__ == "__main__":
    main()
