def main():
    while True:
        try:
            change = float(input("Change: "))
            if change < 0:
                print("Change can not be negative!")
            else:
                break
        except ValueError:
            print("Change must be a Number")
    change *= 100
    quarters = calc_quarters(change)
    change -= quarters * 25

    nickel = calc_nickel(change)
    change -= nickel * 10

    dimes = calc_dimes(change)
    change -= dimes * 5

    print(f"Quarters: {quarters}")
    print(f"Nickel: {nickel}")
    print(f"Dimes: {dimes}")
    print(f"Pennies: {int(change)}")
    print(f"Total: {int(quarters + nickel + dimes + change)}")


def calc_quarters(cents: int):
    count = 0
    while cents >= 25:
        count += 1
        cents -= 25
    return count

def calc_nickel(cents: int):
    count = 0
    while cents >= 10:
        count += 1
        cents -= 10
    return count

def calc_dimes(cents: int):
    count = 0
    while cents >= 5:
        count += 1
        cents -= 5
    return count

main()
