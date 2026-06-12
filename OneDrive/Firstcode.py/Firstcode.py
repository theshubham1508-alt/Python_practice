# del keyword
class student:
    def __init__(self, name):
        self.name = name

s1 = student("shubham")
del s1.name 
print(s1.name)



#private (like) attributes & metod
class account :
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = account("12345","abcde")

print(acc1.acc_no)
print(acc1.acc_pass)


#inheritance
class car :
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop ():
        print("car stopped.")

class toyota(car):
    def __init__(self, name):
        self.name = name

car1 = toyota("fortuner")
car2 = toyota("prius")

print(car1.name)


#multi-level inheritance
class car :
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop () -> None:
        print("car stopped.")

class toyota(car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(toyota):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

car1 = fortuner("toyota","diesel")
car1.start()

#multiple inheritance
class A:
    varA = "welcome to classs A"

class B:
    varB = "welcome to class c"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA) 



#super method
class car :
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop () -> None:
        print("car stopped..")

class toyota(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.type = name
        super().start()


car1 = toyota("prius","electric")
print(car1.type)


#class method 
class person:
    name = "shubham"

    def changeName(self, name):
        self.name = name

p1 = person()
p1.changeName("rahul kumar")
print(p1.name)


#property
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98,97,99)
print(stu1.percentage)


#property
class student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self): 
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98,97,99)
print(stu1.percentage) 

stu1.phy = 86
print(stu1.percentage)


#polymorphism operator
print(1+2)
print("shubham"+"rajput")
print([1,2,3]+[4,5,6])


#complex
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

num1 = complex(1,3)
num1.showNumber() 


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# define a employee class with attributes role department and salary. this class  has also show detail() method 
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("Engineer", "IT", "75,000")
        self.name = name
        self.age = age

engg1 = Engineer("Elon musk","40")
engg1.showDetails()



# Create a last call Order which store item and its price use Dunder function --gt--() to convey that : order1>order2. if price of order 1> price of order 2
class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = order("chips", 20)
ord2 = order("tea", 15)
print(ord1 > ord2)



                 






