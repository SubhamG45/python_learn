# list-comprehension- [expression for items in iterable if condition] syntax.....
number=[x**2 for x in range(1,5)]
print(number)
scores=[65,75,85,95,81,74]
h_marks=[score for score in scores if score > 80]
print(f"high score:{h_marks}")
words=["house","rabbit","score","play"]
check=[word for word in words if len(word)==5]
print("the word is:",check)

# dictionary compression.....
# syntax -{key _expression:value_expression for item in iterable if condition}
square={x:x**2 for x in range (1,6)}
print(square)
student_score={ "ram":20,"shyam":25,"hari":15,"gita":30}
more_than_20 ={name:value for name,value in student_score.items() if value >20}
print(more_than_20)