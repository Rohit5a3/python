num = int(input("Enter a number:"))
flag = 0
for i in range(2,num+1):
    if num%i==0:
        flag=1
        break
if flag==1:
 print("not prime")
else:
 print("prime")

