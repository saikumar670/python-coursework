n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n-row-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()   