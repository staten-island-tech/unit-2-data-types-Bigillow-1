def discount(age, isMember, isResident):
    if (age < 12 or age > 64) and (isResident or isMember):
        return "Yes discount"
    else:
        return "no discount"


print(discount(190, True, False))

print(discount(28, True, False))