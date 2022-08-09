from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bidders = {}
people = True

# Adding people to bidders dictionary
while people == True:
    name = input("What is your name?") 
    price = input("What is your bid? $")
    bidders[name] = price

    new_person = input("Are there any other bidders? Type 'yes' or 'no' ")
    if new_person == "no":
        people = False
        # print(bidders)  Debug line
bids = []

# Adding bids to a list
for bid in bidders:
    bids.append(bidders[bid])

winPrice = max(bids)

# Matching the final price to the name
for name, dollar in bidders.items():
    if winPrice == winPrice:
        winPerson = name


print(f"The winning bidder is {winPerson} and bid {winPrice}!")