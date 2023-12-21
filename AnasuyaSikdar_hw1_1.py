
# Submission Date : 09/12/2023
# Student Name : Anasuya Sikdar

#Take user Inputs of the Number of Shares bought/sold, Purchase Price anf Selling Price
numShares = eval(input('Number of Shares: '))

buyPurchase = eval(input('Buy price of one share: '))

sellPrice = eval(input('Sell price of one share: '))

fee = 3/100

#To calculate the cost of buying the shares
costBuy =  numShares * buyPurchase

#Brokerage fee paid at the time of Purchase
costBrokerageFee = fee * costBuy

#To calculate the cost of selling the shares
costSell = numShares * sellPrice

#Brokerage fee paid at the time of Selling
sellBrokerageFee = fee * costSell

#To calculate the Total Buy and Total Sell Amounts
totalBuy = costBuy + costBrokerageFee
totalSell = costSell - sellBrokerageFee

#To calculate the gain or loss
gain_or_loss = totalSell - totalBuy
#Rounding off the value
finalValue = round(gain_or_loss,2)

#Print Statements to display output
print('Amount invested in stock buy trade(includes fee):',totalBuy)
print('Amount invested in stock sell trade(includes fee):',totalSell)
#Print statement to display the end result
print('The result of the trades is a gain (or loss) of ',finalValue, 'dollars')

#Test Case to compute a Loss
#Number of Shares = 200
#Purchase Amount of each Share = $60
#Selling Price of each Share = $55
#So, the cost of buying the shares would be 200 * 60 i.e. $12000
#And, the cost of selling the shares would be 200 * 55 i.e. $11000
#Also, the total cost to buy the shares = Brokerage fee paid at the time of buying the shares + cost to buy all the given shares
#totalBuy = 12000 + (0.03*12000) = 12000 + 360 = 12360
#Similarly for totalSell = 11000 + (0.03 * 11000) = 11000 + 330 = 11330
# Difference between totalSell and totalBuy = 11330 - 12360 = -1030
#This has resulted into a loss while trading.
