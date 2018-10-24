#calculate celsuis to fahrenheit
#step 1: celsuis from user
#step 2: formula from celsuis to fahrenheit
#step 3: print fahrenheit

#input celsuis from user
celsuis_str = input("Enter temperature in Celsuis: ")
celsuis_float = float(celsuis_str)

#formula to covert celsuis to fahrenheit
fahrenheit = celsuis_float * (9 / 5) + 32

#print statement to the user
print ("The temperature in Fahrenheit is:",fahrenheit,"degrees")
