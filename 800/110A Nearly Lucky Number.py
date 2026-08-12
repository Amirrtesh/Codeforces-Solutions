n = input()
l= 0
for i in n:
    if i == '4' or i == '7':
        l+= 1
if l== 0:
    print("NO")
elif l == 4 or l== 7:
    print("YES")
else:
    print("NO")
