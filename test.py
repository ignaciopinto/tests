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
		print str



p1 = Problem1()
#p1.printNumbers()				
p1.Dots("Hola Mundo")
