class student:
    school_name='xyz' #static variable unchanged value
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printall(self):
        print(self.id,self.name,student.school_name)

s=student(1,'Dinesh')
s.printall()