number=[1,4,6,2]
square=[x**2 for x in number  ]
print(square)
# and
number=[x**2 for x in range(1,5)]
print(number)
# last....
students={ "ram":51,"shyam":60,"gita":40,"rita":45}
new={name:grade for name,grade in students.items() if grade>50}
print(new)