guestList = ['Gustavo', 'Pedro', 'Tiago', 'João']

name = 'Gustavo'
age = 17

if name in guestList and age >= 18:
    print('Entry accepted')
else:
    print('Entry refused')

age = 17
message = "You are of legal age" if age >= 18 else "You are not of legal age"
print(message)

if len(guestList) < 5:
    print("Number of participants less than allowed")
