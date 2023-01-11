import hashlib as h

def sha256(o):
  #The string inside update() is the string to be hashed
    #encode('utf-8')
      #utf-8 is a formatting for text - each character in this formatting is one byte, or 8 bits
        #you may have seen this in the top of the windows notepad app
      #so basically the encode function is turning the string into a utf-8 formatted string
  return h.sha256(o.encode('utf-8')).hexdigest() #this is the hash as a hexadecimal string, im guessing

def merkle(list):
  if (len(list) == 1):
    return list[0]
  new = [hash(list[x] + list[x+1]) for x in range(0, len(list) - 1, 2)]
  if (len(list) % 2 != 0):
    new.append(list[-1])
  return merkle(new)

class Block:
  #Constructor: initialize (create) a block given some parameters
    #The constructor sets a bunch of properties to those parameters
  #Example: myBlock = Block("data", 0, d.datetime.now(), None, 0)
  def __init__(self, transactions, timestamp):
    self.version = 0.0
    self.transactions = transactions
    self.index = 0
    self.previous = None
    self.nonce = 0
    self.difficulty = 3
    self.timestamp = timestamp
    self.hash = self.hash_block()
    
  #Returns the hash of the block
  def hash_block(self):
    #str() casts the instance data to strings
    self.merkle = merkle(map(sha256, self.transactions))
    return sha256(str(self.version) + str(self.timestamp) + str(self.previous) + str(self.merkle) + str(self.difficulty) + str(self.nonce)) 

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
      tran.out()
    print("HASH:", self.hash)
    print("NONCE:", self.nonce)
    print("PREVIOUS HASH:", self.previous)
    print("-----END BLOCK-----\n")