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

        # Straight Flush
        elif all(sorted_ranks[i] + 1 == sorted_ranks[i + 1] for i in range(4)): possible_ranks.append(9)

        #Flush
        else:
            possible_ranks.append(6)
    else: possible_ranks.append(1)

    # Four Of A Kind
    if any(ranks.count(rank) == 4 for rank in ranks): possible_ranks.append(8)

    # Full House
    unique = set(ranks)

    has_three = any(ranks.count(rank) == 3 for rank in unique)
    pairs = [rank for rank in unique if ranks.count(rank) == 2]
    pair_count = len(pairs)

    if has_three and pair_count >= 1:
        possible_ranks.append(7)

    # Straight
    if all(sorted_ranks[i] + 1 == sorted_ranks[i + 1] for i in range(4)): possible_ranks.append(5)

    # Three Of A Kind
    if has_three:
        possible_ranks.append(4)

    # Two Pair
    if pair_count > 1:
        possible_ranks.append(3)

    # One Pair
    if pair_count == 1:
        possible_ranks.append(2)

    if not possible_ranks:
        possible_ranks.append(1)

    # print(hand)
    output = poker_hand_ranks[max(possible_ranks)]
    print(poker_hand_ranks[max(possible_ranks)])
    return output

if __name__ == '__main__':
    find_poker_hand(["AH","KH","QH","JH","10H"]) # Royal Flush
    find_poker_hand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    find_poker_hand(["QC", "JC", "2C", "9C", "8C"])  # Flush
    find_poker_hand(["KC", "KD", "KS", "KH", "8C"])  # Four Of A Kind
    find_poker_hand(["QC", "QD", "QS", "9C", "9D"])  # Full House
    find_poker_hand(["QC", "JD", "10C", "9C", "8C"])  # Straight
    find_poker_hand(["QC", "QD", "QS", "9C", "2C"])  # Three Of A Kind
    find_poker_hand(["QC", "QD", "10C", "10D", "2C"])  # Two Pair
    find_poker_hand(["QC", "QD", "10C", "9C", "2C"])  # One Pair
    find_poker_hand(["QC", "JD", "10C", "9C", "2C"])  # High Card
