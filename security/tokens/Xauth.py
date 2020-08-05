from os import urandom
from time import localtime

def time_stamp():
    timestamp = localtime()
    timestampkeys = ['year', 'mon', 'mday', 'hour', 'min', 'sec', 'wday', 'yday', 'isdst']
    token = ""
    public_token = 0
    for key in timestampkeys:
        token += str(timestamp.__getattribute__(f"tm_{key}"))
        public_token += timestamp.__getattribute__(f"tm_{key}")
    return {'public_token':public_token, 'secret_token':token}



class Base(object):
    def __init__(self, pub, secret_number):
        self.pub = hash(pub)
        self.token = hash(pub*secret_number)
    
class Empty(Base):

    def token_pub(self):
        return abs(self.token)



# print(Empty(time_stamp()['secret_token'], 0x00777).token_pub())

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

person = Person(23, 'Adam')



o = 0
while o == 1:
    password = input('password ➜ ')
    if hash(password).__eq__('realmdp'):
        print('success', hash(password))
        break
    else:
        print('[!] invalid password')




class Mammal(object):
  def __init__(self, mammalName, what):
    print(mammalName, 'is a warm-blooded animal.', what)
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Warm', 'A shit append')
    
d1 = Dog()
d2 = Dog().__setattr__('mammalName', 'Roudolph')
objects = [d1, d2]

# print(*objects, sep=',')

# RUN : python -m http.server --bind 0.0.0.0 81  

# xreq = __import__('requests', globals(), locals(), fromlist=(), level=0)

# request = xreq.get('http://localhost:81')

# print(request.text)

print({1,2,4,3}.union({1,4,2,3,3,2,3})
