price = float(input("Enter a price: "))
vat_rate = 0.20
vat_amt = price * vat_rate
print(vat_amt)
total_price = price + vat_amt

print(f"Total price is {total_price}")
