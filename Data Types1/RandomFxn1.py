import random
mylist=[4,12,17,20]
random.shuffle(mylist) #Shuffle
print(mylist)

print(random.uniform(20000,300000)) #Generate random number between the values given
print(round(random.uniform(20000,300000))) # Generate whole number between the values given

import math
#finding cose
print(math.cos(180))

#given radians, you can convert to degrees and find cos
print(math.cos(math.degrees(3.142)))
#PS: 3.142 is not exactly 180 degrees so it will give a different value to 180

#given degrees you can convert to radians and find degrees
print(math.cos(math.radians(180)))


