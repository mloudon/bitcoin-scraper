from bitcoinapp.models import Net2_edge

FILENAME = "/home/mel/Documents/2012-2013/COMM 645/paper/edges_net2.ncol"

def main():
    out = open(FILENAME,"w")
    for edge in Net2_edge.objects.all():
        out.write(("%d %d %d\n")%(edge.from_user.userid,edge.to_user.userid,edge.val))
        
    out.close()

if __name__ == "__main__":
    main()