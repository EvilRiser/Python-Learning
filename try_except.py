# try:
# 	pass
# except Exception:
# 	pass
# else:
# 	pass
# finally:
# 	pass



#f=open('testfile.txt')
try:
	f=open('input.txt')
	var = bad_var
except FileNotFoundError:
	print('Sorry.This file doesn\'t exist')
# except  Exception:
# 	print('Sorry.Something went wrong')
except Exception as e:
	print(e)


try:
	f=open('input.txt')
except FileNotFoundError:
	print('Sorry.This file doesn\'t exist')
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
	#this runs only when we don't find any exception
finally:
	print("Executing finally...")
	#it will run whether it catches error or not


# to raise own exception
try:
	f=open('input.txt')
	if f.name == 'input.txt':
		raise Exception
except FileNotFoundError:
	print('Sorry.This file doesn\'t exist')
except Exception:
	print('error')
else:
	print(f.read())
	f.close()
	#this runs only when we don't find any exception
finally:
	print("Executing finally...")
	#it will run whether it catches error or not






# print(type(Exception))