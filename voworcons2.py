c=input("enter ....")
def isLowercaseVowel(c):
    return c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
def isUppercaseVowel(c):
    return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
if not c.isalpha():
    print("not alphabet")
elif isLowercaseVowel(c) or isUppercaseVowel(c):
    print("it is a vowel")
else:
    print("it is consonant")
