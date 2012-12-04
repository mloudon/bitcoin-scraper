import urllib2
import json
from time import sleep
from bitcoinapp.models import Transaction, Tx_input, Tx_output, Address

TRANSACTION_FOR_ADDRESS_URL = "http://blockchain.info/address/"

FILENAME = "/home/mel/Documents/2012-2013/COMM 645/paper/forum_addresses_2.txt"

addresses = []

def read_addresses_from_file():
    infile = open(FILENAME,"r")
    
    all_lines = infile.read().splitlines()
    infile.close()
    
    print 'input file has %d lines' % len(all_lines)
    
    for line in all_lines:
        data = line.split(",")
        addr = data[0]
        addresses.append(addr)
        
        handle = data[1]
        url = data [2]
        

def get_tx_for_address(addr):
    print "getting transactions for address %s" % addr
    
    url = TRANSACTION_FOR_ADDRESS_URL + ("%s?format=json" % addr)
    
    try:
        txjson = urllib2.urlopen(url).read()
    except urlib2.HTTPError as e:
        print "error opening url %s %s" % (e.code,e.reason)
    
    txarr = json.loads(txjson)
    
    for txdata in txarr["txs"]:
        tx, created=Transaction.objects.get_or_create(hash=txdata["hash"])
        if (created):
            tx.save()
        
        for tx_in in txdata["inputs"]:
            if len(tx_in)>0:
                addrtxt = tx_in["prev_out"]["addr"]
                address,created = Address.objects.get_or_create(val=addrtxt)
                if (created):
                    address.save()
            
                input = Tx_input.objects.create(address=address,transaction=tx)
                input.save()
            
        for tx_out in txdata["out"]:
            if "addr" in tx_out:
                addrtxt = tx_out["addr"]
                address,created = Address.objects.get_or_create(val=addrtxt)
                if (created):
                    address.save()
                
                output = Tx_output.objects.create(address=address,amount=tx_out["value"],transaction=tx)
                output.save()    
    

def main():

    read_addresses_from_file()
        
    for addr in addresses:
        get_tx_for_address(addr)
        sleep(1)
    

if __name__ == "__main__":
    main()
