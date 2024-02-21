val_one = 1
val_two = 2
val_three = 3

print((val_two > val_one) and (val_three < 5)) # T T = True
print((val_two > val_one) and (val_one>3)) # T F = False

print((val_three < 5) or (val_two>1)) # T T = True
print((0 > val_one) or (0 == -1)) # F F = False
print((0 < val_one) or (0 == -1)) # T F = True