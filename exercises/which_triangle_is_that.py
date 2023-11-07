a = int(input("Lenght of segment 1: "))
b = int(input("Lenght of segment 2: "))
c = int(input("Lenght of segment 3: "))      # Defined our segments

def is_triangle(a,b,c):
  if a > 0 and b > 0 and c > 0:                      #values should be >0
    if a + b > c and b + c > a and a + c > b:        #sum of 2 segments always bigger then 3rd segment
      return True
  return False                                              

res1 = is_triangle(a,b,c)
if res1 is True:
  print("It's a triangle. Let's find out it's type:") # Determined whether it can be a triangle

def which_type(a,b,c):                                  # A little func. to determine the type
  if a == b == c:
    return "Equilateral triangle"
  elif a != b != c:
    return "Scalene triangle"
  elif a == b !=c or a == c != b or b == c != a:
    return "Isosceles triangle"
  
res2 = which_type(a,b,c)                                 
print(res2)