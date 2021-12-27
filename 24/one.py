# --- Advent of code 2021: Day 24 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

class ALU:
	def __init__(self, program):
		self.regs = { "w": 0, "x": 0, "y": 0, "z": 0 }
		self.ins = program[:]
		self.data_in = []

	@staticmethod
	def isnumeric(a):
		return a.isnumeric() or a[0] == '-' and a[1:].isnumeric()

	def input(self, number):
		self.data_in = list(str(number))[::-1]

	def execute(self, instruction, a, b=None):
		if instruction == "inp":
			self.regs[a] = int(self.data_in.pop())
		elif instruction == "add":
			if ALU.isnumeric(b):
				self.regs[a] -=- int(b)
			else:
				self.regs[a] -=- self.regs[b]
		elif instruction == "mul":
			if ALU.isnumeric(b):
				self.regs[a] *= int(b)
			else:
				self.regs[a] *= self.regs[b]
		elif instruction == "div":
			if ALU.isnumeric(b):
				self.regs[a] //= int(b)
			else:
				self.regs[a] //= self.regs[b]
		elif instruction == "mod":
			if ALU.isnumeric(b):
				self.regs[a] %= int(b)
			else:
				self.regs[a] %= self.regs[b]
		elif instruction == "eql":
			if ALU.isnumeric(b):
				self.regs[a] = int(self.regs[a] == int(b))
			else:
				self.regs[a] = int(self.regs[a] == self.regs[b])

	def run(self):
		self.regs = { "w": 0, "x": 0, "y": 0, "z": 0 }
		for asm in self.ins:
			if "inp" in asm:
				ins, a = asm.split(" ")
				self.execute(ins, a)
			else:
				ins, a, b = asm.split(" ")
				self.execute(ins, a, b)

	def valid(self):
		return self.regs["z"] == 0

program = open("input.txt").read().splitlines()

alu = ALU(program)
alu.input("99999795919456")
alu.run()
if alu.valid():
	print("Valid!")

assert alu.valid()

'''
Constrains for my program:

n1 > 3
n2 > 4
n3 > 2
n4
n5  = n4
n6  = n3  - 2
n7  > 8
n8  < 6
n9  = n8  + 4
n10 = n7  - 8
n11 > 5
n12 = n11 - 5
n13 = n2  - 4
n14 = n1  - 3

Check input.c for a decompiled version of the program.

'''
