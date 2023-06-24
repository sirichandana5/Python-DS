sum=0
for i in range(0,41,2):
    if(i==10):
        continue
    else:
        print(i,end=" ")
        sum=sum+i
print("sum=",sum)
