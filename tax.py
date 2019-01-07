def total_tax(price, rate): #you can repeat variable names and they wont matter
    total = price * rate/100
    return total

def total_price(price, rate):
    tax_results = total_tax(price, rate) #making a call to function total_tax and passing it through and storing the results in a variable
    end_price = price + tax_results
    return end_price

#main 
p = float(input("Price: "))
t = float(input("Tax: "))

overall_price = total_price(p, t)
print("Your total price is: ", round(overall_price, 2))
