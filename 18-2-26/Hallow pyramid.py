n=4
for i in range(1,n+1):
    for j in range(1,2*n):
        if  i==4 or j==n-i+1 or j==n+i-1 :
            print("*",end=' ')
        else:
       
            
             print(" ",end=" ")
    print()
    
    