import math

def hare_niemeyer(party_votes: list[int], seats: int):
    total_votes = sum(party_votes)
    party_quotient = [votes*seats/total_votes for votes in party_votes]
    party_seats = [math.floor(quotient) for quotient in party_quotient]

    remainder = [quotient % 1 for quotient in party_quotient]
    idx_of_sorted_remainder = [idx for _, idx in sorted(zip(remainder, range(len(remainder))), reverse=True)]

    allocated_seats = sum(party_seats)
    for i in range(seats - allocated_seats):
        party_seats[idx_of_sorted_remainder[i]] += 1

    return party_seats
