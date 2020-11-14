a = [int(s) for s in input().split()]
# 1 2 2 3 3 3 
count=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            count +=1
print(count)            
