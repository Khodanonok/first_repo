a = int(input("Lenght of segment 1: "))            
b = int(input("Lenght of segment 2: "))              # input is more convenient, i think
c = None                                             # defined c as none for substitution in formulas

possible_side = []                                   # created a list for substitution of c values

def is_triangle(a,b,c):
  if a > 0 and b > 0 and c > 0:                      # values should be >0
    if a + b > c and b + c > a and a + c > b:        # sum of 2 segments always bigger then 3rd segment
      return True
  return False   

for c in range ((b - a) + 1, a + b):                  # loop in range from minimal to maximal possible value of c
   if c!= (a*a + b*b)**0.5 and is_triangle:           # iterating each value (except hypotenuse)
     possible_side.append(c)                          # add acceptable values to the list

print(possible_side)          