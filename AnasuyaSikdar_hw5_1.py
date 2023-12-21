#Anasuya Sikdar
#Assignment 5.1

def evenRow(lst):
    for i in range(len(lst)):  
        sumNum = 0  
        for j in range(len(lst[i])):  
            sumNum += lst[i][j]  
        if sumNum % 2 != 0:  
            return False  
    return True 
