num1, num2 = map(int, input().split())
for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("HCF of", num1, "and", num2, "is", hcf)
lcm=(num1*num2)//hcf
print("lcm",lcm)
