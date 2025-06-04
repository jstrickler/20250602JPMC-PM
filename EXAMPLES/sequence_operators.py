colors = ["red", "blue", "green", "yellow", "brown", "black"]

# Test for membership in list
print("yellow in colors: ", ("yellow" in colors))
print("pink in colors: ", ("pink" in colors))

# Concatenate iterable of strings using ", " as delimiter
sep = ", "
print("colors: ", sep.join(colors))  

del colors[4]  # remove brown

print("removed 'brown':", sep.join(colors))

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(f"{list_c = }")

print('-' * 60)
print(f"{[False] * 10 = }")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

total = sum(nums)
print(f"{total = }")

print(f"{nums = }")
rev_nums = reversed(nums)
print(f"{rev_nums = }")
for num in rev_nums:
    print(num, end=",")
print()