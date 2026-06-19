def main():
    card_type = None
    card_number = input("Card Number: ").strip()
    if not card_number.isdigit():
        print("Invalid")
        return
    card_type = check_card_type(card_number)

    if card_type and valid_number(card_number):
        print(card_type)
    else:
        print("Invalid")

# (name, length, prefixes, prefixlen)
CARD_TYPES = [
    ("American Express", {15},      {"34", "37"},                    2),
    ("MasterCard",       {16},      {"51","52","53","54","55"},    2),
    ("Visa",             {13, 16}, {"4"},                          1),
]

def check_card_type(card_number):
    length = len(card_number)
    for name, lengths, prefixes, plen in CARD_TYPES:
        if length in lengths and card_number[:plen] in prefixes:
            return name
    return None

def valid_number(card_number):
    total = 0
    for pos, number in enumerate(card_number[::-1]):
        if pos % 2 == 0:
            total += int(number)
        else:
            doubled = int(number) * 2
            total += doubled // 10 + doubled % 10
    return total % 10 == 0

if __name__ == "__main__":
    main()
