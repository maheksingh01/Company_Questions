n = int(input("Enter the value of n : "))

arr = [];

# check two consecutive number is not divisible by 3 

def divisible3(arr1, n):
    for i in range(n):
        if(arr1[i]%3==0 and arr1[i+1]%3==0):
            arr[i+1], arr[i+2] = arr[i+2], arr[i+1]
            if(arr1[i]%3==0 and arr1[i+1]%3==0):
                print("arrangement not possible")
                break
            else:
                i+=1
            # print(arr1)
    else:
        print("arrangement successfull")
        print(arr1)
            

# inserting elements in an array

def insertArray(arr, n):
    while n > 0:
        num = int(input("enter the value : "))
        if num not in arr:
            arr.append(num)
        else: 
            break
        n -= 1
    print(arr)

# check the number of elements to be 7 only
if(n == 7) :
    insertArray(arr, n)
    divisible3(arr, n)
else :
    print("invalid input")