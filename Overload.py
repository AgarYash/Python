class Parent:
    def myMethod(self):
        print "Calling parent method"
        
class Child(Parent):
    def myMethdo(self):
        print 'Calling child method'

c=Child()
c.myMethod()
