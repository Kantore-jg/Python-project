import replit
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
        elif bid_amount==highest_bid:
            print("y'all are the looser, coz you have the same price")
    print(f"the winner is {winner} with bid of ${highest_bid}")
dict={}
while True:
    name=input("enter your name: ")
    bid=float(input("enter your price now: "))
    dict[name]=bid
    #dict={name:bid}
    next=input("there are any other user who want to bid? yes to continue or no for break: ").lower()
    if next=="yes":
        clear()
        continue
    elif next=="no":
        find_highest_bidder(dict)
        break
    else:
        print("plz enter a correct answer")


