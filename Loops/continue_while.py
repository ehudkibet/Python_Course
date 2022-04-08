#Unlike break, continue jumps back to the top of the loop, rather than stopping it.
i = 0
while True:
    i = i +1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")
#the continue statement stops the current iteration and continues with the next one
