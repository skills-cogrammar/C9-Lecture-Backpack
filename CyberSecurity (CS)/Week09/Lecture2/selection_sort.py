"""
for i = 0 to length[list] do
   min index = i
   for j = i + 1 to length[list] do
      if list[j] < list[min index] then
         min index = j
   swap list[min index] with list[i]
"""
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


data = [4,3,5,2,1]
selection_sort(data)
print(data)