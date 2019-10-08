mountains = {
    "Mount Everest": 8848,
    "K2": 8611,
    "Kangchenjunga": 8586,
    "Lhotse": 8516,
    "Makalu": 8485,
}

print("Mountain names:")
for name in mountains.keys():
    print(f"\t{name}")
print()

print("Mountain heights:")
for height in mountains.values():
    print(f"\t{height}")
print()

print("Mountain descriptions:")
for name, height in mountains.items():
    print(f"\t{name} is {height} meters high")
print()

print("Mountain descriptions sorted alphabetically:")
for name, height in sorted(mountains.items()):
    print(f"\t{name} is {height} meters high")
print()
