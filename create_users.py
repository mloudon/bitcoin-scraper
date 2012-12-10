from bitcoinapp.models import User, Address

FILENAME = "/home/mel/Documents/2012-2013/COMM 645/paper/nodes_2.txt"

def read_components_from_file():
    infile = open(FILENAME,"r")
    idcount=1
    
    all_lines = infile.read().splitlines()
    infile.close()
    
    print 'input file has %d lines' % len(all_lines)
    
    for line in all_lines:
        user = User.objects.create(userid=idcount)
        user.save()
        
        
        addresses = line.split(",")
        print '%d addresses for user %d' % (len(addresses),user.userid)
        for addrhash in addresses:
            #print addrhash
            addr=Address.objects.get(val__exact=addrhash)
            addr.user=user
            addr.save()
        
        idcount += 1

def create_users_for_orphan_addresses():
    orphans = Address.objects.filter(user__exact=None)
    idcount = User.objects.all().count()+1
    for address in orphans:
        user = User.objects.create(userid=idcount)
        user.save()
        address.user=user
        address.save()
        idcount+=1


def main():
    read_components_from_file()
    create_users_for_orphan_addresses()

if __name__ == "__main__":
    main()