amount = float(input("Enter initial amount: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

for year in range(1, years + 1):
    amount = amount + (amount * rate / 100)
    print("Year", year, ":", round(amount, 2))
