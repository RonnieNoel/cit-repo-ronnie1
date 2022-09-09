# Create a 2-D array and slice out the second number in the second column
numbers=[[1,2,3],
         [4,5,6],
         [9,8,7]]
print(numbers[1][1])
# Write a python program to sort array element in the ascending/descending order
numbers = [30,15,60,1]
numbers.sort()
print('Ascending Order: ', numbers)

numbers.sort(reverse=True)
print('Descending Order: ', numbers)

# Write a python program to find the maximum and minimum value in a given 2-D array

numbers=[[1,2,3],[4,5,6]]
print("the maximum number is" + max(list(map(max, numbers))))
print("the minimum number is" + min(list(map(min, numbers))))
# Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# percentage less than 50 (Grade C)
# percentage equal to 50 and less than 80 (Grade B)
# percentage equal to 80 and more than 80 (Grade A)
num1=int(input("enter the 1st number: "))/100
num2=int(input("enter the 2nd number: "))/100
num3=int(input("enter the 3rd number: "))/100
num4=int(input("enter the 4th number: "))/100
num5=int(input("enter the 5th number: "))/100

total =num1+num2+num3+num4+num5

av_mark=(total/5)*100

if av_mark>=80:
    print(f"{av_mark},Grade A")
elif av_mark>=50:
    print(f"{av_mark},Grade B")
elif av_mark>=0:
    print(f"{av_mark},Grade C")
else:
    print("Enter a correct mark")


# Create a nesting list that prints out the color and the car brand.


matrix = [["toyota","bmw" ,"nisan" ],
          ["red", "blue", "green"],
          ]

rows = len(matrix)  
cols = len(matrix[0])  

print("car and brand matrix ")
for i in range(0, rows):
    print(matrix[i])
    
print( matrix[0][1], matrix[1][0])



# Write a function called show_stars(rows). If rows is 5, it should print the following:
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()


# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
numbers = input("type your numbers seprated commas here : ")
list = numbers.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# Write a function to compute 5/0 and use try/except to catch the exceptions.

def compute():
    return 5/0

try:
    compute()
except ZeroDivisionError:
    print ("division by zero!")
    
# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point
# and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”  


def speedevaluator(speed):
    if speed <= 70:
        return "OK"
    else:
        newspeed = (speed-70)/5
        if newspeed <= 12:
            print(f"Point: {newspeed}")
        else:
            print("License suspended")
speedevaluator(int(input("Enter speed: ")))

# Write a program which will find all such numbers which are divisible by 7 but are not a 
# multiple of 5 between 2000 and 3200 (both included). The numbers obtained should be printed in 
#     a comma-separated sequence on a single line.

numbers=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        numbers.append(str(x))
print (','.join(numbers))


# Write a program that calculates and prints the value according to the given formula:
#     Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. 
#     H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. 
#     Example Let us assume the following comma separated input sequence is given to the 
# program: 100,150,180 The output of the program should be: 18,22,24
import math

val = input("Provide D: ")
val = val.split(',')

res = []
for i in val:
    j = round(math.sqrt(2 * 50 * int(i) / 30))
    res.append(j)

print(res)
