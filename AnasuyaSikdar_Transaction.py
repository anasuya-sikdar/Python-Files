#Assignment5.2
#Anasuya Sikdar

def budget(lst):
    og_budget = sum(lst)  
    print(f"Transactions: {lst}. Value {og_budget}")

    while sum(lst) < 0 and any(item < 0 for item in lst):
            largest_negative_transaction = min(lst)  
            lst.remove(largest_negative_transaction)

    new_budget = sum(lst)

    if not lst or new_budget <= og_budget:
        print("Oops, looks bad, cannot be improved")
    else:
        print(f"Budget: {lst}. Value: {new_budget}")


