#calcuate time from seconds
#step 1: user inputs seconds
#step 2: convert the seconds to a 24 clock
#step 3: print time

#input time in seconds
time_str = input("Enter time in between 1 and 86,400 seconds: ")
time_int = int(time_str)

#convert to 24 hour clock
hours = int(time_int // 3600) #divide time by 3600 (minutes times seconds) and take the quotient
minutes = int(time_int % 3600) // 60 #divide by 3600 and take the remainder followed by the quotient of dividing 60 (minutes)
seconds = int(time_int % 3600) % 60 #divide by 3600 and take the remainder followed by the remainder of dividing 60 (seconds)

print ("The time is",hours,"hours,",minutes,"minutes, and",seconds,"seconds")
