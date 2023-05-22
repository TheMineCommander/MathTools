import math
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
try:
  x1 = (-1*b - math.sqrt((b*b)-(4*a*c)))/(2*a)
  x2 = (-1*b + math.sqrt((b*b)-(4*a*c)))/(2*a)
  if x1 < 0:
    if x2 < 0: print(f"{a}(x+{x1*-1})(x+{x2*-1})\n")
    else: print(f"{a}(x+{x1*-1})(x-{x2})\n")
  elif x2 < 0: print(f"{a}(x-{x1})(x+{x2*-1})\n")
  else: print(f"{a}(x-{x1})(x-{x2})\n")
  if x1 == x2: print(f"The solution to the graph is {x1}.")
  else: print(f"The solutions to the graph are {x1} and {x2}")
except ValueError: print("The graph cannot be factored due to there being no point where x=0.")
input()
