class First:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def getname(self):
    	return self.name

    def setname(self,name):
	       self.name=name

    def func(self):
        print("name",":",self.name)
        print("age",":",self.age)
        print("sex",":",self.sex)

firstperson=First("Ivan Rashkov", 34,"M")
firstperson.setname("Peter Petrov")
firstperson.getname()
firstperson.func()

