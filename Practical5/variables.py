#some simple math task
print('some simple math task:')
#think of a 3-digit number, for example 123 in the script. Store it in a variable a.
a = 123
#Create	another	variable called b and assign to it a six-digit number, created	by writing the digits of a twice (in this example, 123123).
b = 123123
c = b/7
d = c/11
e = d/13
# compare a and e
if a <e:
    print("result : e is greater")
elif a>e:
    print("result : a is greater")
else:
    print("result : e and a are equal")
#Booleans task
print('Booleans task:')
#Create and input a Booleans variable X 
x=eval(input("please input a Boolean variable X="))
#Create and input a Booleans variable Y
y=eval(input("please input a Boolean variable Y="))
# Calculate the value of Z and W
Z = (x and not y) or (y and not x)
W = (x!=y)
#verify the consistence of Z and W
print ('is Z euqal to W?','result:',Z==W)