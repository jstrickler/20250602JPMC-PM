numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
    except Exception as err:
        print(f"{err}: x = {x} y = {y}")
        exit()
    else:
        total += quotient  # Only if no exceptions were raised
    finally:
        print("Can't stop me!")
print(total)
