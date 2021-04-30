#
# Example file for working with classes
# Functions inside classes are called methods

class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2" + someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2")
        
        
def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")


if __name__ == "__main__":
    main()
