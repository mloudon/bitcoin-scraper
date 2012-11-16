import urllib2
import json
import datetime
from time import sleep
from bitcoinapp.models import Block

BLOCK_URL = "http://blockchain.info/blocks/"
TRANSACTION_URL = "http://blockchain.info/rawtx/"

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
        block = Block.objects.create(hash=blockdata["hash"])
        print "block with hash %s" % block.hash
        block.save()
    

def main():

    STARTDATE=datetime.datetime(2011,5,1,0,0,0)

    fetchdate = STARTDATE

    while fetchdate.month == 5 and fetchdate.day <= 2:
        print "getting blocks for date %s - in millis %d" % (fetchdate, unix_time_millis(fetchdate))
        get_blocks_for_date(fetchdate)
        fetchdate += datetime.timedelta(days=1)
        sleep(1)


if __name__ == "__main__":
    main()
