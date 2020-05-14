# What does this piece of code do?
# Answer: get 1 and prime number

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint
# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
p=False
while p==False:
    p=True
# generate a random integer equal to or larger than 1 but equal to or smaller than 100 to test if it is a prime number
    n = randint(1,100)
    u = ceil(n**(0.5))
    #u+1 to solve if the square root is integer
    for i in range(2,u+1):
        if n%i == 0:
#if the generated number can be divided by some number that is not 1 and itself, then it is not a prime number and we set p as 'flase' to restart the loop
            p=False
# the result is a random prime number between 1 and 100 or 1. And the result changes each run
print(n)
