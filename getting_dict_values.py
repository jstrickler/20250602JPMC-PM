airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['MCO'] = }")
print(f"{'MCO' in airports = }")
# print(f"{airports['MIA'] = }")
print(f"{airports.get('MIA') = }")
print(f"{airports.get('MIA', '**NOT FOUND**') = }")
print(f"{airports.get('MCO') = }")

print(f"{airports.setdefault('MIA', 'Miami') = }")
print(f"{airports = }")

# DICT.items() -- view of dictionary pairs

for code, city in airports.items():
    print(code, city.upper())
print()
print(f"{airports.items() = }")
