def find_poker_hand(hand):

    poker_hand_ranks = {10: "Royal Flush", 9: "Straight Flush", 8: "Four Of A Kind", 7: "Full House", 6: "Flush",
                        5: "Straight", 4: "Three Of A Kind", 3: "Two Pairs", 2: "One Pair", 1: "High Card",
                        0: "No Hand Currently Defined in Function Definition"}
    ranks = []
    suits = []
    possible_ranks = []

    print("")

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
    # print(sorted_ranks)

    # Royal Flush
    if suits.count(suits[0]) == 5:
        if 14 in sorted_ranks and 13 in sorted_ranks and 12 in sorted_ranks and 11 in sorted_ranks and 10 in sorted_ranks:
            # print("Royal Flush")
            possible_ranks.append(10)
        # print("Flush")
        possible_ranks.append(0)
    else:
        print("")
        # print("Mix")

    # print(hand)
    print(poker_hand_ranks[max(possible_ranks)])
    return 0

if __name__ == '__main__':
    find_poker_hand(["AH","KH","QH","JH","10H"]) # Royal Flush
    find_poker_hand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush

