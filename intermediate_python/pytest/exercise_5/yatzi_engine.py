def dice_counts(dice):
    return {x:dice.count(x) for x in range(1,6)}

def full_house(dice):
    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.vvalues():
        return sum(dice)
    return 0

if __name__ == "__main__":
    full_house([5,5,6,6,6,])