#Anasuya Sikdar
#Assignment 6.1

def contacts():
    contact_dict = {}  # Dictionary to hold contacts
    
    while True:
        firstName = input("Enter first name: ")
        
        # Break loop if user hits enter without input
        if not firstName.strip():
            # Print the dictionary sorted by last name and exit
            for key in sorted(contact_dict.keys()):
                print(f"{key[0]}, {key[1]}: {contact_dict[key]}")
            return
        
        lastName = input("Enter last name: ")
        key = (lastName, firstName)  # Tuple to store last name and first name

        # Check if the contact (tuple) already exists in the dictionary
        if key not in contact_dict:
            phoneNumber = input("Enter 10-digit phone number 9999999999: ")
            formattedNumber = f"{phoneNumber[:3]}-{phoneNumber[3:6]}-{phoneNumber[6:]}"  # Formatting the number with hyphens
            contact_dict[key] = {formattedNumber}  # Store phone numbers
        else:
            print(f"Phone numbers for {firstName} {lastName}: {contact_dict[key]}")
            addAnother = input("Do you want to enter another phone number? (yes/no) ")
            if addAnother.lower() == 'yes':
                phoneNumber = input("Enter another 10-digit phone number 9999999999: ")
                formattedNumber = f"{phoneNumber[:3]}-{phoneNumber[3:6]}-{phoneNumber[6:]}"  # Formatting the number with hyphens
                contact_dict[key].add(formattedNumber)  # Add the new number to the set of existing numbers

# Test
contacts()
