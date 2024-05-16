number_hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))

if number_hours > 40:
    pay = 40 * rate + (number_hours - 40) * rate * 1.5
else:
    pay = number_hours * rate

print(pay)
