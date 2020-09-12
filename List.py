<<<<<<< HEAD
#list: append, insert, extend, .sort(),sorted, 
#      min, max, sum, index, in

#list
courses =['hisory','maths','physics','compsci'] 
print(courses)
print(len(courses))

#selecting an element in list
print(courses[3])
print(courses[-2])

#selecting in a range
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# to insert items in list
courses.append('Art')
print(courses)

#to insert item at a particular index
courses.insert(3,"law")
print(courses)

#to add multiple values (extend)
cour=['edu','books']
courses.append(cour)
#it will insert again another list inside list
#it will become nested list
print(courses)

#same like append it will make nested list
courses.insert(0,cour)
print(courses)

#correct way to insert list inside a list
courses.extend(cour)
print(courses)

#to remove items
courses.remove('maths')
print(courses)

#remove last element
courses.pop()
print(courses)


# to reverse the list
courses.reverse()
print(courses)

num = [10,24,43,2,7]

#to sort the list
num.sort()
print(courses)

num.sort(reverse=True)
print(courses)

print(sorted(num))

#to get a minimum value
print(min(num))

#to get a maximum value
print(max(num))

#to get the sum of list
print(sum(num))


#to find the index
courses =['hisory','maths','physics','compsci'] 
print(courses.index('maths'))

#to check the va,ue
print('Art' in courses)

print('maths' in courses)

#using loop
for i in courses:
	print(i,sep=",")

for index,course in enumerate(courses,start=1):
	print(index,course,sep="=",)

#Using Join	
course_str = ', '.join(courses)
print(course_str)

#using split
new_l=course_str.split(',')
print(new_l)


# creating empty list 
l = []
=======
#list: append, insert, extend, .sort(),sorted, 
#      min, max, sum, index, in

#list
courses =['hisory','maths','physics','compsci'] 
print(courses)
print(len(courses))

#selecting an element in list
print(courses[3])
print(courses[-2])

#selecting in a range
print(courses[0:2])
print(courses[:2])
print(courses[2:])

# to insert items in list
courses.append('Art')
print(courses)

#to insert item at a particular index
courses.insert(3,"law")
print(courses)

#to add multiple values (extend)
cour=['edu','books']
courses.append(cour)
#it will insert again another list inside list
#it will become nested list
print(courses)

#same like append it will make nested list
courses.insert(0,cour)
print(courses)

#correct way to insert list inside a list
courses.extend(cour)
print(courses)

#to remove items
courses.remove('maths')
print(courses)

#remove last element
courses.pop()
print(courses)


# to reverse the list
courses.reverse()
print(courses)

num = [10,24,43,2,7]

#to sort the list
num.sort()
print(courses)

num.sort(reverse=True)
print(courses)

print(sorted(num))

#to get a minimum value
print(min(num))

#to get a maximum value
print(max(num))

#to get the sum of list
print(sum(num))


#to find the index
courses =['hisory','maths','physics','compsci'] 
print(courses.index('maths'))

#to check the va,ue
print('Art' in courses)

print('maths' in courses)

#using loop
for i in courses:
	print(i,sep=",")

for index,course in enumerate(courses,start=1):
	print(index,course,sep="=",)

#Using Join	
course_str = ', '.join(courses)
print(course_str)

#using split
new_l=course_str.split(',')
print(new_l)


# creating empty list 
l = []
>>>>>>> fd236f1... Basics of List,Tuple,Set
el= list()