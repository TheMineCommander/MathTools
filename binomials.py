import math
import os
from colorama import Fore, Style
from time import sleep

def clear():
  os.system('clear')

def square():
  print(f"({Fore.RED}a{Style.RESET_ALL}x + {Fore.BLUE}b{Style.RESET_ALL})²")
  ai = float(input(f"Enter the value for {Fore.RED}a{Style.RESET_ALL}: "))
  bi = float(input(f"Enter the value for {Fore.BLUE}b{Style.RESET_ALL}: "))
  if ai == 0:
    if input("Are you sure you meant to enter 0 and not 1? (y/n)\n>").lower() != "y":
      ai = 1.0
  a = ai*ai
  b = 2*ai*bi
  c = bi*bi
  print(f"{Fore.LIGHTBLACK_EX}({ai}x + {bi})² = ",end=f"{Style.RESET_ALL}")
  return f"{Fore.LIGHTGREEN_EX}{a}x²+{b}x+{c}{Style.RESET_ALL}"

def unsquare():
  print(f"{Fore.RED}a{Style.RESET_ALL}x²+{Fore.GREEN}b{Style.RESET_ALL}x+{Fore.BLUE}c{Style.RESET_ALL}")
  ai = float(input(f"Enter the value for {Fore.RED}a{Style.RESET_ALL}: "))
  bi = float(input(f"Enter the value for {Fore.GREEN}b{Style.RESET_ALL}: "))
  ci = float(input(f"Enter the value for {Fore.BLUE}c{Style.RESET_ALL}: "))
  a = math.sqrt(ai)
  b = math.sqrt(ci)
  if bi < 0:
    b *= -1
  print(f"{Fore.LIGHTBLACK_EX}{ai}x²+{bi}x+{ci} = {Fore.LIGHTGREEN_EX}({a}x + {b})")
  
choice = input("Would you like to square or un-square? (1 or 2)\n>")
while choice != "1" and choice != "2":
  clear()
  choice = input("Would you like to square or un-square? (1 or 2)\n>")
clear()
if choice == "1":
  print(square())
else:
  unsquare()
