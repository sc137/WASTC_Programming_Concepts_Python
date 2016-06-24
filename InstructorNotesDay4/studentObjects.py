class Student:
  name = None
  gpa = None
  id = None

x = Student()
x.name = 'Joe Student'
x.gpa = 3.5
x.id = 12345

print("%s %f %d" % (x.name, x.gpa, x.id))

import copy
y = copy.copy(x)
y.gpa = 1
print("%s %f %d" % (x.name, x.gpa, x.id))
print("%s %f %d" % (y.name, y.gpa, y.id))

a = [Student() for i in range(10)]
a[0].gpa = 3.67

print(a[0].gpa)
