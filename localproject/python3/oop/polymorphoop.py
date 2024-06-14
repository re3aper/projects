import time
class third:
	def __init__(self,CPU,MEM,SWP,DSK):
	 self.CPU=CPU
	 self.MEM=MEM
	 self.SWP=SWP
	 self.DSK=DSK
# Define gathers for parameters bellow this line untill L16#
	def getmem(self):
         print (self.MEM)
	def getcpu(self):
	 print (self.CPU)
	def getswp(self):
	 print (self.SWP)
	def getdks(self):
	 print (self.DSK)

# Define setters for parameters bellow this line untill L26#
	def setmem(self,MEM):
	 	self.MEM=MEM
	def setcpu(self,CPU):
		self.CPU=CPU
	def setswp(self,SWP):
		self.SWP=SWP
	def setdsk(self,DSK):
		self.DSK=DSK

class fourth(third):
	
	def func1(self):
	 print(self.CPU,self.MEM,self.SWP,self.DSK)


Comp1=fourth("11th Gen Intel(R) Core(TM) i7-11700F @ 2.50GHz","32Gi","127Gi","C:\\ \n, D:\\ \n, E:\\ \n")
Comp1.getmem
Comp1.setmem("64Gi")
Comp1.getcpu
Comp1.setcpu("AMD Threadripper")
Comp1.func1()
