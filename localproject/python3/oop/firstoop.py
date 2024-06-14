class First:
    name="Ivan Rashkov"
    age=34
    sex="M"
    def func(self):
        print("name",":",self.name)
        print("age",":",self.age)
        print("sex",":",self.sex)

firstp=First()
firstp.func()

class second(First):
	def func2(self):
         print("Anything good")
  
x=second()
x.func2()


