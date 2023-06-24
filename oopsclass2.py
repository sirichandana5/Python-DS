class student():
    stname='siri' #instance or class varaiable
    stroll=2057
    stmajor='CSE'
    def toprint(self):
        stname='sy1'
        print("local variable",stname)  #local variable,can be same
        #access instance variable inside funtion
        print("instance/class variable",self.stname)
        print("instance/class variable",self.stroll)
    def secondfunction(self):
        print("second function")
s1 = student()
s2 = student()
print(s1.stroll)
print(s1.stmajor)
print("s2",s2.stname)
s1.toprint()
s2.toprint()
s2.secondfunction()
