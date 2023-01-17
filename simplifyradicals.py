import math
import os

def clear(): #Simple function to clear the screen using the os module. Does not work on Windows, but fine here.
  os.system('clear')
#Welcome the user
print("Welcome! This program will find the simplest form of a radical.")
print("To use it, input the outside variable and the radicand. Tip: If there is no outside variable, use 1.\n\n")
#A visually appealing method of taking the input of the user
outside = int(input("▓√▓\n↑\n"))
if outside == 0: #Make sure the user isn't stupid #1
  exit("Don't use 0.")
clear()
print("Welcome! This program will find the simplest form of a radical.")
print("To use it, input the outside variable and the radicand. Tip: If there is no outside variable, use 1.\n\n")
spaces = (len(str(outside))+1) * " "
radicand = int(input(f"{outside}√▓\n{spaces}↑\n{spaces}"))
if radicand == 1: #Make sure the user isn't stupid #2
  exit("Seriously? sqrt(1) is 1.")
if radicand == 0: #Make sure the user isn't stupid #3
  exit("Seriously? sqrt(0) is 0.")
if radicand < 0: #Make sure the user isn't stupid #4
  exit("You can't take the square root of a negative (and I am not going to implement i.)")
clear()
original = f"{outside}√{radicand}"
print(original)

#This is the main part of the program!
i = 2
print("Working...")
while True: #Repeat forever
  a = radicand/i
  b = math.sqrt(a)
  if math.pow(int(b),2) == a: #If a simplification has been found
    b *= outside
    break #Get out of the loop
  i += 1 #Otherwise, increment i

c = math.sqrt(i)
clear()
if f"{int(b)}√{i}" == original: #Make sure that the original is not the same as the new one
  print("The radical is already in its simplest form.")
elif math.pow(int(c),2) == i: #If the new radicand is a perfect square
  print(int(b*c))
else:
  print(f"{int(b)}√{i}")
