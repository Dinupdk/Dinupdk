#class is combination of variables and methods
class student:
    def __init__(self,id,name,age):  
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
        self.id=id
        self.name=name
        self.age=age
#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.
    def printall(self):
        print(self.id,self.name,self.age)
    
s=student(1,'dinesh',20)#creation methods
s.printall()  #callthe class function

    