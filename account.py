accounts = [{"acc_id":201,"balance":15000.00},{"acc_id":202,"balance":25000.00}]
def create_acc(a_no,bal):
    acc={}
    #print(acc)
    for ele in accounts:
        if ele["acc_id"]==a_no :
            print("ERROR account already exists")
            return
    if bal < 1000.0:
        print("ERORR Minimum balance is 1000")
        return
    acc["acc_id"]=a_no
    acc["balance"]=bal
    print("The account has been created succesfully")
    accounts.append(acc)
    print("----------------------------------------------------------")
    #print(accounts)
    return
def deposit(a_no,amt):
    flag=0
    for ele in accounts:
        if ele["acc_id"]==a:
            flag=1
            print("Before deposit balance in account no %d is %.2f"%(a_no,ele["balance"]))
            ele["balance"]+=amt
            print("After deposit balance in account no %d is %.2f"%(a_no,ele["balance"]))
    if flag==0:
        print("account does not exists\nEnter 1 to create account")
    print("----------------------------------------------------------")
    #print(accounts)
def withdraw(a_no,amt):
    flag=0
    if amt > 10000:
        print("maximum withdrwal is 10000")
        return
    for ele in accounts:
        flag=0
        if ele["acc_id"]==a:
            flag=1
            if ele["balance"]-amt <1000:
                print("minimum balance must be maintained")
                return
            else:
                print("Before withdrawal balance in account no %d is %.2f"%(a_no,ele["balance"]))
                ele["balance"]-=amt
                print("After withdrawal balance in account no %d is %.2f"%(a_no,ele["balance"]))
    if flag==0:
        print("account does not exists\nEnter 1 to create account")
    print("----------------------------------------------------------")
    #print(accounts)
def show(a_no):
    flag=0
    for ele in accounts:
        if ele["acc_id"]==a_no:
            flag=1
            print("balance in the acc %d is %d"%(a_no,ele["balance"]))
    if flag==0:
        print("account does not exists\nEnter 1 to create account")
    print("----------------------------------------------------------")
    #print(accounts)
def transfer(so,ac,amt):
    f1=0
    f2=0
    for i in accounts:
        if i["acc_id"]==so:
            f1=1
            break
    for j in accounts:
        if j["acc_id"]==ac:
            f2=1
            break
    if f1==1 and f2==1:
        flag=0
        if amt > 25000:
            print("maximimum transfer is 25000")
            return
        for ele in accounts:
            #flag=0
            if ele["acc_id"]==so:            
                if ele["balance"]-amt <1000:
                    print("minimum balance must be maintained")
                    return
                else:
                    print("Before tranfer balance in account no %d is %.2f"%(so,ele["balance"]))
                    ele["balance"]-=amt
                    print("After tranfer balance in account no %d is %.2f"%(so,ele["balance"]))
                    flag=1
                    break
        for el in accounts:
            #flag=0
            if el["acc_id"]==ac:
                flag=1
                print("Before tranfer balance in account no %d is %.2f"%(ac,el["balance"]))
                el["balance"]+=amt
                print("After tranfer balance in account no %d is %.2f"%(ac,el["balance"]))
                break
    else:
        print("account does not exists\nEnter 1 to create account")
        #print(accounts)
    print("----------------------------------------------------------")
def close(a_no):
    for i in accounts:
        if i["acc_id"]==a_no:
            accounts.remove(i)
            print("Account has been deleted successfully")
            #print(accounts)
            return
    print("Account does not exists")
    #print(accounts)
    print("----------------------------------------------------------")
print("**************************")
print("   WELCOME TO I.C.I.C.I ")
print("**************************")
print("      OPERATIONS")
choice=1

print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Show Balance\n5. Fund Transfer\n6. Close Account\n7. Exit")
while choice:
    choice=int(input("Enter operation number: "))
    match choice:
        case 1:
            a=int(input("Enter Account Number: "))
            b=float(input("Enter Starting Balance: "))
            create_acc(a,b)
        case 2:
            a=int(input("enter account number: "))
            d=int(input("enter amount to be deposited: "))
            deposit(a,d)
        case 3:
            a=int(input("enter account number: "))
            w=int(input("enter amount to be withdrawn : "))
            withdraw(a,w)
        case 4:
            a=int(input("enter account number: "))
            show(a)
        case 5:
            s=int(input("Enter Source Account Number :"))
            a=int(input("Enter Target Account Number :"))
            p=float(input("Enter Transfer Amount :"))
            transfer(s,a,p)
        case 6:
            a=int(input("enter account number: "))
            close(a)            
        case 7:
            print("THANK YOU")
            break
        case _:
            print("Enter valid input")
            
        



# In[ ]:
