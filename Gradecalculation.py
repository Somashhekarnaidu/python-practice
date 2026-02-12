name=input("subject name:")
marks=int(input("Enter the marks:"))
if marks>=50:
    print(name,"||",marks,"||,","Pass","Grade=D")

elif marks>=65:
    print(name,"||",marks,"||,","Pass","Grade=C")
elif marks>=75:
    print(name,"||",marks,"||,","Pass","Grade=B")
elif marks>=85:
    print(name,"||",marks,"||,","Pass","Grade=A")
else:
    print(name,"||",marks,"||,","Fail")
