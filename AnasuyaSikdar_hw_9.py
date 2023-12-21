#Anasuya Sikdar
#Extra Credit

class MyRR:
    def __init__(self, input_list):
        self.list = input_list
        self.index = 0

    def next(self):
        item = self.list[self.index]
        self.index = (self.index + 1) % len(self.list)
        return item

# Example usage:
#rr1 = MyRR([7,9,-11,3,110])
#print(rr1.next()) 
#print(rr1.next()) 
#print(rr1.next()) 
#print(rr1.next()) 

#rr2 = MyRR(['Monica','Chandler','Ross'])
#print(rr2.next()) 
#print(rr2.next()) 
# print(rr2.next()) 
# print(rr2.next()) 
