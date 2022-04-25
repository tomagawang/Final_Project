from pprint import pprint

def offer():
    '''A negotiation game that simulates a standard negotiation where the buyers have to make strategic 
    offers in order to win the game.'''
    deal = 0
    seller_offer = 1450000
    minimum_offer = 1100000
    buyer_offer = 900000
    while seller_offer-buyer_offer > 50000:
        offer = int(input("Here is my counteroffer(enter a offer number): $ "))
        if offer < 1250000:
            if offer/buyer_offer > 1.05:
                buyer_offer = offer
                if seller_offer > minimum_offer:
                    seller_offer *= 0.95
                if seller_offer-buyer_offer > 50000:
                    print(f"Seller responds: sorry, your offer is too low. I can do ${seller_offer}.")
            else:
                return print("Seller: sorry, I can't do this deal. The Seller walked away because your offer was not good enough.")
        else:
            return print("You can't pay this much, so you walked away.")
    if offer >= minimum_offer:
        deal = 1
        print(f"Seller says: That is a deal, we will sell the plant to you for ${buyer_offer}.")
    return deal

def no_deal():
    pprint("After the negotiation ended, your team suggest you to talk with the board and ask for more money to strike the deal, or you can sit out and wait for a response from the seller(they may not response).")
    pprint('A: ask for more money from the board; B: wait for seller to respond.')
    answer = input('Type your answer here(A or B):').lower()
    if answer == "a":
        pprint('The board agrees to give you more money, but they are not very happy with your decision.')
        return 0
    elif answer == 'b':
        pprint('The seller comes back and says they have talked with the headquarter and they are willing to sell the plant at your offerring price. After the negotiation, your associates congrat you on striking the deal and they are sure that the board will give you a raise and promotion soon. The current CEO is retiring soon, you are the right person to fill that position.')
        return 1
    else:
        pprint("please type A or B")
        no_deal()


def yes_deal():
    pprint("After the negotiation, your associates congrat you on striking the deal and they are sure that the board will give you a raise and promotion soon. The current CEO is retiring soon, you are the right person to fill that position.")


def main():
    pass


if __name__ == '__main__':

    main()