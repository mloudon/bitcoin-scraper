from django.db import models

class User (models.Model):
    userid=models.BigIntegerField()
    username = models.CharField(max_length=200,blank=True,null=True)
    profileurl = models.URLField(blank=True,null=True)
    numposts = models.IntegerField(blank=True,null=True)
    date_reg = models.DateField(blank=True,null=True)
    date_last = models.DateField(blank=True, null=True)

class Address (models.Model):
    val = models.CharField(max_length=34,unique=True)
    user = models.ForeignKey(User, blank=True,null=True)
    
class Block (models.Model):
    hash = models.CharField(max_length=1000, unique=True)
    created = models.DateField()
    
class Transaction (models.Model):
    hash = models.CharField(max_length=1000,unique=True)
    block = models.ForeignKey(Block, blank=True,null=True)
    
class Tx_input (models.Model):
    address = models.ForeignKey(Address)
    transaction = models.ForeignKey(Transaction)

class Tx_output (models.Model):
    address = models.ForeignKey(Address)
    amount = models.BigIntegerField()
    transaction = models.ForeignKey(Transaction)
    
class Net1_edge (models.Model):
    addr1 = models.CharField(max_length=34)
    addr2 = models.CharField(max_length=34)
    
class Net2_edge (models.Model):
    from_user = models.ForeignKey(User, related_name="user_from")
    to_user = models.ForeignKey(User,related_name="user_to")
    val = models.BigIntegerField()

