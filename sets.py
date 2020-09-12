#Unordered and no duplicates
s1 = {'History','math','Physics'}

print(s1)

s2 = {'History','math','Physics','math'}

print(s2)

print('math' in s2)

s3 = {'History','math','Art','Design'}

print(s1.intersection(s3))
print(s1.difference(s3))
print(s1.union(s3))

es = set()
es1 = {}  # wrong method it will create dictionary