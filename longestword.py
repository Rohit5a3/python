st=list(map(str,input().split()))
print(st)
max_len=0
for i in st:
  l=len(i)
  if max_len<l:
    max_len=l
print(max_len)
t=max(st,key=len)
print(t)
