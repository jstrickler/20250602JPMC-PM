fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

# [VALUE for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if len(f) > 8]
print(f"{f3 = }\n")

fruit_gen = (f.upper() for f in fruits)
print(f"{fruit_gen = }")
for fruit in fruit_gen:
    print(fruit)

# LIST COMPREHENSION:  [VALUE for VAR in ITERABLE if CONDITION]
# GENERATOR EXPRESSION:  (VALUE for VAR in ITERABLE if CONDITION)

