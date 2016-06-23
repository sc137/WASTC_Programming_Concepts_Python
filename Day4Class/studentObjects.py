import copy
class Student:
    name = None
    gpa = None
    id = None
x = Student()
x.name = 'Joe Student'
x.gpa = 3.5
x.id = 12345
print("%s %.2f %d" %(x.name, x.gpa, x.id))

y = copy.copy(x)
y.gpa = 1
print("%s %.2f %d" %(x.name, x.gpa, x.id))
print("%s %.2f %d" %(y.name, y.gpa, y.id))

a = [Student () for i in range(10)] # creates 10 objects of students all at once but takes up more space
a[0].gpa = 3.67
a[0].name = "frank"
a[0].id = 4321
print("%s %.2f %d" %(a[0].name, a[0].gpa, a[0].id))