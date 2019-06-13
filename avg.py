a5=input()
b5=list(map(int,input().split()))
sum=0
avg=0
for i in b5:
          sum=sum+i
avg=sum//len(b5)
print(avg)
