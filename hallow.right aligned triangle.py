n=int(input())
for i in range(1,n+1):
    if i==1:
        print(" "*(2*n-2)+"*")
    elif i==n:
        print("* "*n)
    else:

        print(" "*(2*n-i*2)+"*"+" "*(2*i-3)+"*")
'''


        *
      * *
    *   *
  *     *
* * * * * 
                           '''