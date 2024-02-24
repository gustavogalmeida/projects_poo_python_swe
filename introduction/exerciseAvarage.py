# First, we should ask for the person's name and give a welcome message.
# Continue by collecting 3 grades and calculate the average.
# If the average is >= 7, the student is approved.
# If the average is < 3, the student is failed.
# If 3 <= average < 7, the student goes to the final exam.

name = str(input('Please enter your name: '))
print('Wellcome, %s' %name,'!\n')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('      The student %s, was approved?'%name)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

note1 = float(input('Enter your first note: '))
note2 = float(input('Enter your second note: '))
note3 = float(input('Enter your third note: '))

average = (note1 + note2 + note3)/3

if average>7:
    result = 'APPROVED'
elif average<3:
    result = 'DISAPPROVED'
else:
    result = 'FINAL EXAM'

print('Average: ',average)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('      The result was: ', result)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')