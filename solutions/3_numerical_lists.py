# multiples of ten
tens = [i * 10 for i in range(1, 11)]
print("Multiples of ten:", tens)

# but also
tens = list(range(10, 101, 10))
print("Multiples of ten v2:", tens)

# working backwards
plus_thirteen = []

for number in range(1, 11):
    plus_thirteen.append(number + 13)

print("Working backwards:", plus_thirteen)
