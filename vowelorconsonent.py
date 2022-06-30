str=input("enter the letter:")
if not str.isalpha():
    print("not alphabet")
elif str in ['a','e','i','o','u','A','E','I','O','U']:
    print(str,"is a vowel")
else:
    print(str,"is a consonant")
