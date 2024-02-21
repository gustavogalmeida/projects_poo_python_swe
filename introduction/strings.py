# concatenation
str_oo = "Object-oriented"
str_p = "Programing"
str_oop = str_oo + " " + str_p
print(str_oop)

# length
print(len(str_oop))

# indexing and substrings
phrase = "Python is a powerful programming language"

# the indexing start with 0
print(phrase[3])

# negative number starts at the end of the array
print(phrase[-1])

# using ":" i can inform [start:end]
# the "end" is not included
# example [0:6] is equal to [0:6)
print(phrase[0:6])

# multiplicating strings
laughter = "ha"
print(laughter*10)

# in operator
phrase = "Python Programming"
print("Python" in phrase)
print("python" in phrase)
print("lemon" in phrase)

# escaping | break line
print("Hello \nWorld!")

# upper case and lower case convertions
print(phrase)
print(phrase.upper())
print(phrase.lower())
phrase = phrase.lower()
print(phrase.capitalize()) # first latter capitalized

print("\n")

# format
name = "Gustavo"
int_number = 23
float_numer = 3.1415

print("Hello, my name is %s!\nI'm %d years old and $ %d.\n"
      % (name, int_number, float_numer))
# decimal printed as integer %d

print("Hello, my name is %s!\nI'm %d years old and $ %f.\n"
      % (name, int_number, float_numer))
# decimal printed as decimal %f

print("Hello, my name is %s!\nI'm %d years old and $ %.2f.\n"
      % (name, int_number, float_numer))
# decimal printed with two decimal places %.2f
