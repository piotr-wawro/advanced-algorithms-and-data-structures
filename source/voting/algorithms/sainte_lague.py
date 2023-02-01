def sainte_lague(party_votes: list[int], seats: int):
    party_seats = [0]*len(party_votes)
    party_quotient = [votes for votes in party_votes]

    allocated_seats = 0
    while allocated_seats < seats:
        max_quotient = max(party_quotient)
        max_quotient_idx = [idx for idx, quotient in enumerate(party_quotient)
                            if quotient == max_quotient]

        for idx in max_quotient_idx:
            allocated_seats += 1
            party_seats[idx] += 1
            party_quotient[idx] = party_votes[idx] / (2*party_seats[idx] + 1)

            if allocated_seats == seats:
                break

    return party_seats
