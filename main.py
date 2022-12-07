import hashlib as h
import datetime as d
from Crypto.PublicKey import RSA

def sha256(o):
  #The string inside update() is the string to be hashed
    #encode('utf-8')
      #utf-8 is a formatting for text - each character in this formatting is one byte, or 8 bits
        #you may have seen this in the top of the windows notepad app
      #so basically the encode function is turning the string into a utf-8 formatted string
  return h.sha256(o.encode('utf-8')).hexdigest() #this is the hash as a hexadecimal string, im guessing

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
  def __init__(self, transactions, timestamp):
    self.transactions = transactions
    self.index = 0
    self.previous = None
    self.nonce = 0
    self.timestamp = timestamp
    self.hash = self.hash_block()
    
  #Returns the hash of the block
  def hash_block(self):
    #str() casts the instance data to strings
    return sha256(str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous) + str(self.nonce)) 

  #a function for mining the block
  def mine_block(self, difficulty):
    #The while loop keeps hashing the block with a different nonce value until the block's hash satisfies some condition given by the difficulty value
    #after the loop finishes
    while (self.hash[-difficulty:] != "".zfill(difficulty)):
      self.nonce += 1
      self.hash = self.hash_block()
      
    return True

  def out(self):
    print("-----BEGIN BLOCK", str(self.index) + "-----")
    print("TIME:", self.timestamp)
    print("TRANSACTIONS:")
    for tran in self.transactions:
      print(tran)
    print("HASH:", self.hash)
    print("NONCE:", self.nonce)
    print("PREVIOUS HASH:", self.previous)
    print("-----END BLOCK-----\n")


#The Blockchain is currently being stored as an array of blocks
class Blockchain:
  def __init__(self):
    #Here is the chain, which as you can see is initialized as an array with a single block inside of it
      #This block is self.add_genesis() (see the function add_genesis(self) for more info)
    self.chain = [self.add_genesis()] 
    self.pending = [self]

  #This function returns the first block (genesis block) in the chain (hence the function is only going to be used once)
  def add_genesis(self):
    return Block([], d.datetime.now())

  #mines a block with current transactions and adds it to the chain
  def add_block(self, block):
    if (block.mine_block(1)):
      block.index = len(self.chain) + 1
      block.previous = self.chain[-1].hash
      self.chain.append(block)

  #to be explained
  def newTransaction(self, sender, receiver, amt, senderKey):
    senderKeyByte = senderKey.encode('ASCII')

  def generateKeys(self):
    # Makes sure the RSA key is not a duplicate of one used in the chain already
    
    flag = False
    while flag == False:
      keys = RSA.generate(2048)
      pub_key = keys.publickey().export_key()
      priv_key = keys.export_key()
      flag = True
      for block in self.chain:
        print(block)
        for tran in block.transactions:
          if tran.sender == pub_key or tran.receiver == pub_key:
            flag = False

    file_out = open("private.pem", "wb")
    file_out.write(priv_key)
    file_out = open("public.pem", "wb")
    file_out.write(pub_key)
    print(pub_key.decode('ASCII'))
    return pub_key.decode('ASCII')

  def out(self):
    for block in self.chain:
      block.out()
    

class Transaction(object):
  def __init__(self, sender, receiver, amount):
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
    self.time = d.datetime.now()
    self.hash = self.hash_transaction()
  
  def hash_transaction(self):
    return sha256(str(self.sender) + str(self.receiver) + str(self.amount) + str(self.time))
  
  def signTransaction(self, keys, senderKey):
    if self.hash != self.hash_transaction:
        print("transaction tamper")
        return False
    if senderKey.publickey().export_key() != str(keys.publickey().export_key()):
        print("transaction signed by different wallet")
        return False
    
    def out():
      pass


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