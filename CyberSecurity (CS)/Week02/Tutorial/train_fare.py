age = int(input("Please enter your age: "))
base_fare = 30
discount = 0.50

if(age > 60):
    fare = base_fare * discount
else:
    print(base_fare)

print(fare)
