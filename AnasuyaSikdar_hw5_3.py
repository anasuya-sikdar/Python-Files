
#Anasuya Sikdar
#Assignment 5.3

def squareDiagonals(n):
    
    if n < 5 or n % 2 == 0:
        return "Please provide an odd number greater than or equal to 5."
    
    for i in range(n):
        for j in range(n):
            
            if i == j or i == n - j - 1 or i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  

