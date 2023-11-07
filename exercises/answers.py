instructions = input("Ho-ho-ho! Where the fuck am i supposed to go? ") 

def path(instructions):
  floor = 0                                    # The floor setted as 0
  for i in instructions:                       # For loop is created to iterate through each item
    if i == ")":
      floor += 1                               # ")" is adding 1 to result
    elif i == "(":
      floor -= 1                               # opposite shit
    else:
     print("Only ') or '(' is allowed, hoe-hoe-hoe!")  # Shows that incorrect item is printed
  return(floor)                                        # returning our result

res = path(instructions)                          
print(res)                                             # Displays result on the screen