def vowels(word):
    count=0
    for i in word:
        if i in "aeiouAEIOU":
            count+=1
    return count
word=input("Enter the word:")
result=vowels(word)
print("The number of vowels in the word is :",result)
