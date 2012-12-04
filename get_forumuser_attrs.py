import urllib2
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from bitcoinapp.models import User, Address

FILENAME = "/home/mel/Documents/2012-2013/COMM 645/paper/forum_addresses.txt"

users = []

def read_users_from_file():
    infile = open(FILENAME,"r")
    
    all_lines = infile.read().splitlines()
    infile.close()
    
    print 'input file has %d lines' % len(all_lines)
    
    for line in all_lines:
        data = line.split(",")
        
        users.append(data)
        

def get_attrs_for_address(addr, handle, profileurl):
    print "getting attributes for address %s" % addr
    
    url = profileurl
    
    try:
        profilehtml = urllib2.urlopen(url).read()
    except urlib2.HTTPError as e:
        print "error opening url %s %s" % (e.code,e.reason)
        
    soup = BeautifulSoup(profilehtml)
    
    tableofinterest = soup.find("td",class_="windowbg").find_all("td")
    
    if(tableofinterest[2].get_text().startswith("Posts:")):
        firstrow=3
    else:
        firstrow=5
    posts = tableofinterest[firstrow].get_text()
    date_reg_str = tableofinterest[firstrow+4].get_text()
    date_reg = datetime.strptime(date_reg_str, '%B %d, %Y, %I:%M:%S %p')
    date_last_str = tableofinterest[firstrow+6].get_text()
    
    if date_last_str.startswith("Today"):
        date_last = datetime.now()
    else:
        date_last = datetime.strptime(date_last_str, '%B %d, %Y, %I:%M:%S %p')
    
    try:
        address = Address.objects.get(val__exact=addr)
        user = address.user
        user.username=handle
        user.profileurl=profileurl
        user.numposts=posts
        user.date_reg=date_reg
        user.date_last=date_last
        user.save()
    
    except Address.DoesNotExist as d:
        print 'no address in database: %s ' %addr

def main():

    read_users_from_file()
        
    for user in users:
        addr = user[0]
        handle = user[1]
        url = user[2]
        get_attrs_for_address(addr,handle,url)
        sleep(1)
    

if __name__ == "__main__":
    main()
