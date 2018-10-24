#calculate the price of an item with sale tax
#step 1: price from user
#step 2: the sale tax rate from user
#step 3: overall price

#input purchase price from user
price_str = input("Enter the purchase price: ")
price_float = float(price_str)

#input sale tax rate from use and convert to be in decimals
tax_rate_str = input("Enter the sale tax rate: ")
tax_rate_float = float(tax_rate_str)
tax_rate_float = float(tax_rate_float / 100) #divide by 100 to convert to decimals

#formulas to print total price
tax_float = (price_float) * (tax_rate_float) #find the amount of tax user pays
total_price = (tax_float) + (price_float) #add tax_float to purchase price

print ("The total price is:$",round(total_price,2), sep="") #sep= will remove space between $ and total price
