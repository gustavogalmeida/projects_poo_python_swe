print("\n")

dictionaryPeople = {"name" : "Gustavo",
                    "age" : 23,
                    "city" : "Patrocínio"}

print(dictionaryPeople)
print(dictionaryPeople["age"])

print("\n")
dictionaryStudents = {1 : "Pedro",
                      2 : "Tiago",
                      3 : "João"}
print(dictionaryStudents)
dictionaryStudents[4] = "Gustavo"
print(dictionaryStudents)

print("\n")
studentPresent = (2 in dictionaryStudents)
print("The student Tiago is present:", studentPresent)

