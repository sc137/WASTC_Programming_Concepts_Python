# WASTC 2016
# Sable Cantus

class Student:
    name = None
    gpa = None
    id = None
    
x = Student()

x.name = "Bart Simpson"
x.gpa = 3.5
x.id = "000000000"

#to copy an object from one var to another, you need copy (or deep copy)

import copy
y = copy.copy(x)
y.name = "Bart's Friend"
y.gpa = 1
y.id = "000000001"
print ("%s %.2f %s" % (x.name, x.gpa, x.id))
print ("%s %.2f %s" % (y.name, y.gpa, y.id))

a = [Student() for i in range(10)]
a[0].gpa = 3.67

print(a[0].gpa)