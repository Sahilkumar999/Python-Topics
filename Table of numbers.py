number = int(input("Which number's table do you want? "))

num = [1,2,3,4,5,6,7,8,9,10]
print('Table of %(number)d is : '  )
for  x in num:
    y = number * x 
    print(str(number) + ' X ' + str(x) + '=' + str(y))
