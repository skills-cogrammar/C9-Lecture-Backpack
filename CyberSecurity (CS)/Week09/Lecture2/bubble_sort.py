
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
           if data[j] > data[j+1]:
               data[j], data[j+1] = data[j+1], data[j]

data = [3,4,6,3,4,5]
bubble_sort(data)
print(data)