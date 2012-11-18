from bitcoinapp.models import Transaction, Net2_edge, Tx_input, Tx_output, User, Address

def main():
    for tx in Transaction.objects.all():
        for tx_in in tx.tx_input_set.all():
            user1 = tx_in.address.user
            for tx_out in tx.tx_output_set.all():
                user2=tx_out.address.user
                amount=tx_out.amount
            


if __name__ == "__main__":
    main()