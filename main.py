y = int(input("y = "))
k = 0
m=0
for i in range (1,y+1):
    t = int(input(f"temperature in {i} day: "))
    if t>0:
        k+=1
    else:
        if k>m:
            m=k 
            k = 0
        else: 
            k = 0

if k>m:
    print(k)
else: 
    print(m)


'''
y = int(input("please input number y :"))

r1=0
r2=1
n=2
while r2<y:
    t = r1
    r1 = r2
    r2 = t + r1
    n+=1
if r2==y:
    print(n)
else:
    print(-1)


'''
'''
y = int(input("введите число: "))


r = 1

for i in range (1, y+1): 
    r = i*r


print(r)


'''
'''
else: 
    if (y//100 == y/100): 
        print ("NO")
    else: 
        if (y//4 == y/4):
            print("YES")
        else: print ("NO")
n = 354813

if (n//100000+n%100000//10000+n%10000//1000==n%1000//100+n%100//10+n%10):
    print('yes')
else:
    print('no')
'''