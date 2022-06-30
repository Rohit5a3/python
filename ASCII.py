#ASCII Value of the Word
str=input("enter:")
for i in range(0,len(str)):
    print(str[i],"=",ord(str[i]))
 #ACSII OF ITS REVERSE
rev=str[::-1]
print(rev)
for j in range(0,len(rev)):
    print(rev[j],"=",ord(rev[j]))
