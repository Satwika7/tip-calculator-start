#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = input("what is the total bill\n$")
tip = input("what is the tip percentage\n%")
no_of_members = input("how many members\n$")
bill_new = float(bill)
tip_new = float(tip)
no_of_members_new = int(no_of_members)
tip_value = (bill_new*tip_new)/100
final_bill = bill_new+tip_value
bill_for_each = round(final_bill/no_of_members_new,2)
print(f"final bill for each of them is ${bill_for_each}")
#print("{.2f}".format(bill_for_each))