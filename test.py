class Dog:
    species = "Canine"  # 类属性
    kinds = "PET"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性
        self.__price #私有属性

    def bark(self):       # 实例方法
        print(f"{self.name} says Woof!")

    def Sell_Price(self, real_price):
        self.__price = real_price + 200
        print(f"It's price is {self.__price}")

    @classmethod
    def get_species(cls): # 类方法
        return cls.species

    @staticmethod
    def info():           # 静态方法
        return "This is a dog class."
    
# 创建对象
my_dog = Dog("Buddy")
print(my_dog.name)          #实例调用实例属性，输出：Buddy   
my_dog.bark()               #实例调用实例方法，输出: Buddy says Woof!
print(Dog.get_species())    #直接调用类方法，输出: Canine
print(my_dog.get_species()) #实例调用类方法
print(my_dog.kinds)       #实例调用类属性
print(Dog.kinds)          #直接调用类属性
print(my_dog.info())        #实例调用静态方法
print(Dog.info())           #直接调用静态方法
my_dog.Sell_Price(1000)