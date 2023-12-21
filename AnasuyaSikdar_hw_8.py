#Anasuya Sikdar
#Assignment 8


class TransitCard:
    # Class variable for the maximum transaction amount
    MAX_TRANSACTION_AMOUNT = 100
    
    def __init__(self, amount=5):
        """Initialize the TransitCard with a specified balance up to $100, defaults to $5."""
        if amount > 100.00:
            raise ValueError('Amount is > 100.00')
        self.balance = amount  # Instance variable for the card balance
        self.MAX_BALANCE = 350  # Instance variable for the maximum card balance amount

    def ride(self, fare):
        """
        Deduct fare from the card balance if the conditions are met,
        otherwise raise a ValueError.
        """
        if self.balance <= 0:
            raise ValueError('Card balance is 0 or negative; ride is denied')
        elif 0 < self.balance < fare:
            self.balance -= fare
        elif self.balance >= fare:
            self.balance -= fare

    def addValue(self, amount):
        """
        Add value to the card balance if the amount is within the limits,
        otherwise raise a ValueError.
        """
        if amount > TransitCard.MAX_TRANSACTION_AMOUNT:
            raise ValueError('Amount is > 100.00;')
        if not 0 < amount <= TransitCard.MAX_TRANSACTION_AMOUNT:
            raise ValueError('Invalid amount; it must be greater than 0 and less or equal to 100.00.')
        if self.balance + amount > self.MAX_BALANCE:
            raise ValueError('Card balance will be greater than 350.00; request is denied')
        self.balance += amount

    def balance(self):
        """Return the current balance on the card."""
        return self.balance

    def __repr__(self):
        """Return a canonical string representation of the TransitCard."""
        return f'The card balance is {self.balance}'

# Example usage:
#card = TransitCard()
#card.addValue(50)
#print(card)
#card.ride(2.75)
#print(card)
#card.ride(3.50)
#print(card)
