
#Homework Assignment 2.2
#Submission Date : 09/19/2023
#Anasuya Sikdar

#The club charges for monthly membership
membership_plan = ['Standard adult','Child(age 12 and under)','Student','Senior Citizen(age 65 and over)']
monthly_plan_fees = [40.00, 20.00, 25.00, 30.00]

# The club's optional services and monthly additional fees
optional_services = ['No lessons','Yoga lessons','Personal trainer','Yoga and Personal trainer']
optional_services_fees = [0.00, 10.00, 50.00, 60.00]

#User input to choose the membership plan and optional plan, as well as the duration of membership
membership_type = int(input('Enter number of membership type 1 - 4: '))
idx1 = int(membership_type)
optional_service_type = int(input('Enter number of optional service 0 - 3: '))
idx2 = int(optional_service_type)
month = int(input('Enter the number of months: '))

#Calculate the discounts based on the months of membership plan
if membership_type < 1 or membership_type > 4 or optional_service_type < 0 or optional_service_type > 3 or month < 1:
   print('Invalid number entered. Please enter a valid value')
else:
   if 1 <= month <= 3:
       discount = 0.00
   elif 4 <= month <=6:
       discount = 0.05
   elif month>=7 and month<=9:
       discount = 0.08
   else:
       discount = 0.10

   #Calculate the monthly fee
   monthly_fee = monthly_plan_fees[idx1-1] + optional_services_fees[idx2]
   #add the discount on the monthly fee
   monthly_fee_discount = monthly_fee - monthly_fee * discount

   #Calculate the total fee
   total_fee = (monthly_plan_fees[idx1-1] + optional_services_fees[idx2]) * month
   #add the discount on the total fee
   total_fee_discount = total_fee - total_fee * discount

   #Outputs
   print(membership_plan[idx1-1],' with ',optional_services[idx2],' for ',month ,' months')
   print('Monthly Fee is ',monthly_fee_discount,' dollars')
   print('Total ',total_fee_discount,' dollars' )

   #Free drink
   if optional_service_type!=0:
      free_drink_code = membership_type * 1000 + optional_service_type * 100 + month
      print('Redeem your free drink at the juice bar using code: ',free_drink_code)
        

    
