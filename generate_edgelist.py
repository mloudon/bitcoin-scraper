from bitcoinapp.models import Net1_edge

FILENAME = "/home/mel/Documents/2012-2013/COMM 645/paper/edges_net1_v2.ncol"

def main():
    out = open(FILENAME,"w")
    for edge in Net1_edge.objects.all():
        out.write(edge.addr1+" "+edge.addr2+"\n")
        
    out.close()

if __name__ == "__main__":
    main()