num1 = [4,3,2,3,1]
num2 = [2,2,5,2,3,6]
c1=0
c2=0
for i in num1:
    if i in num2:
        c1=c1+1
for i in num2:
    if i in num1:
        c2=c2+1
print("[",c1,",",c2,"]")
