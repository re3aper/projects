class first:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def func(self):
        print("name",":",self.name)
        print("age",":",self.age)
        print("sex",":",self.sex)

firstperson=first("Ivan",34,"M")
firstperson.func()

