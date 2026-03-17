subjects=int(input("Enter the subjects:"))
marks=[]
for i in range(subjects):
    mark=int(input(f"Enter the marks for subjects{i+1}:"))
    marks.append(mark)
total=sum(marks)
avg=total/subjects
highest=max(marks)
lowest=min(marks)
if avg>=90:
    grade="S"
elif avg>=85:
    grade="A"
elif avg>=70:
    grade="B"
elif avg>=60:
    grade="C"
elif avg>=50:
    grade="D"
else:
    grade="F"
print("\n_-----Marks Analysis-----")
print("Total Marks:",total)
print("Average Marks:",avg)
print("Highest Marks:",highest)
print("Lowest Marks:",lowest)
print("Grade:",grade)
