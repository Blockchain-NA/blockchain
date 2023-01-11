import hashlib as h
import datetime as d
from Crypto.PublicKey import RSA
from blockchain import Blockchain
from block import Block
from transaction import Transaction

def sha256(o):
  #The string inside update() is the string to be hashed
    #encode('utf-8')
      #utf-8 is a formatting for text - each character in this formatting is one byte, or 8 bits
        #you may have seen this in the top of the windows notepad app
      #so basically the encode function is turning the string into a utf-8 formatted string
  return h.sha256(o.encode('utf-8')).hexdigest() #this is the hash as a hexadecimal string, im guessing

# Assuming the inputs ARE already hashed
def merkle(list):
  if (len(list) == 1):
    return list[0]
  new = [hash(list[x] + list[x+1]) for x in range(0, len(list) - 1, 2)]
  if (len(list) % 2 != 0):
    new.append(list[-1])
  return merkle(new)

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