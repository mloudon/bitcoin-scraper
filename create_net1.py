from bitcoinapp.models import Transaction, Net1_edge, Tx_input

def main():
    count = 1;
    txset = Transaction.objects.all()
    numtx = len(txset)
    for tx in txset:
        print("linking inputs for tx %s - %d of %d" % (tx.hash,count,numtx))
        inputs = tx.tx_input_set.all()
        for i in range(0,len(inputs)-1):
            addr1 = inputs[i].address.val
            if (i+1<len(inputs)):
                addr2 = inputs[i+1].address.val
                e = Net1_edge.objects.create(addr1=addr1,addr2=addr2)
                e.save()
        count +=1


if __name__ == "__main__":
    main()