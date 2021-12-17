import collections;

inp = int(input())
coll = collections.OrderedDict()

for i in range(inp):
    word = input()
    if word in coll:
        coll[word] +=1
    else:
        coll[word] = 1

print(len(coll));

for k,j in coll.items():
    print(j,end = " ");