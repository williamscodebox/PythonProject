def find_poker_hand(hand):

    ranks = []
    suits = []

    for card in hand:
        if len(card) ==2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]
        if rank == 'A':
            rank = 14
        elif rank == 'K':
            rank = 13
        elif rank == 'Q':
            rank = 12
        elif rank == 'J':
            rank = 11
        else: rank = int(rank)  # handles 2–10

        print(rank, suit)
        ranks.append(rank)
        suits.append(suit)

    sorted_ranks = sorted(ranks)
    print(sorted_ranks)

    # Royal Flush
    if suits.count(suits[0]) == 5:
        print("Flush")
    else:
        print("Mix")


    print(hand)
    return 0

if __name__ == '__main__':
    find_poker_hand(["AH","KH","QH","JH","10H"]) # Royal Flush
    find_poker_hand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush

