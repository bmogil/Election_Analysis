import random

our_List = ['r', 'p', 's']
print(random.choice(our_List))
the_User = input("Enter r, p, or s")
if random.choice(our_List) == the_User:
    print("It's a tie!")
