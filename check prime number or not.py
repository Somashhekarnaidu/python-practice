def check_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i== 0:
                return "Not a prime number"
            else:
                return "Prime number"
num=int(input("Enter the number:"))
result=check_prime(num)
print(result)

