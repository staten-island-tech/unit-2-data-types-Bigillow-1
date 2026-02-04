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




# dividing_number = 1
# number = int(input("Number to factor:"))
# factor = [1, number]
# for i in range(2,number):    
    
#     if number%i == 0 : 
#         factor.append(i)
#         print(factor)
        

#     else: 
#         continue



number = int(input("Number1 to factor:"))
number2 = int(input("Number2 to factor:"))
factors = []
loop = max(number, number2)
for p in range(loop):
    dividing_number = 1
    
    for i in range(2, number):    
        if number%i == 0 : 
            factors.append(i)
        else: 
            continue

    dividing_number2 = 1
    for o in range(2,number2):    
        
        if number2%o == 0 : 
            factors.append(o)       
        else: 
            continue
print("Done")
gcf = 0 
for factor in factors:
    if factor > gcf and number%factor == 0 and number2%factor == 0:
        gcf = factor

print(gcf)
