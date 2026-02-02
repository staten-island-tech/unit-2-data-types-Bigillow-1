# number = input("Is this number even or odd?")
# number = int(number)%2
# if number == 1:
#     print("Odd")
# else:
#     print("Even")





# bill = input("How much is the bill?")
# service = input("Is the service bad, okay, good , or great?")
# service = service.lower()
# if service == "bad":
#     bill = int(bill)+(int(bill)*0)
#     bill = "$" + str(bill)
#     print(bill)
# elif service == "okay":
#     bill = int(bill)+(int(bill)*0.15)
#     bill = "$" + str(bill)
#     print(bill)
# elif service == "good":
#     bill = int(bill)+(int(bill)*0.2)
#     bill = "$" + str(bill)
#     print(bill)
# elif service == "great":
#     bill = int(bill)+(int(bill)*0.25)
#     bill = "$" + str(bill)
#     print(bill)

number = input("Number to factor:")
for i in range(21):
    factor = []
    dividing_number = 1
    
    number = int(number)%dividing_number
    if number == 0: 
        factor.apend(dividing_number)
        dividing_number += 1
    elif number == 1:
        continue
    print(factor)

    



