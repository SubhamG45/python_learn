# dictionary......
data ={"Nepal":"kathmandu", "india":"new delhi", "usa":"wdc"}
data["Nepal"]="ktm"
print(data)
data.pop("Nepal")
# print(f"the capital city of nepal is {data["Nepal"]}") pop...removing
person_info={
    "name":"ram"
    ,"age":1,
    "f.movie":["dear_comrade","saran",]
}
print(person_info)
print(f"{person_info["f.movie"][0]} is my favourite movie.")
print("name" in person_info)