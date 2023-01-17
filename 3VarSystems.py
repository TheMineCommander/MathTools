from sympy import Matrix
from os import system

oo = float(input("eq1:x>"))
ot = float(input("eq1:y>"))
oh = float(input("eq1:z>"))
of = float(input("eq1:c>"))
to = float(input("eq2:x>"))
tt = float(input("eq2:y>"))
th = float(input("eq3:z>"))
tf = float(input("eq3:c>"))
ho = float(input("eq3:x>"))
ht = float(input("eq3:y>"))
hh = float(input("eq3:z>"))
hf = float(input("eq3:c>"))
m = Matrix([[oo, ot, oh, of], [to, tt, th, tf], [ho, ht, hh, hf]])
system('clear')
mm = (m.rref())
print("Your matrix in reduced row eschelon form is:\n" + str(mm))
