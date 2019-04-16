# Write a function `is_leap_year` that takes a year as a parameter
#   -->**RETURNS**<-- True if the year is a leap year, False otherwise.
# The logic-chain is somewhat similar to the Sherlock problem.

# Don't forget to reach out for help after your own due diligence

year = int()

def is_leap(year):
    if year % 100 == 0 and year % 400 == 0: 
       return True
    elif year % 100 != 0 and year % 4 == 0:
       return True 
    else: 
       return False
 

print(is_leap(year))
