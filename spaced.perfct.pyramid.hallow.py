n=int(input())
for i in range(1,n+1):
    if i==1 or i==n:
        print(" "*(n-i)+"* "*i)
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")


#reverse
# n=int(input())                                        
# for i in range(n,0,-1):
#     if i==1 or i==n:
#         print(" "*(n-i)+"* "*i)
#     else:
#         print(" "*(n-i)+"*"+" "*(2*i-3)+"*")

''''
                    * * * * * *
                     *       *
                      *     *
                       *   *
                        * *
                         *              '''