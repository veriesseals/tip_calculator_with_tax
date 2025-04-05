# Print Welcome to tip calculator
# ----------------------------------------------------

greeting = "Welcome to the tip calculator "
print(greeting)

# Define input to take in the input for the total bill from user
# ----------------------------------------------------

total_bill = float(input("Enter total bill "))
print('${:,.2f}'.format(total_bill))

# Define input to take in the tip amount percentage from user
# ----------------------------------------------------

tip_amount = int(input("Please enter percentage of your tip: "))
print(f"Your tip amount is: {tip_amount} %")

# Change tip amount to decimal
# ----------------------------------------------------

tip_percentage = tip_amount / 100
# print(tip_percentage)

# Total bill x tip_percentage for amount of tip
# ----------------------------------------------------
amount_of_tip = total_bill * tip_percentage
print("This is the amount of your tip that goes to your waitress/waiter: ", '${:,.2f}'.format(amount_of_tip))

# Calculate total_bill plus tip_amount
# ----------------------------------------------------

total_bill = total_bill + amount_of_tip
print("This is your total bill with tip: ", '${:,.2f}'.format(total_bill))


# Lets calculate some tax!
# ----------------------------------------------------
tax_amount = total_bill * .07
print("Your Mississippi State Tax amount is: 7%")
print("This will be your tax amount for this transaction: ", '${:,.2f}'.format(tax_amount))

total_bill = total_bill + tax_amount
print("This will be your bill with tax added: ", '${:,.2f}'.format(total_bill))

# Enter number of users to split the bill
# ----------------------------------------------------

num_of_guest_to_split = int(input("Enter number of guest "))
print(num_of_guest_to_split)

# each person should pay
# ----------------------------------------------------

each_should_pay = total_bill / num_of_guest_to_split
print("Each guest should pay: " '${:,.2f}'.format(each_should_pay))






