
sum = 0
i = 2
while(i <= 20):
    c=1
    k=int((i/2)+1)
    for j in range(1,k):
        if(i%j==0):
            c=c+1

    if(c == 2):
        sum = sum + i
    i=i+1
print(sum)


