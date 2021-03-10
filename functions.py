def my_function():
    print("hello world")
my_function()

def sum (x,y):
    a=x+y
    print("the sum is",a)
sum (10,20)
sum(501,987)

def multiply (x,y):
    a=x*y
    print("the multiplication is",a)
multiply (10,20)
multiply(501,987)

def modulus (x,y):
    a=x%y
    print("the modulus is",a)
modulus (10,20)
modulus(501,987)

def courses (*args):
    for subject in args:
        print(subject)
courses ("breeding horses", "bee keeping", "writing programmes")

def course(**kwargs):
    for key, value in kwargs.items():
       print("{}:{}".format(key,value))
course(first='breeding horses', second='bee keeping', third='writing programmes')

def Kenya(county = "Marsabit"):
    print("i am from" + county)
Kenya()
Kenya("Nairobi")
Kenya("Meru")
Kenya("Kisumu")
#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["Pomegranate", "Grapes", "Peach"]
my_function(fruits)
#find the area of a circle
def findArea(r): 
    PI=3.142
    return PI*(r*r);
    num=float(input("Enter r value:"))
    print("Area is %.6f" % findArea(num));

