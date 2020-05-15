a=int(input())
li=list()
i=input().split()
for j in i:
    li.append(int(j))

print (hash(tuple(li)))
