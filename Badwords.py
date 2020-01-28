def checker(word):
    y  = word
    bad=["f","F","c","C","k","K","r","R"]
    vowels=["a","A","e","E","i","I","o","O","u","U","y","Y"]
    x=[]
    for i in y :
        check=1
        for j in vowels:
            if j==i:
                check=0
        if check==1:
            x.append(i)
    bc=0
    gc=0
    for i in x:
        check = 1
        for j in bad:
            if i==j:
                check=1
                break
            else:
                check=0
        print (check)
        if check==1:
            bc+=1

        else:
            gc+=1
        
    print (bc,gc)
    if bc>=gc:
        res="Bad Word"
    else:
        res="Good Word"
    return (res)
    

doc=open("test.txt","r")
wordlist=doc.read
brokenup=wordlist.split(" ")
for l in wordlist:
    if len(l)>=3:  
        word=l
        result=checker(l)
        print (l,result)
doc.close()



