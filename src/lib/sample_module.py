class MyClass:
    '''Have name, age and total no of classes attended by all'''
    batch = 'LTT'  # static/class variable
    total_classes = 0
    def __init__(self,name,age):
        self.__name = name
        try:
            if age<0:
                raise Exception(name,age)
            else:
                self.age = age
        except Exception as e:
            print("Negative age",e.args)
            self.age = 20
        self.attendclass = 0
    def getname(self):
        return self.__name

    def getage(self):
        return self.age

    def inc_age(self,yrs):
        self.age += yrs

    def inc_noofClass(self):
        self.attendclass +=1
        #self.__class__.total_classes += 1
        #or
        MyClass.total_classes +=1

    def __repr__(self):
        return "MyClass's object"


class MySubClass(MyClass):
    def __init__(self,name,age,topic):
        MyClass.__init__(self,name,age)
        self.topic = topic

    def getname(self):
        return "S."+MyClass.getname(self)

    def gettopic(self):
        return self.topic

def myadd(x,y):
    return x+y

def mysub(x,y):
    return x-y

if __name__ == "__main__":
    print("From module add",myadd(5,6))
    print("From module sub",mysub(5,3))


