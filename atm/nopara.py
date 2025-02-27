
# function with no return type and no parameter............................
def prime_minister():
    print("current prime minister is kp")
prime_minister()

 # function with no return type but with parameter..........................
def full_name(first_name,last_name):
    print(f"my name is {first_name} {last_name} ")
full_name("ram","bdr")
# having both parameter and return type......................................
def full_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name
fn=full_name("ram","adi")
print(fn)
# no parameter and return type..................................................
def voter_age():
    return 18
age=17
if age>=voter_age():
    print("he can vote")
else:
    print("he cannot vote")