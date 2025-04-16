print("Welcome to the tip calculator!");
bill = float(input("What was the total bill?: R$"));
tip_percentage = int(input("How much tip would you like to give?: %"));
ppl_amnt = int(input("How many people is going to pay (to split the bill)?: "));
pretotal = bill * (bill * tip_percentage / 100);
total = (pretotal / ppl_amnt);

print(f"You have to pay: R${total: .2f}");