lst=[50,60,20,30]
lst=sorted(lst)
limit=100
a=[]
for i in range(0,len(lst)):
    a.append(lst[i])
    limit=limit-lst[i]
    if limit<1:
      break
print(a) 
