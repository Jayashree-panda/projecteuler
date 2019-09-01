#even fibonacci series below 4 million
a=0
b=1
sum=0
while True: 
    c=a+b
    if(c%2==0):
        sum=sum+c
    a=b
    b=c
    if(c>4):
        break

print(sum)
 