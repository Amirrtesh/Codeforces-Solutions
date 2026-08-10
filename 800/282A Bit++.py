n=int(input())
x=0
for i in range(n):
  s=input()
  if s.lower()=="++x" or s.lower()=="x++":
    x=x+1
  elif s.lower()=="--x" or s.lower()=="x--":
    x=x-1
print(x)
