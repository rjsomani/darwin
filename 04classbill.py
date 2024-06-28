electricity_bills = {
    "January": 1000.25,
    "February": 1200.75,
    "March": 9500.50,
    "April": 1050.00,
    "May": 11000.60,
    "June": 1300.40,
    "July": 12500.30,
    "August": 1350.25,
    "September": 1450.90,
    "October": 14000.55,
    "November": 1500.10,
    "December": 1600.45
}

total_bill = sum(electricity_bills.values())
average_bill = total_bill / len(electricity_bills)

print(f"Total electricity bill for the year: {total_bill:.2f}")
print(f"Average monthly electricity bill: {average_bill:.2f}")
