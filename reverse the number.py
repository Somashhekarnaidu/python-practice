def reverse(num):
    rev=0
    while num>0:
        rev=rev*10
        rev+=num%10
        num=num//10
    return rev
num=int(input("Enter the number:"))
result=reverse(num)
print("The reverse of the number is:",result)