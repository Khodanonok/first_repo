a = int(input("Lenght of segment 1: "))
b = int(input("Lenght of segment 2: "))
c = int(input("Lenght of segment 3: "))      # Defined our segments

def is_triangle(a,b,c):
  if a > 0 and b > 0 and c > 0:                      #values should be >0
    if a + b > c and b + c > a and a + c > b:        #sum of 2 segments always bigger then 3rd segment
      return True
  return False                                              

res = is_triangle(a,b,c)                                    
print(res)                                           # Displays result on the screen