#Anasuya Sikdar
#Assignment 3.1
def formatOutput(num):
  import random
  lst = []
  for i in range(num):
    lst.append(random.uniform(0, 10000))
  #print(lst)
  for i in range(0, len(lst), 3):
    row = lst[i:i+3]
    new_row = [f"{x:9,.2f}" for x in row]
    print(" ".join(new_row))

