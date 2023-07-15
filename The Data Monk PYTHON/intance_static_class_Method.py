class MyClass:
    class_variable = 0


    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        print("This is an instance method.")
        print("Instance variable:", self.instance_variable)
        print("Class variable:", MyClass.class_variable)



    @staticmethod
    def static_method():
        print("This is a static method.")
        print("Class variable:", MyClass.class_variable)


    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print("Class variable:", cls.class_variable)


        
# Creating an instance of the class
obj = MyClass("hello")
# Calling instance method
obj.instance_method()
# Calling static method
MyClass.static_method()
# Calling class method
MyClass.class_method()