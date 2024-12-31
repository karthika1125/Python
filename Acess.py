                        # Public

# class Person():
#     def __init__(self,Name,age):
#         self.name=Name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# x=Person("Sidhu",12)
# x.display()
# class student(Person):
#     pass
# x=student("karthika",14)
# x.display()


                                #   private

# class bankAccount:
#     def __init__(self,account,balance):
#         self.__account=account
#         self.__balance=balance
#     def __display(self):
#         print(self.__balance)
# b=bankAccount(1258945,530)
# b.__display()        

                                        
                    #    protected

class person():
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def _display(self):
        print("Name : ",self._name)
        print("Age : ",self._age)

class student (person):
    def __init__(self, name, age,rollnumber):
        super().__init__(name, age)  
        self.rollnumber=rollnumber
    def display(self):
        self._display()
        print("rollnumber :",self.rollnumber)
        
x=student("sidhu",20,101)
x.display()             

        

