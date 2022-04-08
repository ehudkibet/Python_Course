#Simple merging
'''dict1={'a':1,'b':2,'c':3,'d':4}
myDict1={k:v*2 for (k,v) in dict1.items()} #Doubling the value
myDict2={k*2:v for (k,v) in dict1.items()}#Doubling the key
myDict3={k*2:v*2 for (k,v) in dict1.items()} #Doubling both key and value
print(myDict1)
print(myDict2)
print(myDict3)'''

#Convert temp in Farenheit to degrees
'''dict2={'a':-30,'b':-20,'c':-10,'d':0,'e':10,'f':20}
myDict2={k:round((v-32)*5/9) for (k,v) in dict2.items()}
print(myDict2)'''

#Conditional merging
dict1={'a':1,'b':2,'c':3,'d':4}
myDict1={k:v for (k,v) in dict1.items() if v>2}#values greater than 2
print(myDict1)


