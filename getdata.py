import urllib2
import json
import datetime
from time import sleep
from bitcoinapp.models import Block, Transaction, Tx_input, Tx_output, Address

BLOCK_URL = "http://blockchain.info/blocks/"
TRANSACTION_URL = "http://blockchain.info/rawblock/"

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0

def get_blocks_for_date(d):
    url = BLOCK_URL + ("%d"%unix_time_millis(d)) + "?format=json"
    blocksjson = urllib2.urlopen(url).read()
    blocksarr = json.loads(blocksjson)
    
    for blockdata in blocksarr["blocks"]:
        block = Block.objects.create(hash=blockdata["hash"], created=d)
        print "block with hash %s" % block.hash
        block.save()
        
def get_tx_for_block(hash):
    curblock = Block.objects.get(hash=hash)
    print "getting transactions for block %s" % curblock.hash
    
    url = TRANSACTION_URL + ("%s"%hash)
    
    try:
        txjson = urllib2.urlopen(url).read()
    except urlib2.HTTPError as e:
        print "error opening url %s %s" % (e.code,e.reason)
    
    txarr = json.loads(txjson)
    
    for txdata in txarr["tx"]:
        tx=Transaction.objects.create(hash=txdata["hash"],block=curblock)
        tx.save()
        
        for tx_in in txdata["inputs"]:
            if len(tx_in)>0:
                addrtxt = tx_in["prev_out"]["addr"]
                addr,created = Address.objects.get_or_create(val=addrtxt)
                if (created):
                    addr.save()
            
                input = Tx_input.objects.create(address=addr,transaction=tx)
                input.save()
            
        for tx_out in txdata["out"]:
            if "addr" in tx_out:
                addrtxt = tx_out["addr"]
                addr,created = Address.objects.get_or_create(val=addrtxt)
                if (created):
                    addr.save()
                
                output = Tx_output.objects.create(address=addr,amount=tx_out["value"],transaction=tx)
                output.save()    
    

def main():

    STARTDATE=datetime.datetime(2011,5,1,0,0,0)

    fetchdate = STARTDATE

    '''
    while fetchdate.month == 5:
        print "getting blocks for date %s - in millis %d" % (fetchdate, unix_time_millis(fetchdate))
        get_blocks_for_date(fetchdate)
        fetchdate += datetime.timedelta(days=1)
        sleep(1)
    '''
        
    for block in Block.objects.filter(id__gt=6520):
        get_tx_for_block(block.hash)
        sleep(1)
    

if __name__ == "__main__":
    main()
