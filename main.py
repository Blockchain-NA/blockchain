import datetime as d
from Crypto.PublicKey import RSA
from blockchain import Blockchain
from block import Block
from transaction import Transaction


# Assuming the inputs ARE already hashed


'''
Basic terminology
An object is a piece of data. It can have properties, which can have also be objects
  Ex: Say you have an object called Jason. Then some properties could be Jason.age, Jason.shoes, etc
A class is a template for an object
  Whenever you call the class's constructor, __init__(), it creates an object and runs the code inside the constructor
  Example code (say we have a class Person): 
    class Person:
      def __init__(self, years):
        #when this function is called, all we do is set the property age to years
        self.age = years;
    Jason = Person(5); #__init__(5) is called here; i know, this is confusing, but think of Person() as __init__()
    print(Jason.age); #prints 5
Also try searching how to code in python if the stuff here does not make sense
'''






    





#testing random stuff here
def main():
  bc = Blockchain()

  t = Transaction("jim", "bob", 5)
  m = Transaction("jim", "bob", 6)
  z = Transaction("jim", "bob", 7)

  someTransactions = [t, m, z]

  b1 = Block([t,z], d.datetime.now())
  b2 = Block([t,m], d.datetime.now())
  b3 = Block(someTransactions, d.datetime.now())
  b4 = Block([z], d.datetime.now())

  bc.add_block(b1)
  bc.add_block(b2)
  bc.add_block(b3)
  bc.add_block(b4)
  
  #Sbc.generateKeys()

  bc.out()

main()