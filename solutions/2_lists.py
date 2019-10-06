# working list
careers = ['programmer', 'truck driver', 'astronaut', 'farmer']
print(careers)

print('The index of "astronaut" is:', careers.index('astronaut'))
print('Is "farmer" in the list?', 'farmer' in careers)
print('Is "potato" in the list?', 'potato' in careers)

careers.append('cook')
print(careers)
careers.insert(0, 'scientist')
print(careers)

for job in careers:
    print(job)

# ordered working list
careers = ['programmer', 'truck driver', 'astronaut', 'farmer']     # re-set list to original

print('This is the list in its original order:')
for job in careers:
    print(job)

print('This is the list in alphabetical order:')
for job in sorted(careers):
    print(job)

print('This is the list in its original order:')
for job in careers:
    print(job)

print('This is the list in reverse alphabetical order:')
for job in sorted(careers, reverse=True):
    print(job)

print('This is the list in its original order:')
for job in careers:
    print(job)

print('This is the list in reverse order from what it started:')
for job in reversed(careers):
    print(job)

print('This is the list in its original order:')
for job in careers:
    print(job)

print('This is the list permanently sorted in alphabetical order:')
careers.sort()
for job in careers:
    print(job)

print('This is the list permanently sorted in reverse alphabetical order:')
careers.sort(reverse=True)
for job in careers:
    print(job)
