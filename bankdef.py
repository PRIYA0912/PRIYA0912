def checklength(la,le):
    username = input('Enter '+str(la)+':')
    if(int(len(username)) < le):
        username = checklength(la,le)
    return username    

def openaccount(cus):
    customer = []
    print('You r in Customer Open Account Process')
    id = input('Enter Customer Code:')
    email = checklength('Email',5)
    password = checklength('Password',6)
    fullname = checklength('Fullname',4)
    type_account = int(input('TYPE OF ACCOUNT\n1.SAVING\n2.CURRENT\n'))
    opening_balance = int(input('Enter Account Opening Balance:'))
    account_number = input('Enter Account Number:')
    customer.append(id)
    customer.append(email)
    customer.append(password)
    customer.append(fullname)
    customer.append(type_account)
    customer.append(opening_balance)
    customer.append(account_number)   
    cus.append(customer)
    o = int(input('Do You want to Open another Account?\n1.YES\n2.NO\n'))
    if(o == 1):
        cus = openaccount(cus)
    else:
        print('Continue with Openinig Account Module!') 
    return cus     


def registration(adm):
    admin = []
    print('You r in Bank User Registration Process')
    id = input('enter Employee Code:')
    username = checklength('Username',5)
    password = checklength('Password',6)
    fullname = checklength('Fullname',4)
    mobilenumber = input('enter Employee Mobile Number:')
    status = bool(input('enter Employee Status:'))
    admin.append(id)
    admin.append(username)
    admin.append(password)
    admin.append(fullname)
    admin.append(mobilenumber)
    admin.append(status)   
    adm.append(admin)
    o = int(input('Do You want to Register another User?\n1.YES\n2.NO\n'))
    if(o == 1):
        adm = registration(adm)
    else:
        print('Continue with admin!') 
    return adm     

def displayaccount(cus):
    print('ID \t EMAIL \t PASSWORD \t FULLNAME \t TYPE ACC. \t BALANCE \t ACCOUNT NUMBER')
    for i in range(int(len(cus))):
        iu = ''
        if(int(cus[i][4]) == 1):
            iu = 'SAVING'
        else:
            iu = 'CURRENT'    
        print(cus[i][0],' \t ',cus[i][1],' \t ',cus[i][2],' \t ',cus[i][3],' \t ',iu,' \t ',cus[i][5],' \t ',cus[i][6])

def login(adm,cus):
    print('You r in Bank User Login Process')
    uname = input('Enter Username:')
    x = -1
    for i in range(int(len(adm))):
        if(uname == adm[i][1]):
            x = i
            break
    if(x==-1):
        print('Invalid Username!')
        login(adm,cus)
    else:
        passd = input('Enter Password:')
        if(passd == adm[x][2]):
            print('welcome,',adm[x][3],'[Admin]')
            home(adm,cus)                   
def updateaccount(cus):
    displayaccount(cus)
    print('IN ABOVE RECORDS WHAT WOULD YOU LIKE TO UPDATE??')
    print('1.EMAIL')
    print('2.PASSWORD')
    print('3.FULL NAME')
    print('4.A/C TYPE')
    print('5.BALANCE')
    print('6.ACCOUNT NUMBER')
    d = input('ENTER CHOICE::')
    n = input('WHICH ID RELATED YOU WANT TO UPDATE:-')
    for i in range(int(len(cus))):
        aa = cus[i].index(n)
    if(int(d)==1):
        cus[aa][1] = input('ENTER UPDATED EMAIL:-')
    elif(int(d)==2):
        cus[aa][2] = input('ENTER UPDATED PASSWORD:-')
    elif(int(d)==3):
        cus[aa][3] = input('ENTER UPDATED FULL NAME:-')
    elif(int(d)==4):
        cus[aa][4] = input('ENTER UPDATED A/C TYPE:-')
    elif(int(d)==5):
        cus[aa][5] = input('ENTER UPDATED BALANCE:-')
    elif(int(d)==6):
        cus[aa][6] = input('ENTER UPDATED A/C NUMBER:-')
    return cus

