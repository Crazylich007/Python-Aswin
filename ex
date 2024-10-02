print("Welcome to data entry App")
fdict={}

with open('serial.txt', 'r') as file1:
    z=file1.read()
    if z=='':
        i=0
        with open('data.txt', 'w') as file:
            file.write('Serial_No,Name,Age,Address\n')
    else:
        i=int(z)
        
while True:
    i+=1
    key = i
    mydict={}
    print("Serial_No:", key)
    key1 = "name"
    value = input("Enter name: ")
    mydict[key1] = value
    key2 = "age"
    value = input("Enter age: ")
    mydict[key2] = value
    key3 = "address"
    value = input("Enter address: ")
    mydict[key3] = value
    
    with open('serial.txt', 'r') as file1:
        z=file1.read()
        if z=='':
            for j,k in fdict.items():
                l=str(k)
                if l in str(mydict):
                    print("This duplicate entry already exists in key value:", j)
                    i-=1
                else:
                    continue
        else:
            with open ('data1.txt','r') as file:
                entry=file.read()
                rows = entry.split()
                ndict={}
                for m in rows:
                    serial, name, age, address = m.split(',')
                    ndict[int(serial)] = {"name": name,"age": age,"address": address}

                for j,k in ndict.items():
                    l=str(k)
                    if l in str(mydict):
                        print("This duplicate entry already exists in Serial_No:", j)
                        i-=1
                    else:
                        continue

    fdict[key] = mydict

    x=input("Do you want to enter another person: to Stop Enter 'n' ")
    if x=='n':
        break
print(fdict)

with open('data.txt', 'a') as file:

    for serial, details in fdict.items():
        row = f"{serial},{details['name']},{details['age']},{details['address']}\n"
        file.write(row)

with open('data1.txt', 'a') as file2:

    for serial, details in fdict.items():
        row = f"{serial},{details['name']},{details['age']},{details['address']}\n"
        file2.write(row)

with open('serial.txt', 'w') as file1:
    row = f"{key}\n"
    file1.write(row)



        

