
class antAccount:
    antcount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        antAccount.antcount +=1

    def displayCount(self):
        print(antAccount.antcount)


ant1 = antAccount("小张",100)
ant1.displayCount()

class Parent:
    parentAttr = 100
    def __init__(self):
        print("父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getattr(self):
        print(Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("子类构造函数")

    def childMethod(self):
        print("子类方法")


c = Child() #子类实例化
c.childMethod()
c.parentMethod()
c.setAttr("300")
c.getattr()