def removeaccount(cus):
    n = input('WHICH ID RELATED YOU WANTED TO DELETE??')
    for i in range(int(len(cus))):
        aa = cus[i].index(n)
        cus[i][aa].pop
    return cus

def home(adm,cus):
    print('1.Open Account for Customers\n2.View Account\n3.Remove\n4.Update\n5.Logout')
    a = int(input('enter your choice:'))
    if(a == 1): 
        cus = openaccount(cus)
    elif(a==2):
        displayaccount(cus)
    elif(a==3):
        cus = removeaccount(cus)
    elif(a==4):
        cus = updateaccount(cus)
    elif(a==5):
        admin(adm,cus)
    home(adm,cus)    

def admin(adm,cus):
    print('1.REGISTRATION\n2.LOGIN\n3.EXIT')
    a = int(input('enter your choice:'))
    if(a == 1):
        adm = registration(adm)
    elif(a==2):
        login(adm,cus)
    elif(a==3):
        o = int(input('Are You Sure you want to exit from admin?\n1.YES\n2.NO\n'))
        if(o == 1):
           start(adm,cus)
        else:
            print('Continue with admin!')            
    else:
        print('wrong choice!') 
    admin(adm,cus)

def Withdraw(adm,cus,aa):
    if(aa == 0):
        ap = 'Withdraw'
    else:
        ap = 'Diposit'    
    print('You r in Bank ',ap,' Process')
    ac = input('enter your account number')
    x = -1
    for i in range(int(len(cus))):
        if(ac == cus[i][6]):
            x = i
            break
    if(x==-1):
        print('Invalid Account Number!')
        Withdraw(adm,cus,aa)
    else:
        print('Your Account Balance = ',cus[i][5])
        rs = int(input('Now,how many rs '+str(ap)+':'))
        if((rs > cus[i][5]) and (aa==0)): 
            print('Plz Enter Amount under your balance!') 
            Withdraw(adm,cus,aa)
        else:
            if(aa == 0):
                am = cus[i][5] - rs
            else:
                am = cus[i][5] + rs

            cus[i][5] = am
            o = int(input('Are You Sure you want to exit from '+str(ap)+'?\n1.YES\n2.NO\n'))
            if(o == 1):
                homecustomer(adm,cus)
            else:
                cus = Withdraw(adm,cus,aa)
    return cus



def homecustomer(adm,cus):
    print('1.Withdraw\n2.Deposit\n3.Logout')
    a = int(input('enter your choice:'))
    if(a == 1): 
        cus = Withdraw(adm,cus,0)
    elif(a==2):
        cus = Withdraw(adm,cus,1)
    elif(a==3):
        customer(adm,cus)
    homecustomer(adm,cus)


def logincustomer(adm,cus):
    print('You r in Bank Customer Login Process')
    uname = input('Enter Email:')
    x = -1
    for i in range(int(len(cus))):
        if(uname == cus[i][1]):
            x = i
            break
    if(x==-1):
        print('Invalid Email!')
        logincustomer(adm,cus)
    else:
        passd = input('Enter Password:')
        if(passd == cus[x][2]):
            print('welcome,',cus[x][3],'[Customer]')
            homecustomer(adm,cus)                 

def customer(adm,cus):
    print('1.LOGIN\n2.EXIT')
    a = int(input('enter your choice:'))
    if(a==1):
        logincustomer(adm,cus)
    elif(a==2):
        o = int(input('Are You Sure you want to exit from customer?\n1.YES\n2.NO\n'))
        if(o == 1):
           start(adm,cus)
        else:
            print('Continue with admin!')            
    else:
        print('wrong choice!') 
    customer(adm,cus)


def start(adm,cus):
    print('1.ADMIN\n2.CUSTOMER\n3.EXIT')
    a = int(input('enter your choice:'))
    if(a == 1):
        admin(adm,cus)
    elif(a == 2):
        customer(adm,cus)
    elif(a==3):
        o = int(input('Are You Sure you want to exit?\n1.YES\n2.NO\n'))
        if(o == 1):
            exit(0)
        else:
            print('Continue with my system!')    
    else:
        print('wrong choice!') 
    print('Your Above Operation is close Now,')
    start(adm,cus)    
adm = []
cus = []

start(adm,cus)