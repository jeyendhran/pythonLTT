class Computer:
    def __init__(self,n):
        self.name = n

    def __str__(self):
        return  "My computer name is "+self.name

    def execute(self):
        return "executed a prgm"

class Synthesizer:
    def __init__(self,n):
        self.name = n

    def __str__(self):
        return  "My synthesizer name is "+self.name

    def play(self):
        return "can able to play a song"

class Human:
    def __init__(self,n):
        self.name = n

    def __str__(self):
        return  "My name is "+self.name

    def speak(self):
        return "can able to speak"


class Adapter:
    def __init__(self,obj,adapter_meth):
        self.obj = obj
        self.__dict__.update(adapter_meth)



comp = Computer("Mac")
print(comp,"and it was",comp.execute())
mysyn =Synthesizer("Mysyn")
print(mysyn,"and it",mysyn.play())
me = Human("Jeyendhran")
print(me,"and I",me.speak())
objects = [comp]
objects.append(Adapter(mysyn,dict(execute=mysyn.play)))
objects.append(Adapter(me,dict(execute=me.speak)))
for i in objects:
    print(i,i.execute())

class Projector:
    def __init__(self,n):
        self.name  = n
    def hdmiconnector(self):
        return self.name+" connected to hdmiconnector"

class Intel:
    def __init__(self,n):
        self.name = n
    def vgiconnector(self):
        return self.name+" connected to VGI connector"

class MacInTosh:
    def __init__(self,n):
        self.name = n
    def usbconnector(self):
        return self.name+" connected to usb connector"

proj = Projector("Myprojector")
intel = Intel("MyIntel")
mac = MacInTosh("MyMac")

inteladapter = Adapter(intel,dict(hdmiconnector = intel.vgiconnector))
macadapter = Adapter(mac,dict(hdmiconnector = mac.usbconnector))
print()
print(proj.hdmiconnector())
print(macadapter.hdmiconnector())
print(inteladapter.hdmiconnector())
print(inteladapter)


