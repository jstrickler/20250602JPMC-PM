import sys
import alpha.mathlib.geometry as geometry   # find and load geometry.py

# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in <INSTALLATION-DIR>/lib/

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

print(f"{geometry.PI = }")

print(f"{sys.prefix = }")
print(f"{sys.executable = }")
for folder in sys.path:
    print(folder)