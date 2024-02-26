x=[]
while True:
    names=input("enter name:")
    if names=="exit":
        break
    x.append(names)
print(names)
n=len(x)
for i in range(n-1):
    for j in range(n-1-i):
        if len(x[j])>len(x[j+1]):
           x[j],x[j+1]=x[j+1],x[j]
        elif x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)