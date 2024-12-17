"""
class Student:
    # method __init__ defines attributes
    def __init__(self):
        self.name = "Vishnu"
        self.age = 10
        self.marks = 100

    # method talk() defines a method
    def talk(self):
        print("Hi, I am",self.name)
        print("My age is",self.age)
        print("My marks are",self.marks)

s1 = Student()
print(s1)
# s1.talk()
# they only retrieve the attribute values but do not print them. To print use the print statement.
# Only the values are displayed.
# for the method to be displayed use:
s1.talk()
print(s1.name)
print(s1.age)
print(s1.marks)
"""

"""
Constructor
1. A constructor is a special method that is used to initialize the instances variables of the class.
2. In the constructor, we create the instance variables and initialize them with some starting values.
3. The first parameter of the constructor will be "self" variable that contains the memory address of
   the instance.
4. Here, the constructor has only one parameter, i.e "self". 
   Using "self.name" and "self.marks" we can access the instance variables of the class.
5. A constructor is called at the time of creating an instance. So, the above instance will be called when 
   we create an instance as:
    s1 = Student()

"""

def __init_(self):
    self.name = "Vishnu"
    self.marks = 800

s1 = Student()

"""
6. Here, "s1" is the name of the instance. The empty parentheses after the class name "Student". These empty
   parentheses represent that we are not passing any values to the constructor.
7. Any values to be passed to the constructor, then we have to pass them in the parentheses after the 
   class name.

"""
def __init__(self, n = "", m=0):
    self.name = n
    self.marks = m
"""
8. 

"""