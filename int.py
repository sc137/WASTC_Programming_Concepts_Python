# WASTC notes

print ('even though we add .1 ten times, we do not get the answer one')

x = 0.0
x += .1
x += .1
x += .1
x += .1
x += .1
x += .1
x += .1
x += .1
x += .1
x += .1

if x == 1.0:
    print ('x is one')
else:
    print ('x is not one')

print ('x is', x)

print ('but we can get 1.25')

x = 0.0
x += .125
x += .125
x += .125
x += .125
x += .125
x += .125
x += .125
x += .125
x += .125
x += .125

if x == 1.25:
    print ('x is one point two five')

print ('x is', x)


a = 'hello'
b = 'world'
c = a+b
# concatenated strings are immutable - we can't updated c[1]
print (c[1])






