Python swapping
#using temporary variable
x=10
y="ten"
temp=x
x=y
y=temp
print(x)
print(y)

#Using single line syntax
x = 10
y = "ten"

# Step 1
x,y = y,x

print(x)
print(y)
#X will now be ten and y 10

#Variable update operators

#The equal symbol in computer science is used for assignment and does not represent equality used in normal math equations
x = 5
x *= 3
print(x) #It will be 15
#Arithmetic sign placed before equals
