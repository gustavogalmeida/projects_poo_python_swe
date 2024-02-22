iterator = 1
list = []
while iterator < 100:
    list.append(iterator)
    iterator += 1

print(list)

stackOfBooks = ['Portuguese', 'Math', 'History', 'Geograph', 'Chemical']
print(stackOfBooks)

while True:
    book = stackOfBooks.pop()
    print(book)
    if book == 'Math':
        break

print('Rest of the stack of books', stackOfBooks)