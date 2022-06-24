num=int(input('enter number:'))
temp=num
rev=0
while num>0:
     rem=num%10
     rev=rev*10+rem
     num=num//10
print("reverse is",rev)
if num==rev:
    print(temp,"is"+" "+"palindrome")
else:
    print(temp,"is"+" "+"not palindrome")





