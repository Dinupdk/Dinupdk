class A:
    def __init__(self,a_value):
        self.a=a_value
    def get_a(self):
        print('A_value :',self.a)

class B(A):
    def __init__(self,a_value,b_value):
        A.__init__(self,a_value) #like import 
        self.b=b_value
    def get_b(self):
        print('B_value:',self.b)

obj1=B(10,20)
obj1.get_a()
obj1.get_b()