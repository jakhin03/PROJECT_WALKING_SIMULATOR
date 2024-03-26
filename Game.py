import random

class normaly:
	def __init__(self, case):
		self.case = case
		self.isNormal = "normal"

	def isNormaly(self):
		if self.case != 0:
			self.isNormal = "abnormal"
	def normalize(self):
		if self.case == 0:
			print("I am normal!")
		if self.case != 0:
			print("I am normal|")
	


if __name__ == '__main__':
	n = 0
	while (n < 10):
		case = random.randint(0,1)
		stage = normaly(case)
		stage.normalize()
		stage.isNormaly()
		print("Stage:", n)
		_input = input("Enter: ")
		if (_input == stage.isNormal):
			n += 1
		else:
			n = 0

		print(" ------------------------ ")
	print("You are normal! congarat tolaution")	