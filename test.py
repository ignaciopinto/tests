import re
class Problem1:
	def __init__(self):
		self.worda = "Foo"
		self.wordb = "Bar"
		self.min = 50
		self.max = 151
		self.multa = 5
		self.multb = 7

	def printNumbers(self):
		for i in range(self.min,self.max):
			fullword = ""
			if i%self.multa == 0 :
				fullword += self.worda
			if i%self.multb == 0:
				fullword += self.wordb
			if i%self.multa != 0 and i%self.multb != 0 :
				fullword = i

			print fullword

	def Dots(self,str):
		forreturn = False
		x = re.search("[0-9A-z](...)[0-9A-z]", str)
		if x :
			numbers = re.findall(r'\d', str)
			i = 0
			while i < len(numbers) :
				print int(numbers[i]) + int(numbers[i+1])
				if int(numbers[i]) + int(numbers[i+1]) <= 10 : 
					forreturn = True
				else:
					forreturn = False
				i+=2
		return forreturn



p1 = Problem1()
p1.printNumbers()				
print p1.Dots("arrb6...4xxbl5...eee5")
