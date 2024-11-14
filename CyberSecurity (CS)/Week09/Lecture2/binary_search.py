"""
binarySearch(array, size)
    loop until start is not equal to finish
        midIndex = (start + finish)/2
        if (element == array[midIndex] )
            return midIndex
        else if (element > array[midIndex] )
            start = midIndex + 1
        else
            finish = midIndex - 1
"""
def binary_search(data, target):
    left, right = 0, len(data)-1
    while left <= right:
        mid = (left + right)//2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10,11], 5))
