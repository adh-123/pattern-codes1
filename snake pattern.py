n=4
for i in range(n):
    for j in range(n):
        if i%2==0:
            num=i*n+j+1
        else:
            num=(i+1)*n-j
        print(num,end=" ")
    print()
 
 