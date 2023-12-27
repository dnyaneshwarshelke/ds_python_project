class students:
    '''This class will consist of different attribute for students'''
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.subject=subject
    def sub(self):
        print(f"The student name {self.name.title()} is having this subject {self.subject.title()}" )
    def age1(self):
        print(f"{self.age.title()} is qualified for the subject")
    
results=students('Dnyanu','23','English')
results.sub()
results.age1()


