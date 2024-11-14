"""
for each item in the list
    if match item == value
        return the item's location
    end if
end for
"""
def linear_search(data, target):
    for value in data:
        print(value)
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

print(linear_search([5,7,7,6,45,4,3,2], 7))