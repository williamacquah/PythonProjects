from art import logo
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
print(logo)
auction_dict = {}
moreUsers = True
while moreUsers is True:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    otherUser = input("Are there any other bidders? Type 'yes' ore 'no'.\n").lower()
    auction_dict[name] = bid
    if otherUser == "no":
        moreUsers = False
    else:
        moreUsers = True
        print("\n" * 100)
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
highestBid = 0
winner = ""
for name, bid in auction_dict.items():
    if bid > highestBid:
        highestBid = bid
        winner = name
print(f"The winner is {winner} with a bid of ${highestBid}.")