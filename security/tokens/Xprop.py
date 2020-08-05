

box = {'pop':100, 'laylow':102}

class MagicNumber:
    def __init__(self, name, value):
        self.value = value
        self.name = name
    
    def __dir__(self):
        return ['value', 'name']
    
    @classmethod
    def frombox(cls, name, box):
        return cls(name, box[f'{name}'])

    
    def display(self):
        print(self.name +"'s value is : " + str(self.value))


m1 = MagicNumber('pop', 100)
m1.display()
m2 = MagicNumber.frombox('laylow', box)
m2.display()

# hasattr -> bool : check if an object have an attribute

class Person:
  def __dir__(self):
    return ['age', 'name', 'salary']
    

teacher = Person()
print(dir(teacher))