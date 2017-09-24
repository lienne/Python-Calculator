#Simple Calculator

# Python's GUI library
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
	
	# Called anytime a number button is pressed
	def button_press(self, value):
	
		# self refers to our current object, in this case our calculator class
		# Get the current value in the entry
		entry_val = self.number_entry.get()
		
		# Put the new value to the right of it
		# For ex, if 1 and 2 are pressed, the number is now 12
		# Otherwise the new number goes on the left
		entry_val += value
		
		# Clear the entry box
		self.number_entry.delete(0, "end")
		
		# Insert the new value going from left to right
		self.number_entry.insert(0, entry_val)
		
	# Returns true or false if the string is a float
	def isFloat(self, str_val)
		try:
			# If the string isn't a float, float() will throw a ValueError
			float(str_val)
			
			# If there is a value you want to return, use return
			return True
		except ValueError:
			return False
	
	# Handles logic when math buttons are pressed
	def math_button_press(self, value)
		
		# Only do anything if entry currently contains a number
		if self.isFloat(str(self.number_entry.get())):
			
			# Make false to cancel out previous button click
			self.add_trigger = False
			self.sub_trigger = False
			self.mult_trigger = False
			self.div_trigger = False
			
			# Set the math button click so when equals is clicked,
			# that function knows what calculation to use
			if value == "/":
				print("/ Pressed")
				self.div_trigger = True
			elif value == "*":
				print("* Pressed")
				self.mult_trigger = True
			elif value == "+":
				print("+ Pressed")
				self.add_trigger = True
			else:
				print("- Pressed")
				self.sub_trigger = True
			
			# Clear the entry box
			self.number_entry.delete(0, "end")
	
	# Performs a mathematical operation by taking the value before the math button is clicked.
	# Then perform the right calculation by checking what math button was clicked last
	def equal_button_press(self):
		
		# Make sure a math button was clicked
		if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
			
			if self.add_trigger:
				solution - self.calc_value + float(self.entry_value.get())
			elif self.sub_trigger:
				solution = self.calc_value - float(self.entry_value.get())
			elif self.mult_trigger:
				solution = self.calc_value * float(self.entry_value.get())
			else:
				solution = self.calc_value / float(self.entry_value.get())
				
			print(self.calc_value, " ", float(self.entry_value.get()), " ", solution)
			
			# Clear the entry box
			self.number_entry.delete(0, "end")
			
			self.number_entry.insert(0, solution)
	
	
	# Create our interface
	def __init__(sef, root):
		
		# Will hold the changing value stored in the entry
		self.entry_value = StringVar(root, value = "")
		
		# Define title for the app
		root.title("Calculator")
		
		# Defines the width and height of the window
		root.geometry("430x220")
		
		# Block resizing of the window
		root.resizable(width = False, height = False)
		
		# Customize the styling of the buttons and entry
		style = ttk.Style()
		style.configure("TButton", font = "Serif 15", padding = 10)
		style.configure("TEntry", font = "Serif 18", padding = 10)
		
		# Create the text entry box
		self.number_entry = ttk.Entry(root, textvariable = self.entry_value, width = 50)
		self.number_entry.grid(row = 0, columnspan = 4)
		
		# First row of buttons
		self.button7 = ttk.Button(root, text = "7", command = lamba: self.button_press("7")).grid(row = 1, column = 0)
		self.button8 = ttk.Button(root, text = "8", command = lamba: self.button_press("8")).grid(row = 1, column = 1)
		self.button7 = ttk.Button(root, text = "9", command = lamba: self.button_press("9")).grid(row = 1, column = 2)
		self.button_div = ttk.Button(root, text = "/", command = lamba: self.math_button_press("/")).grid(row = 1, column = 3)
		
		# Second row of buttons
		self.button4
		self.button5
		self.button6
		self.button_mult
		
		# Third row of buttons
		self.button1
		self.button2
		self.button3
		self.button_add
		
		# Fourth row of buttons
		self.button_clear
		self.button0
		self.button_equal
		self.button_sub


# Get the root window object 
root = Tk()

# Create the calculator
calc = Calculator(root)

# Run the app until exited
root.mainloop()
		
		
		
		
		
	
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