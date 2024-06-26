a=["abc","car","ada","racecar","cool"]
flag=0
for i in range(len(a)):
    b=a[i]
    c=b[::-1]
    if b==c:
        flag=1
        break
print(a[i])
