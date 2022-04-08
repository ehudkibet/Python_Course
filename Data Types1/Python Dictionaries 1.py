#Python Dictionaries
myDict={'name':'Zara','Age':21,'class':'4th year'}
print(myDict.keys()) #Obtain keys
print(myDict.values()) #obtain values
print(myDict.items()) #Obtain both keys and values
print(myDict['name']) #Indexed using keys
print(myDict['Age'])

#Making a dictionary from lists&Tuples
list1=['James','John','Elvis']
list2=[1999,2000,2005]
dict1=dict(zip(list1,list2)) #We use zip()
print(dict1)

tuple1=('Kenya','Uganda','Rwanda')
tuple2=('Nairobi','Kampala','Kigali')
capitals=dict(zip(tuple1,tuple2))
print(capitals)




