# fruits={"apple","mango","orange"}
# fruit={"grapes","apple","pear"}
# fruits[0]="banana" unchangeable.....
# print("apple" in fruits)
# fruits.add("banana")
# print(fruits)
# for fruit in fruits:
    # print(fruit)
fruits={"apple","mango","orange"}
fruit={"grapes","apple","pear"}

common=fruits.union(fruit)
print(common)
common=fruits.intersection(fruit)
print(common)


