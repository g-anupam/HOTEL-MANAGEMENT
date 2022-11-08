import mysql.connector as mc
print("In order to establish MySql connection on your device,you must enter the MySql details below:")
a9 = str(input("Enter name of the host:"))
b9 = str(input("Enter name of the user:"))
c9 = str(input("Enter the password for your MySql:"))
mydb = mc.connect(host=a9,user=b9,passwd=c9,database='hotel')
mycursor = mydb.cursor()
l=[]
q=[]
global w
global e
w=1
e=1
print("                                                                                                                 ")
print("                                                                                                                 ")
print("-----------------------------------------------------------------------------------------------------------------")
print("_________________________________________________________________________________________________________________")
print("                                 WELCOME TO GRAND PALACE HOTEL                                                   ")
print("                                                                         129,Oakwood street                      ")
print("                                                                         New Delhi-680004                        ")
print("                                                                         8492349530                              ")
print("                                                                         www.grandpalace/hotel.com               ")
print("-----------------------------------------------------------------------------------------------------------------")
print("_________________________________________________________________________________________________________________")
print("                                                                                                                 ")
print("                                                                                                                 ")
def registercust():
    name=input("Enter name:")
    addr=input("Enter address:")
    indate=input("Enter check in date:")
    outdate=input("Enter check out date:")
    query="insert into custdata values('{}','{}','{}','{}')".format(name,addr,indate,outdate)
    mycursor.execute(query)
    mydb.commit()

def roomtypeview():
    ch=int(input("Enter 1 if you would liek to see the types of rooms."))
    if ch==1:
        sql="select * from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def roomrent():
    global u
    print ("We have the following rooms for you:-")
    print ("1. type A- 1 bed--->rs 1000 PN\-")
    print ("2. type B- 2 beds--->rs 2000 PN\-")
    print ("3. type C- 2 beds--->rs 3000 PN\-")
    print ("4. type D- 4 beds--->rs 4000 PN\-")
    x=int(input("Enter Your Choice Please->"))
    n=int(input("For How Many Nights Did You Stay:"))
    if(x==1):
        print ("you have opted room type A")
        s=1000*n
    elif (x==2):
        print ("you have opted room type B")
        s=2000*n
    elif (x==3):
        print ("you have opted room type C")
        s=3000*n
    elif (x==4):
        print ("you have opted room type D")
        s=4000*n
    else:
        print ("please choose a room")
    print ("your room rent is =",s,"\n")
    u=s
def restaurentmenuview():
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
def orderitem():
    global s
    global r
    print("Do yoy want to see menu available : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)

    print("do you want to purchase from above list:enter your choice:")
    d=int(input("enter your choice:"))
    if(d==1):
        print("you have ordered tea")
        a=int(input("enter quantity"))
        s=10*a
        l.append(s)
        print("your amount for tea is :",s,"\n")
    elif (d==2):
        print("you have ordered coffee")
        a=int(input("enter quantity"))
        s=10*a
        l.append(s)
        print("your amount for coffee is :",s,"\n")
    elif(d==3):
        print("you have ordered colddrink")
        a=int(input("enter quantity"))
        s=20*a
        l.append(s)
        print("your amount for colddrink is :",s,"\n")
    elif(d==4):
        print("you have ordered samosa")
        a=int(input("enter quantity"))
        s=10*a
        l.append(s)
        print("your amount fopr samosa is :",s,"\n")
    elif(d==5):
        print("you have ordered sandwich")
        a=int(input("enter quantity"))
        s=50*a
        l.append(s)
        print("your amount fopr sandwich is :",s,"\n")
    elif(d==6):
        print("you have ordered dhokla")
        a=int(input("enter quantity"))
        s=30*a
        l.append(s)
        print("your amount for dhokla is :",s,"\n")
    elif(d==7):
        print("you have ordered kachori")
        a=int(input("enter quantity"))
        s=10*a
        l.append(s)
        print("your amount for kachori is :",s,"\n")
    elif(d==8):
        print("you have ordered milk")
        a=int(input("enter quantity"))
        s=20*a
        l.append(s)
        print("your amount for kachori is :",s,"\n")
    elif(d==9):
        print("you have ordered noodles")
        a=int(input("enter quantity"))
        s=50*a
        l.append(s)
        print("your amount for noodles is :",s,"\n")
    elif(d==10):
        print("you have ordered pasta")
        a=int(input("enter quantity"))
        s=50*a
        l.append(s)
        print("your amount for pasta is :",s,"\n")
    else:
        print("please enter your choice from the menu")
    w=sum(l)
    print("The total cost for your food is:",w)
    r=w
def laundarybill():
    global la
    print("Do yoy want to see rate for laundary : Enter 1 for yes :")
    ch=int(input("enter your choice:"))
    if ch==1:
        sql="select * from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Enter Your number of clothes->"))
    z=y*10
    q.append(z)
    e = sum(q)
    print("your laundary bill:",e,"\n")
    la=e
def lb():
    print(la)
def res():
    print(r)
def rent():
    print(u)
def viewbill():
    a=input("Enter customer name:")
    print("---------------------------------------------------------------------------")
    print("Customer name :",a,"\n")
    print("Laundry bill:")
    lb()
    print("Restaurent bill:")
    res()
    print("Room Rent:")
    rent()
    print("TOTAL AMOUNT TO BE PAID",la+r+u)
    print("---------------------------------------------------------------------------")

def Menuset():
    while True:
        userinput=int(input('''Enter your choice for apllication:
1:Enter Customer Data
2:View Rooms
3:Calculate Room Bill
4:View Restaurent menu
5:Calculate Restaurant Bill
6:Calculate laundry Bill
7:Complete bill for Check Out
8:exit'''))
        if(userinput==1):
            registercust()
        elif(userinput==2):
            roomtypeview()
        elif(userinput==3):
            roomrent()
        elif(userinput==4): 
            restaurentmenuview()
        elif(userinput==5):
            orderitem()
        elif(userinput==6):
            laundarybill()
        elif(userinput==7):
            viewbill()
            quit()
        elif(userinput==8):
            quit()
        else:
            print("Enter correct value for choice!")
            break 
Menuset()
        
    



    
