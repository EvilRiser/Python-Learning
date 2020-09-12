print("hello World")
message = "hello world"
print(message)
print(len(message))
# \ -> escape character
# """ -> multiline character
message = "hello world\'s"
print(message)
print(len(message))
print(message[0:5])

#to lower case

print(message.lower())
print(message.upper())

#to count the no of occurence of that letter or word

print(message.count('l')) # l has occured 3 times
print(message.count('hello')) #hello has occured once

#to find the index
print(message.find('l'))
# if not found then returns -1

#to replace 
message=message.replace('world','universe')
print(message)

#concatenating
g="hello"
name="ss"
msg=g+name
print(msg)
msg=g+" "+name
print(msg)

mess = '{}, {}. Welcome!. '.format(g,name)
print(mess)

#fstrings

mess = f'{g}, {name.upper()}. Welcome!. '.format(g,name)
print(mess)

print(dir(g))


print("hello World")
message = "hello world"
print(message)
print(len(message))
# \ -> escape character
# """ -> multiline character
message = "hello world\'s"
print(message)
print(len(message))
print(message[0:5])

#to lower case

print(message.lower())
print(message.upper())

#to count the no of occurence of that letter or word

print(message.count('l')) # l has occured 3 times
print(message.count('hello')) #hello has occured once

#to find the index
print(message.find('l'))
# if not found then returns -1

#to replace 
message=message.replace('world','universe')
print(message)

#concatenating
g="hello"
name="ss"
msg=g+name
print(msg)
msg=g+" "+name
print(msg)

mess = '{}, {}. Welcome!. '.format(g,name)
print(mess)

#fstrings

mess = f'{g}, {name.upper()}. Welcome!. '.format(g,name)
print(mess)

print(dir(g))

>>>>>>> fd236f1... Basics of List,Tuple,Set
print(help(str))
