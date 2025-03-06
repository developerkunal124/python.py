#creation of list 
a=[]   
print(type(a))

a=[1,2,3,4,5]
print(a)

#list of mixed data types
b=[1,2,3,"hello", 1.1]
print(a)

#indexing
c=[1,2,3,4,5]
print(a[0])
print(a[0:4])

#formatting of list
c=[1,4,5,4,8]
#formating contain C
c.reverse()
print(c)
c.sort( reverse=False)
# b.sort()
# print(b)    TypeError: '<' not supported between instances of 'str' and 'int'
print(c)
# length finding.

len(b)
print(len(b))

#Adding elements to the list
b.insert( 3,"kunal")

print(b)
#finding
print("kunal" in b)
print(b.index("kunal"))
#update.
b[3]="kushal"
print(b)
#removing.
b.remove("kushal")
print(b)
