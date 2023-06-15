"""
Argument is money value.
Returns the tax on that value as a float.

Data:
https://www.ato.gov.au/Rates/Individual-income-tax-rates/
"""

def TaxFunction(num):
    if num <= 18200:
        return 0
    elif num <= 45000:
        return (19/100)*(num - 18200)
    elif num <= 120000:
        return 5092 + (32.5/100)*(num - 45000)
    elif num <= 180000:
        return 29467 + (37/100)*(num - 120000)
    else:
        return 51667 + (45/100)*(num - 180000)