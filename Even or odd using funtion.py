def Check_Even_Odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return  "Odd"
num=int(input("Enter the number:"))
result=Check_Even_Odd(num)
print("The number is", result)