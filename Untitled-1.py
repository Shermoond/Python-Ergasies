x=0
x=input()
ix=int(x)
digits=[]
while ix>99:
    ix=(ix*3)+1
    k=len(str(ix))
    y=ix
    for i in range(0,k):
        digits.append(y%10)
        y=y//10
    s=0
    for i in digits:
        s=s+i
    ix=s
print(ix)
