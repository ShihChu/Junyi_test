import sys

num  = input("Input: ")

def Count(n):
    ans = list()
    for i in range(1,int(n)+1):
        if i%15 == 0:
            ans.append(i)
        elif i%3 == 0:
            continue
        elif i%5 == 0:
            continue
        else:
            ans.append(i)
    return len(ans)

print("Ouput: ", Count(num))