def sum(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total
n=int(input("Enter the number:"))
result=sum(n)
print("The sum of the digits is:",result)