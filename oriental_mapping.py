arr1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


# mapping the 2 provided arrays
mapping = dict(zip(arr1, arr2))
# print(mapping)

# taking two names as input
name1 = input("Enter first name : ")
name2 = input("Enter second name : ")

# function to calculate the value of the name
def calculate_name_value(name):
    return sum(mapping.get(char.upper(), 0) for char in name);

# storing the values of the sum
sum1 = calculate_name_value(name1)
sum2 = calculate_name_value(name2)

# main condition
if(sum1 > sum2):
    print(name1 + " WINS!")
elif(sum1 < sum2):
    print(name2 + " WINS")
else:
    print("TIE, Better luck next time")


