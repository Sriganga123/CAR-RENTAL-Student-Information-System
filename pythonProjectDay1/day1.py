print ('hello')
import keyword
print(keyword.kwlist)


a=100
print(type(a))
b=10.19199
print(type(b))

print(id(a))
print(id(b))

_=1000 # valid variable
print(_)


name='Python'
value=' is a programming language'
print(name+value) # conactenation

print(name*3) # repetition

#lists
l1=[10,20,30,40,50]
print(l1)
print(l1[0])
print(l1*10)
l2=[90,98]
print(l1+l2)

print(dir(l1))# prints all the functions of list

#accessing list elements( by iterating)
for i in l1:
    print(i)

# list supports heterogenous or disimilar data
l3=[11,23.45,2+6j,'stone',11,11]
print(l3)

l3[5]=89
print(l3)

#nested list
l4=[[1,2,3,4],78,97,54]
print(l4[0])
print(l4[0][3])
print(l4[3])

#tuple
t=(10,20,30,40,50)
print(t)
print(type(t))
print(t[0])

print(dir(t))
t1=(10)
print(t1)
print(type(t1))

l5=[100]
print(type(l5))

s={5,10,15,20,20}
print(s)
print(dir(s))
d={1:'a',2:'b',3:'c'}
print(d)
d1={1:'a',1:'b',3:'b'}
print(d1)
print(d[1])

for i in d:
    print(i)

for i in d:
    print(d[i])

for i in d:
    print(i,d[i])

for i,j in d.items():
    print(i,j)

print(dir(d))