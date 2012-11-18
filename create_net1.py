from bitcoinapp.models import Transaction, Net1_edge, Tx_input

def main():
    for tx in Transaction.objects.all():
        for tx_in1 in tx.tx_input_set.all():
            addr1 = tx_in1.address.val
            for tx_in2 in tx.tx_input_set.all():
                addr2=tx_in2.address.val
                if addr1!=addr2:
                    e = Net1_edge.objects.create(addr1=addr1,addr2=addr2)
                    e.save()


if __name__ == "__main__":
    main()