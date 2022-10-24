import hashlib as h
import datetime as d


class Block:

  def __init__(self, data, index, timestamp, previous):
    self.data = data
    self.index = index
    self.previous = previous
    self.nonce = 0
    self.timestamp = timestamp
    self.hash = self.hash_block()

  def hash_block(self):
    block_encryption = h.sha256()

    block_encryption.update(
      (str(self.index) + str(self.timestamp) + str(self.data) +
       str(self.previous) + str(self.nonce)).encode('utf-8'))

    return block_encryption.hexdigest()

  def mine_block(self, difficulty):
    while (self.hash[-difficulty:] != "".zfill(difficulty)):
      self.nonce += 1
      self.hash = self.hash_block()
    print('mined!')
    return True


class Blockchain:

  def __init__(self):
    self.chain = [self.add_genesis()]

  def add_genesis(self):
    return Block("data", 0, d.datetime.now(), None, 0)

  @staticmethod
  def add_block(last_block):
    index = last_block.index + 1


class Transaction(object):

  def __init__(self, sender, receiver, amount):
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
    self.time = d.now().strftime("%m/%d/%Y, %H:%M:%S")
    self.hash = self.hash_block()


g = Block("fdaksf", d.datetime.now(), 5, 5)
print(g.hash)

g.mine_block(5)
print(g.hash, g.nonce)
