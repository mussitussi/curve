## Data fra et eksempel i "Options, Futures And Other Derivative", J. C. Hull [1]

# table 4.3 [1]
data = {
    "bond_principal": [100.0, 100.0, 100.0, 100.0, 100.0],
    "time_to_maturity": [0.25, 0.50, 1.00, 1.50, 2.00],
    "annual_coupon": [0, 0, 0, 8, 12],
    "bond_price": [97.5, 94.9, 90.0, 96.0, 101.6],
    #"bond_price": [99.5, 94.9, 90.0, 96.0, 101.6],
}

# table 4.4 [1]
result = {
    "time_to_maturity": [0.25, 0.50, 1.00, 1.50, 2.00],
    "zero_rate": [10.127, 10.469, 10.536, 10.681, 10.808],
}

# cashflow matrix generated from table 4.3
cf = [
    [100, 0, 0, 0, 0],
    [0, 100, 0, 0, 0],
    [0, 0, 100, 0, 0],
    [0, 4, 4, 104, 0],
    [0, 6, 6, 6, 106],
]
