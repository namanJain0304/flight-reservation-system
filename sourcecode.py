import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="1234",database="airline")
if con.is_connected():
    print("connection successful")
cur=con.cursor()
amount=0
def menu():
    print()
    print("FLIGHT MANAGEMENT SYSTEM PORTAL".center (50) )
    print("*"*126)
    print("1".center(50))
    print("This option allows you to:-")
    print("Create your Profile")
    print("Book your Flight tickets")
    print("Show your luggage expense")
    print("order your food(optional)")
    print("*"*50)
    print("2".center(50))
    print("This option allows you to:-")
    print("edit your profile")
    print("*"*126)
menu()

def create_passenger():
    cur.execute("create table if not exists passenger(id int(3),name varchar(25),age int(3),address varchar(50),rdate date,mobno int(11))")
    ID=int(input("please enter the passenger id-"))
    pname=input("please enter you name-")
    age=int(input("enter age-"))
    address=input("enter the address-")
    rdate=input("enter the registration date(YYYY-MM-DD)-")
    mobno=int(input("enter your mobile number-"))
    cur.execute("insert into passenger values({},'{}',{},'{}','{}',{})".format(ID,pname,age,address,rdate,mobno))
    con.commit()
    print("\n")
    print("your details are as follows:")
    print("\n")
    print(("Id","name","age","address","rdate","mobno"))
    cur.execute("Select * from passenger")
    data=cur.fetchall()
    print(data[-1])
    print("\n")


def edit_passenger():
    cur=con.cursor()
    a=int(input("enter the id"))
    print("1. edit name")
    print("2. edit age")
    print("3. edit address")
    print("4. edit rdate")
    print("5. edit mobno")
    while True:
        b=int(input("pls enter your choice(1,2,3,4,5)-"))
        if b==1:
            name=input("please enter your new name-")
            cur.execute("update passenger set name='{}' where id={}".format(name,a))
        elif b==2:
            age=int(input("please enter your new age-"))
            cur.execute("update passenger set age={} where id={}".format(age,a))
            
        elif b==3:
            address=input("please enter your new address-")
            cur.execute("update passenger set address='{}' where id={}".format(address,a))
        elif b==4:
            rdate=input("please enter your new rdate-")
            cur.execute("update passenger set rdate='{}' where id={}".format(rdate,a))
        elif b==5:
            mobno=int(input("please enter your new mobile no,-"))
            cur.execute("update passenger set mobno={} where id={}".format(mobno,a))
        else:
            print("u have enteres wrong choice")
        ch=input("d u want to edit more records(y,n)")
        if ch in "nN":
            break
    
    con.commit()


def flights_available():
    print("Here are the flights available:")
    print("\n")
    cur.execute("select * from flight")
    data=cur.fetchall()
    print(("flight_number","date_and_time","source","destination","seats_left","fare_price"))
    print("\n")
    for i in data:
        print(i)
    print("\n")



def book_seat():
    
    global amount
    flight_no=input("please enter the flight no.:")
    seat=int(input("enter the no. of seats you want to book:"))
    cur.execute("select * from flight")
    found=0
    data=cur.fetchall()
    for i in data:
        if i[0]==flight_no:
            print("\n")
            print("BOOKING SUCCESSFUL!")
            print("\n")
            print("you have booked",seat,"seats on flight number:",flight_no)
            print("the flight will go from",i[2],"to",i[3],"on",i[1])
            print("payable amount for flight=",i[5]*seat,"rupees")
            found=1
            a=i[4]-seat
            cur.execute("update flight set seats_left={} where  flight_number='{}'".format(a,flight_no))
            amount+=i[5]*seat
            con.commit()
            print("\n")
    if found==0:
            print("Sorry,no such flight no. was found")





def show_fooditems():
    print("Here are the food items you can order:")
    print("\n")
    cur.execute("select * from food")
    data=cur.fetchall()
    print(("item_number","itemname","price"))
    print("\n")
    for i in data:
        print(i)
    print("\n")
        
        
        
def order_fooditems():
    global amount
    item_no=input("please enter the item no. of the food item you want to order:")
    quantity=int(input("Quantity:"))
    print("\n")
    cur.execute("select * from food")
    found=0
    data=cur.fetchall()
    for i in data:
        if i[0]==item_no:
            print("ORDER SUCCESSFUL!")
            print("\n")
            print("You have ordered:",i[1],",","quantity=",quantity)
            print("payable amount for food=",i[2]*quantity,"rupees")    
            amount+=i[2]*quantity

            found=1
            print("\n")
    if found==0:
        print("Sorry,no such item no. was found")



def luggage_expenses():
    global amount
    c2=con.cursor()
    c2.execute("Select * from luggage")
    data=c2.fetchall()
    print(" the luggage charges are as follows:")
    print("\n")
    print(("sno","Weight","rate"))
    print("\n")
    for i in data:
        print(i)
    ch=int(input("enter the sno you want to purchase-"))
    print("\n")
    for j in data:
        if j[0]==ch:
            print("payable amount for luggage=",j[2],"rupees")
            amount+=j[2]
            print("\n")
        
        
        
        
        


opt=int(input("enter your choice from the menu(1/2):"))
  
if opt==1: 
    create_passenger()
    print("*"*126)
    flights_available()
    print("*"*126)
    book_seat()
    print("*"*126)
    luggage_expenses()
    print("*"*126)
    x=input("do you want to order food(y/n):")
    print("/n")

    if x in "yY":
        show_fooditems()
        print("*"*126)
        order_fooditems()
        print("*"*126)
        print("THANKYOU FOR VISITING")
        print("Your Total Payable Amount=",amount,"rupees")
        print("*"*126)

    else:
        print("THANKYOU FOR VISITING")
        print("*"*126)
        print("Your Total Payable Amount is-",amount,"rupees")
        print("*"*126)
       
elif opt==2: 
    edit_passenger()


else:
    print('invalid option')



