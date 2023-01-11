from transaction import Transaction
from block import Block
from Crypto.PublicKey import RSA
import datetime as d


#The Blockchain is currently being stored as an array of blocks
class Blockchain:
  def __init__(self):
    #Here is the chain, which as you can see is initialized as an array with a single block inside of it
    #This block is self.add_genesis() (see the function add_genesis(self) for more info)
    self.chain = [self.add_genesis()] 
    self.pending = [self]

    #a set of keys of transacters; used to easily find if a generated key is a duplicate
    #feel free to change the name of this property as you see fit
    self.transacters = set()

  #This function returns the first block (genesis block) in the chain (hence the function is only going to be used once)
  def add_genesis(self):
    return Block([], d.datetime.now())

  #mines a block with current transactions and adds it to the chain
  def add_block(self, block):
    if (block.mine_block(1)):
      block.index = len(self.chain) + 1
      block.previous = self.chain[-1].hash
      self.chain.append(block)

      # add all the new transacters to the set of transacters
      for tran in block.transactions:
        self.transacters.update((tran.sender, tran.receiver))

  #to be explained
  def new_transaction(self, sender, receiver, amount, senderKey):
    senderKeyByte = senderKey.encode('ASCII')
    trans = Transaction(sender, receiver, amount)
    trans.sign_transaction(senderKey)

  def validate_transaction(self, signature, transaction):
    #pkcs1_15.new(key).verify(transaction, signature)
    pass


  def generateKeys(self):
    # The while loop makes sure the RSA key is not a duplicate of one used in the chain already
    keys = RSA.generate(2048)
    pub_key = keys.publickey().export_key()
    priv_key = keys.export_key()
    while pub_key not in self.transacters or priv_key not in self.transacters:
      keys = RSA.generate(2048)
      pub_key = keys.publickey().export_key()
      priv_key = keys.export_key()

    file_out = open("private.pem", "wb")
    file_out.write(priv_key)
    file_out = open("public.pem", "wb")
    file_out.write(pub_key)
    print(pub_key.decode('ASCII'))
    return pub_key.decode('ASCII')

  def out(self):
    for block in self.chain:
      block.out()