def second_largest(lst):
    if len(lst)<2:
        return "List has less than 2 elements"
    lst.sort()
    return lst[len(lst)-2]
list=int(input("Enter the number of elements in the list:"))
lst=[]