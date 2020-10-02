

a=[]
i=1
while i<=1000:    
    if(i%3==0 or i%5==0):        
        a.append(i)
    i+=1

sum(a)

c=0
i=1
while i<=1000:    
    if(i%3==0 or i%5==0):        
        c+=i
    i+=1
c

d=[1,2]
e=2
i=1
while i<=4000000:    
    d.append(d[-1]+d[-2])
    if(d[-1]%2==0):        
        e+=d[-1]
    i=d[-1]
e

f=1
i=1
while i<13195: 
    if(13195%i==0 and i%2!=0):        
        f=i
    i+=1
f

primeFactor = 1
i = 2
n=13195  
while i <= n / i:  
    print(n)  
    if n % i == 0:
        primeFactor = i         
        n /= i
    else:
        i += 1

if primeFactor < n: primeFactor = int(n)
primeFactor
e=13
while e!=1:
    print(e)
    if(e%2==0):
        e=e/2
    else:
        e=3*e+1


f=1
g=1
while f<=1000:
    g*=2
    f+=1
i=0
h=0
while i < len(str(g)):    
    h+=int(str(g)[i])
    i+=1

h

d=[2]
i=2
k=1
while i!=0:
    if(i%2!=0): 
        isprime = True
        for j in d:
            if(i%j==0):
                isprime = False
        if(isprime):
            d.append(i) 
            k+=1           
    if(k==100):
        k=i
        break
    i+=1
k