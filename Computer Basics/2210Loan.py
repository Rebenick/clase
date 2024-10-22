p = 250000
annual_rate = 5 / 100
years = 30
r = annual_rate / 12
n = years * 12

M = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

print(f"The monthly payment for the loan is: {M:}€")