#nested loops
n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n):
        print(row,end=' ')
        print()





n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()




n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()




n=int(input("enter the sizes: "))

for row in range(n):
    for spc in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()




n=int(input("enter the sizes: "))

for row in range(n):
    for spc in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()





n=int(input("enter the sizes: "))

for row in range(n):
    if row<=n//2:
        for col in range(row+1):
            print('*',end=' ')
    else:
        for col2 in range(n-row):
            print('*',end=' ')
    print()





n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()        




n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()     







n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()    




n=int(input("enter the sizes: "))

for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==n-row-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()     


















