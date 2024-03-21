from z3 import *
s=Solver()
a1,a2,a3,a4,a5,aa=Ints("a1 a2 a3 a4 a5 aa")
s.add(a2-a3==2225223423)
s.add(a3+a4==4201428739)
s.add(a2-a4==1121399208)
s.add(a5==-2064448480)
s.add(a1==550153460)
s.add(aa==-548868226)
if(s.check()==sat):
    print(s.model())
else:
    print("OOOOOOOOOOOooOOOOOOOOOOOOO")