moves=34
winningpoint=int(input("enter the winning point: "))

while moves>0:
    if moves==winningpoint:
        print("congratulations!!!you won the game")
        break
    print(f"{moves} are left. you have chance to win the game")
    moves-=1
else:
    print("game over.try again")









l=(1,2,3,4,5)
ind=0
while ind<len(l):
    print(l[ind])
    ind+=1




#5 4 3 2 1
n=5
while n>0:
    print(n)
    n=n-1 



 
while n<19:
    print(n)
    n=n+3





1**2
2**2
3**2
4**2
5**2
6**2
n=1
while n<7:
    print(n**2)
    n+=1



l=list(map(int,input().split()))
s=0
ind=0
while ind<len(l):
    s=s+l[ind]
    ind+=1
    print(s)



n=int(input())
s=0
while n>0:
    s+=(n%10)
    n=n//10
    print(s)




n=input()
full=len(n)-1
length=len(n)//2
ind=0

while ind <=length:
    if n[ind]!=n[full]:
        print("not a palindrome")
        breakind+=1
        full-=1
    else:
        print('palindrome')
        
















