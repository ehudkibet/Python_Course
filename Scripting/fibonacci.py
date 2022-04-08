#Module to write fibonacci series from 0 and 1 to any number.
def fib(n): #return fibonacci series upto n
    result=[]
    a,b=0,1
    while a < n:
        result.append(a)
        a,b=a,a+b
    return result
#Try it out in the next py file called two