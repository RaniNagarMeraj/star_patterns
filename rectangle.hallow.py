n=4
c=8


for i in range(n):
    for j in range(c):
        if i==0 or i==n-1 or j==0 or j==c-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   

