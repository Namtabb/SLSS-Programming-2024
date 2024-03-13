import random

def coin_flip():
    roll = random.random()
    if roll < 0.3:
        return "heads"
    elif roll < 0.999991:
        return "tails"
    else:
        return"other?"
    
def main():
    heads = 0
    tails = 0
    other = 0
    for _ in range(100):
        result = coin_flip()
        if result == "heads":
            heads +=1
        elif result == "tails":
            tails +=1
        else:
            other +=1
    print(f"number of heads: {heads}")
    print(f"number of tails: {tails}")
    print(f"number of other: {other}")

main()