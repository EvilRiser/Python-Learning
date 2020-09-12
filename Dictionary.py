#var_name = {key:value}
student = {'name':'John', 'Age':25, 'courses':['Math','compsci'],}
print(student)

print(student['name'])

print(student['courses'])

# print(student['phone']) #key doesn't exist
print(student.get('phone'))
print(student.get('phone','not_found'))

student['phone'] = '5555555'
print(student)

student['name'] = 'james'
print(student)

# another way to update
student.update({'name':'jane','Age':26})
print(student)

# delete 

#method1
del student['Age']
print(student)

#method2
name = student.pop('name')
print(student)
print(name)

#to know key and values
print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key in student:
	print(key)

for key,value in student.items():
	print(key,value)