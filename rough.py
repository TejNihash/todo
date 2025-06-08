
liss = ("take","a","shit")
item = next(ite for ite in liss if len(ite)==1)
print(item)
item = next(ite for ite in liss)

print(item)

