""" BATTLE SIMULATION

https://open.kattis.com/problems/battlesimulation

by Michael Welsh
"""

counters = {
    "R": "S",
    "B": "K",
    "L": "H",
}

if __name__ == "__main__":
    moves = input()
    counter_moves = []
    count = 0
    for idx, move in enumerate(moves):
        if len(set(moves[idx: idx + 3])) == 3 and count == 0:
            counter_moves.append("C")
            count = 3

        if count > 0:
            count -= 1
            continue

        counter_moves.append(counters[move])

    print("".join(counter_moves))
        
