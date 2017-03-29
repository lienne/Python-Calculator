#Simple Calculator

exp = []
exp = raw_input()

def add(exp):
	result = int(exp[0]) + int(exp[2])
	return result

def sub(exp):
	result = int(exp[0]) - int(exp[2])
	return result

def div(exp):
	result = int(exp[0]) / int(exp[2])
	return result

def mult(exp):
	result = int(exp[0]) * int(exp[2])
	return result

if exp[1] == '+':
	result = add(exp)
	print result
if exp[1] == '-':
	result = sub(exp)
	print result
if exp[1] == '/':
	result = div(exp)
	print result
if exp[1] == '*':
	result = mult(exp)
	print result