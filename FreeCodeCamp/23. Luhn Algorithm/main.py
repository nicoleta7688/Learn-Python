def verify_card_number(card_nr):
    card_nr = card_nr.replace("-", '')
    card_nr = card_nr.replace(" ", '')
    
    to_double = False
    total_sum = 0

    for c in card_nr[::-1]:
        nr = int(c)
        if to_double: 
            nr *= 2
            to_double = False
        else:
            to_double = True

        if nr >= 10:
            nr -= 9
        
        total_sum += nr

    return "VALID!" if total_sum % 10 == 0 else "INVALID!"

print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('1234 5678 9012 3456'))