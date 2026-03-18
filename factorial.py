def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number:"))
result=fact(n)
print("The factorial of th e number is:",result)