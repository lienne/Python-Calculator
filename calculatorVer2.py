#Simple Calculator

from tkinter import *
from tkinter import ttk

class Calculator:

	# Stores the current value to display in the entry
	calc_value = 0.0
	
	# Will define if this was the last math button clicked
	div_trigger = False
	mult_trigger = False
	add_trigger = False
	sub_trigger = False
	
	def __init__(sef, root):
		self.entry_value = StringVar(root, value = "")
		root.title("Calculator")
		root.geometry("400x400")
		root.resizable(width = False, height = False)
		style = ttk.Style()
		style.configure("TButton", font = "Serif 15", padding = 10)
		style.configure("TEntry", font = "Serif 18", padding = 10)	
		self.number_entry = ttk.Entry(root, textvariable = self.entry_value, width = 50)
		self.number_entry.grid(row = 0, columnspan = 4)
		self.button7 = ttk.Button(root, text = "7", command = lamba: self.button_press("7")).grid(row = 1, column = 0)
		self.button8 = ttk.Button(root, text = "8", command = lamba: self.button_press("8")).grid(row = 1, column = 1)
		self.button7 = ttk.Button(root, text = "9", command = lamba: self.button_press("9")).grid(row = 1, column = 2)
		self.button_div = ttk.Button(root, text = "/", command = lamba: self.math_button_press("/")).grid(row = 1, column = 3)

root = Tk()

calc = Calculator(root)

root.mainloop()
	
	# Called anytime a number button is pressed
	#def button_press(self, value):
		# Get the current value in the entry
	#	entry_val = self.number_entry.get()
		
		# Put the new value to the right of it
		# For ex, if 1 and 2 are pressed, the number is now 12
		# Otherwise the new number goes on the left
	#	entry_val += value
		
		# Clear the entry box
		
		
		
		
		
	
	#exp = []
	#exp = raw_input()

	#def add(exp):
	#	result = int(exp[0]) + int(exp[2])
	#	return result

	#def sub(exp):
	#	result = int(exp[0]) - int(exp[2])
	#	return result

	#def div(exp):
	#	result = int(exp[0]) / int(exp[2])
	#	return result

	#def mult(exp):
	#	result = int(exp[0]) * int(exp[2])
	#	return result

	#if exp[1] == '+':
	#	result = add(exp)
	#	print result
	#if exp[1] == '-':
	#	result = sub(exp)
	#	print result
	#if exp[1] == '/':
	#	result = div(exp)
	#	print result
	#if exp[1] == '*':
	#	result = mult(exp)
	#	print result