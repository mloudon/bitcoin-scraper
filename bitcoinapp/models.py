from django.db import models

class Address (models.Model):
    val = models.CharField(max_length=34,null=True,blank=True)
    
class Block (models.Model):
    hash = models.CharField(max_length=1000, null=True,blank=True)
    
class Transaction (models.Model):
    hash = models.CharField(max_length=1000,null=True,blank=True)
    block = models.ForeignKey(Block)
    
class Tx_input (models.Model):
    address = models.ForeignKey(Address)
    amount = models.BigIntegerField()
    transaction = models.ForeignKey(Transaction)

class Tx_output (models.Model):
    address = models.ForeignKey(Address)
    amount = models.BigIntegerField()
    transaction = models.ForeignKey(Transaction)
