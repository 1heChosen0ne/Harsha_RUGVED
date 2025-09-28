def luhn_check(card_number):
    total = 0
    num_digits = len(card_number)
    parity = num_digits % 2
    for i, digit in enumerate(card_number):
        d = int(digit)
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0
card = input("Enter credit card number: ")
if luhn_check(card):
    print("Valid card number")
else:
    print("Invalid card number")
