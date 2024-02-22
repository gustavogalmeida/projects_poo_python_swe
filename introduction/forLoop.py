names = ['Gustavo', 'Pedro', 'Jose']

for name in names:
    print(name)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Range form 1: range(stop)
# Range form 2: range(start, stop)
# Range form 2: range(start, stop, step)
for numbers in range(1, 10, 2):
    print(numbers)

phrase = 'Hello world'
length = 0

for char in phrase:
    length += 1

print(length)