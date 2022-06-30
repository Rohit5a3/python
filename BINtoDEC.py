num=int(input())
binary_num=num
dec_num=0
base=1
while num>0:
    rem=num%10
    dec_num=dec_num+rem*base
    num=num//10
    base=base*2
print("BINARY NUMBER:",binary_num,"DECIMAL NUMBER:",dec_num)