address = "221B Baker Street, London"
postcode = "NW1 6XE"
full_address = address + ", " + postcode
print(full_address.lower())

my_address = f"{address}, {postcode}" #f-string

print(my_address.upper())
print(postcode.replace(" ", ""))

random_string = "Bonaventure"

sub_string = random_string[::2]

print(random_string[0])
