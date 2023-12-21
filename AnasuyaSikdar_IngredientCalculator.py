# Assignment 1_2
# Anasuya Sikdar

#Input the number of cookies that the baker would like to make
numNewCookies = eval(input('Enter the number of cookies: '))

#Original Cookie Quantity
numOldCookies = 48

#Define constants for ingredient quantities for 48 cookies
sugar_48 = 1.5
butter_48 = 1.0
flour_48 = 2.75

#Calculations to adjust the quantity of each ingredient
adjusted_sugar = (sugar_48 * numNewCookies)/numOldCookies
adjusted_butter = (butter_48 * numNewCookies)/numOldCookies
adjusted_flour = (flour_48 * numNewCookies)/numOldCookies

#Output of the Results Calculated
print('To make ',numNewCookies,' cookies use:')
print(round(adjusted_sugar,2),' cups of sugar')
print(round(adjusted_butter,2),' cups of butter')
print(round(adjusted_flour,2),' cups of flour')

#Test Case 1
#For 12 cookies as input(less than 48 cookies)
#The adjusted sugar would be = (1.5 * 12)/48 = 0.375
#The adjusted butter required = (1.0 * 12)/48 = 0.25
#The adjusted flour required = (2.75 * 12)/48 = 0.6875


#Test Case 2
#For 60 cookies as input(more than 48 cookies)
#The adjusted sugar would be = (1.5 * 60)/48 = 1.875
#The adjusted butter required = (1.0 * 60)/48 = 1.25
#The adjusted flour required = (2.75 * 60)/48 = 3.4375
