#Python tuples
myTuple=('physics','chemistry',1997,2000)
print(myTuple[1:3])
del myTuple #Delete entire tuple as deleting individual componenets not possible
myTuple=('Kwame','Zuri')
myList=list(myTuple)#Conversion
print (myList)

myList1=['apple','orange','pear']
myTuple1=tuple(myList1)
print(myTuple1)
print(len(myTuple1))#Get length
#Iterate in a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
 print(x)

