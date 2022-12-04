# check prime no. or not
"""n=int(input("emter number:"))
c=0
for i in range(2,n):
    if(n%i==0):
        c+=1
        break
if(c==0):
    print("prime")
else:
    print("n.p")"""
#revverse no.
"""n=123
t=n
rev=0
while(n>0):
    l=n%10
    rev=rev*10+l
    n=n//10
if (t==rev):
    print("palindrome",rev)
else:
    print("n.p",rev)"""
l=1
u=20
s=[]
for num in range(l,u+1):
        if(num>1):
            for i in range(2,num):
                if(num%i)==0:
                    break
                else:
                    print(num)
'''n=int(input())
list=[]
sum = 0
for i in range(2,n+1):
    ifi%'''
