from main import sha256
from Crypto.Signature import pkcs1_15
import datetime as d


class Transaction(object):
  def __init__(self, sender, receiver, amount, signature: str = ""):
    self.sender = sender
    self.receiver = receiver
    self.amount = amount
    self.time = d.datetime.now()
    self.hash = self.hash_transaction()
    self.signature = signature
  
  def hash_transaction(self):
    return sha256(str(self.sender) + str(self.receiver) + str(self.amount) + str(self.time))
  
  def sign_transaction(self, keys, senderKey):
    if self.hash != self.hash_transaction:
        print("transaction tamper")
        return False
    if senderKey.publickey().export_key() != str(keys.publickey().export_key()):
        print("transaction signed by different wallet")
        return False
    signature = pkcs1_15.new(senderKey).sign(self.hash_transaction())
    self.signature = signature
    
  def out(self):
    print("SENDER:", self.sender)
    print("RECEIVER", self.receiver)
    print("TIME:", self.time)
    print("AMOUNT", self.amount)
    print("HASH", self.hash)
    print("SIGNATURE", self.signature)