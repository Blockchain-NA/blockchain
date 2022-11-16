import hashlib as h
import datetime as d
from Crypto.PublicKey import RSA

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


class Block:
  #Constructor: initialize (create) a block given some parameters
    #The constructor sets a bunch of properties to those parameters
  #Example: myBlock = Block("data", 0, d.datetime.now(), None, 0)
  def __init__(self, transactions, index, timestamp, previous):
    self.transactions = self.compile_transactions()
    self.index = index
    self.previous = previous
    self.nonce = 0
    self.timestamp = timestamp
    self.hash = self.hash_block()
    
  #Returns the hash of the block
  def hash_block(self):
    block_encryption = h.sha256()
    
    #The string inside update() is the string to be hashed
    #str() casts the instance data to strings
    #encode('utf-8')
      #utf-8 is a formatting for text - each character in this formatting is one byte, or 8 bits
        #you may have seen this in the top of the windows notepad app
      #so basically the encode function is turning the string into a utf-8 formatted string
    block_encryption.update(
      (str(self.index) + str(self.timestamp) + str(self.transactions) +
       str(self.previous) + str(self.nonce)).encode('utf-8'))

    return block_encryption.hexdigest() #this is the hash as a hexadecimal string, im guessing

  #a function for mining the block
  def mine_block(self, difficulty):
    #The while loop keeps hashing the block with a different nonce value until the block's hash satisfies some condition given by the difficulty value
    #after the loop finishes
    while (self.hash[-difficulty:] != "".zfill(difficulty)):
      self.nonce += 1
      self.hash = self.hash_block()   
    
    return True
  
  def compile_transactions(trans):
    #for t in trans:
     # pass
    pass

#The Blockchain is currently being stored as an array of blocks
class Blockchain:
  def __init__(self):
    #Here is the chain, which as you can see is initialized as an array with a single block inside of it
      #This block is self.add_genesis() (see the function add_genesis(self) for more info)
    self.chain = [self.add_genesis()] #A

  #This function returns the first block (genesis block) in the chain (hence the function is only going to be used once)
  def add_genesis(self):
    return Block("data", 0, d.datetime.now(), None)

  #This function is called when you just receive 
  @staticmethod
  def add_block(self, block):
    if (block.mine_block()):
      block.index = len(self.chain)
      self.chain.append(block)
      
  #to be explained
  def addTransaction(self, sender, receiver, amt, keyString, senderKey):
    senderKeyByte = senderKey.encode('ASCII')

  def generateKeys(self):
    keys = RSA.generate(2048)
    pub_key = keys.publickey().export_key()
    priv_key = keys.export_key()
    #file_out = open("private.pem", "wb")
    #file_out.write(priv_key)
    print(pub_key.decode('ASCII'))
    print(priv_key.decode('ASCII'))
    return pub_key.decode('ASCII')
    



class Transaction(object):
  def __init__(self, sender, receiver, amount):
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
    self.time = d.datetime.now()
    self.hash = self.hash_transaction()
  
  def hash_transaction(self):
    hash_encryption = h.sha256()

    hash_encryption.update(
      (str(self.sender) + str(self.receiver) + str(self.amount) +
       str(self.time)).encode('utf-8'))

    return hash_encryption.hexdigest()
  
  def signTransaction():
    pass
    


g = Block("fdaksf", d.datetime.now(), 5, 5)
print(g.hash)

g.mine_block(5)
print(g.hash, g.nonce)
b = Blockchain()
b.generateKeys()


t = Transaction("jim", "bob", 5)
m = Transaction("jim", "bob", 6)
z = Transaction("jim", "bob", 7)

print(t.hash_transaction())

someTransactions = [t, m, z]