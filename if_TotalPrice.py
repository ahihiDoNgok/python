#calculate the price of an item with sale tax
#step 1: price from user
#step 2: check price is positive and continue for sale tax
#step 3: input sale tax rate from user
#step 4: if sale tax is postive, add formula and print total price
#step 5: if purchase price or sale tax is negative, use else to tell user calculation is not possible

#input purchase price from user
price_float = float(input("Enter the purchase price: "))

if price_float > 0:
    #input sale tax
    tax_rate_float = float(input("Enter the sale tax rate: "))

    if tax_rate_float > 0:

        #formulas to print total price
        tax_rate_float = float(tax_rate_float / 100) #divide by 100 to convert to decimals
        tax_float = (price_float) * (tax_rate_float) #find the amount of tax user pays
        total_price = (tax_float) + (price_float) #add tax_float to purchase price

        print ("The total price is:$",round(total_price,2), sep="") #sep= will remove space between $ and total price
    else:
        print("Cannot have negative sale tax")
else:
    print("Cannot have negative price")
