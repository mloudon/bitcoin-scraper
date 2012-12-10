from bitcoinapp.models import Net2_edge, User

EDGELIST = "/home/mel/Documents/2012-2013/COMM 645/paper/edges_net2_forumusers_only.ncol"
NODEATTRS = "/home/mel/Documents/2012-2013/COMM 645/paper/attrs_forumusers.ncol"

def main():
    edgelist()
    attrs()
    
def edgelist():
    out1 = open(EDGELIST,"w")
    
    for edge in Net2_edge.objects.filter(val__lte=500000000):
        out1.write(("%d %d %d\n")%(edge.from_user.userid,edge.to_user.userid,edge.val))
        
    out1.close()
 
def attrs():   
    out2 = open(NODEATTRS,"w")
    for user in User.objects.all():
        if user.numposts:
            out2.write((("%d\t%d\t%s\n")%(user.userid,user.numposts,unicode(user.username))).encode("utf-8"))
            
    out2.close()

if __name__ == "__main__":
    main()