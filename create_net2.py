from bitcoinapp.models import Transaction, Net2_edge, Tx_input, Tx_output, User, Address

def main():
    total_tx=Transaction.objects.all().count()
    i = 1
    for tx in Transaction.objects.all():
        print "transaction %d with hash %s of %d" % (i, tx.hash, total_tx)
        if len(tx.tx_input_set.all())>0:
            tx_in = tx.tx_input_set.all()[0]
            
            #assume all inputs have the same user since this is how users were created
            user1 = tx_in.address.user
            for tx_out in tx.tx_output_set.all():
                user2=tx_out.address.user
                amount=tx_out.amount
                
                edge,created = Net2_edge.objects.get_or_create(from_user=user1,to_user=user2,defaults={"val":0})
                edge.val+= amount
                
                edge.save()
            i+=1
            

if __name__ == "__main__":
    main()