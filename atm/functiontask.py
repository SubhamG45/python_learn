# def cube_num(num):
#     print(f"cube of {num} is {num**3}")
#     num**3
# cube_num(5)
def find_age(birth_year):
    from datetime import date
    print(f"age:{date.today().year-birth_year}")
find_age(2006)