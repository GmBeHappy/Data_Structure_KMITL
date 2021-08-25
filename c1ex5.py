bids = [int(x) for x in input("Enter All Bid : ").split()]

if(len(bids)<=1):
    print("not enough bidder")
else:
    bids.sort(reverse=True)
    if(bids[0]==bids[1]):
        print("error : have more than one highest bid")
    else:
        print("winner bid is {} need to pay {}".format(bids[0],bids[1]))
