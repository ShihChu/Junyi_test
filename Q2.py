import sys

num  = input("Input: ")
ans = list()

for i in range(1,int(num)+1):
    if i%15 == 0:
        ans.append(i)
    elif i%3 == 0:
        continue
    elif i%5 == 0:
        continue
    else:
        ans.append(i)

print(len(ans))