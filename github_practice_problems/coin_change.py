''' Cute Mistake: Permutations dont matter
Solution: Configuration.
Arbitrarily decide that between 1-1-2, and 2-1-1, favor 2-1-1.'''

def count_change(coins, amount, last_coin):
    if amount < 0:
        return 0
    if amount == 0:
        return 1
    acc = 0
    for coin_value in coins:
        if coin_value > last_coin:
            continue
        acc += count_change(coins, amount - coin_value, coin_value)
    return acc

if __name__=="__main__":
    c = [1,2,3]
    print count_change(c, 4, 3)
