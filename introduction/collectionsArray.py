numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[1])

numbers += [1000, 2000]
print(numbers)

numbers.append('Gustavo')
print(numbers)

numbers[0:3] = [123]
print(numbers)

numbers[3:6] = []
print(numbers)

print(len(numbers), "\n")

listPeoples1 = ['Gustavo', 'Pedro', 'Jose']
listPeoples2 = ['Marcos', 'Tiago', 'João']
listPeoplesConcat = listPeoples1 + listPeoples2
listPeoplesMulti = listPeoples1 * 2
print(listPeoples1,"\n",
      listPeoples2,"\n",
      listPeoplesConcat,"\n",
      listPeoplesMulti,"\n")