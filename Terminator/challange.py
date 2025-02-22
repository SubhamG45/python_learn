values =[10,0,25,0,50,-1,40]
total=0
average=0
for i in values :
    if i<0:
        break
    if i==0:
        continue
    total=total+i
    average=total/3
print(f"the total is {total}")
print(f"the average is {average}")    
