#Simple Calculator

exp = []
exp = raw_input()

if exp[1] == '+':
	result = add(exp)
if exp[1] == '-':
	result = sub(exp)
if exp[1] == '/':
	result = div(exp)
if exp[1] == '*':
	result = mult(exp)


def add(exp):
	result = int(exp[0]) + int(exp[2])
	return result

def sub():
	result = int(exp[0]) - int(exp[2])
	return result

def div():
	result = int(exp[0]) / int(exp[2])
	return result

def mult():
	result = int(exp[0]) * int(exp[2])
	return result