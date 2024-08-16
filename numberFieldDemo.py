"""
Program: numberFieldDemo.py
ch8
8.12.24

***NOTE: the module breezypythongui.py MUST be in the same direvtory as this file for the app to run correctly!

GUI-based app which has labels, number entry fields for both input and output and a command buttonn. Button triggers a function that calculates square roots. """


from breezypythongui import EasyFrame
import math
# Other imports can go here

# class header (class name will change project2project)
class numberFieldDemo(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Square Root Calculator", width = 280, height = 160, background = "red4")

		# Label and entry field for the input
		self.addLabel(text = "An integer", row = 0, column = 0, background = "red4", foreground = "white")
		self.inputField = self.addIntegerField(value = 0, row = 0, column = 1, width = 10)
		self.inputField["background"] = "azure"

		# Label and field for the output
		self.addLabel(text = "Square root", row = 1, column = 0, background ="red4", foreground = "white")
		self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 10, precision = 2, state = "readonly")

		# The command button which triggers the convertSqrt() funtion
		self.addButton(text = "Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)

	#global Definition of the computeSqrt() function
	def computeSqrt(self):
		"""Collects the input integer, calculates the square root, and outputs the result."""
		try:
			number = self.inputField.getNumber()
			result = math.sqrt(number)
			self.outputField.setNumber(result)
		except ValueError:
			self.messageBox(title = "Error!", message = "Input must be a non-negative integer!")


# Global defnition of the main() method
def main():
	# Instantiate an object from the class int0 mainloop()
	numberFieldDemo().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()

