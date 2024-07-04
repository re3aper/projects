# Class definition from the top as constructor parameters
class human():
	def func(self):
	    print("age",":",self.age)
	    print("sex",":",self.sex)
	    print("hormones",":",self.hormones)
	def ret_func(self,age):
	    print(age)
        def __init__(self,age,sex,hormones):
		self.age=age
	    	self.sex=sex
	    	self.hormones=hormones
# Define setters:
	def setage(self,age):
		self.age=age
	def setsex(self,sex):
		self.sex=sex
	def sethormones(self,hormones):
		self.hormones=hormones

# Define getters:
	def getage(self):
		print (self.age)
	def getsex(self):
		print (self.sex)
	def gethormones(self):
		print (self.hormones)

# Define objects & call them
age=int(input("Enter average Age \n"))
sex=int(input("Enter interpersonal sex \n"))
hormones=int(input("Enter hormone type \n"))
ageint={1,80}
sexint={'M','F'}
hormint={'T','E'}
Henry=human(age,sex,hormones)
def sexval(age,hormones):
	if age<68 and hormones='T' and sex=None:
	 sex='M'
	 print("Sex condition undefined \n")
	elif age>68 and hormones='E'and sex=None:
	 sex='F'
	 print("Sex condition undefined \n")
	elif sex='M' and hormones='T' and age=None:
	 age=68
	 print("Age condition undefined \n")
	elif age>68 and sex='F' and hormones=None:
	 hormones='E'
	 print("Hormones undefined \n")
		



Henry.ret_func(Henry)
Henry.func()






	

	    
	    
