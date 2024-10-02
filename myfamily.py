#Need to add serial number in the before entering inputs
#If name age address are exact same then say duplicate entry print existing serial number

print("Welcome to data entry App")
fdict={}
i=0        
while True:
    i+=1
    key = i
    mydict={}
    print("Serial No:", key)
    key1 = "name"
    value = input("Enter name: ")
    mydict[key1] = value
    key2 = "age"
    value = input("Enter age: ")
    mydict[key2] = value
    key3 = "address"
    value = input("Enter address: ")
    mydict[key3] = value
    
    for j,k in fdict.items():
        l=str(k)
        if l in str(mydict):
            print("This duplicate entry already exists in key value:", j)
            i-=1
        else:
            continue
    fdict[key] = mydict

    x=input("Do you want to enter another person: to Stop Enter 'n' ")
    if x=='n':
        break
print(fdict)





        

