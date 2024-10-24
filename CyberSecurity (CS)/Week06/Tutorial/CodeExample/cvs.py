import csv

data = [
    {
        'Name' : 'Alice',
        'Age' : 30,
        'City' : 'New York'
    },
    {
        'Name' : 'John',
        'Age' : 30,
        'City' : 'London'
    }
]

with open('output.csv', 'w', newline='') as file:
    fieldNames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(data)


with open('output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
