NPR_TO_USD = 0.009
NPR_TO_EUR = 0.0086
NPR_TO_JPY = 1.6908

def convert_currency(nrs):
    return nrs * NPR_TO_USD, nrs * NPR_TO_EUR, nrs * NPR_TO_JPY

nrs_amount = float(input("Enter amount in Nepali Rupees (NRS): "))

usd, eur, jpy = convert_currency(nrs_amount)
print(f"NRS {nrs_amount} is approximately:")
print(f"USD ${usd:.2f}")
print(f"Euro €{eur:.2f}")
print(f"Japanese Yen ¥{jpy:.2f}")