import pymysql
import sys
from tabulate import tabulate
import datetime
from prettytable import PrettyTable 
conn=pymysql.connect(host="localhost",user="root", password="avi12345", database="Project",autocommit=True)
c1= conn.cursor()

def open():
    print("You Are....".center(140))
    print("1.Customer".center(140), "2.Owner".center(139), "3.Exit".center(138),sep="\n")
    global z
    z=input("Enter Choice".rjust(75)) 
    if z=="1":
        customer() 
    elif z=="2":
        owner_intro()
    elif z=="3":
        sys.exit() 
    else:
        print("Wrong Input".center(140))
        j=input("Do you want to Try Again(y/n)".rjust(85) ) 
        if j.strip()=="y":
           open() 
        else:
           sys.exit()

def customer():
    global u
    u=input("Enter Customer name".rjust(79)) 
    print()
    print("Welcome Customer".center(140)) 
    user()

def user():
    print("Choose from the following".center(140), "1.Electrical Items".center(140), "2.Furniture Items".center(140),
        "3.Food Items".center(140),
        "4.Print Bill".center(140),sep="\n")
    i=int(input("Enter Choice".rjust(75))) 
    print()
    if i==1:
        f("Electric_items") 
    elif i==2:
        f("Furniture_items") 
    elif i==3:
        f("Food_items")
    elif i==4:
        bill() 
    else:
        print("Wrong Input".center(140))
        j=input("Do you want to Try Again(y/n)".rjust(85) ) 
        if j.strip()=="y":
             pass 
        else:
             open()

def f(u):
    try:
        c1.execute("Select * from {}".format(u))
    except:
        print("No Item Exists".center(140))
    j=input("Do you want to Search other type of goods(y/n)".rjust(95))
    if j.strip()=="y":
        user() 
    else:
        return open() 
    r=c1.fetchall() 
    l=[]
    for i in r:
        l+=[i] 
    global d
    if len(l)!=0:
        print(tabulate(l,headers=[" Item_Code "" Name ",
    " Cost ",
    " Quantity Available ",
    " Item_Provider ",
    " Item_Provier_Phone_No "],tablefmt='orgtbl') ) 
    
    while True:
    
        i=input("Enter Item Code which is to be Bought".rjust(88)) 
        qty=int(input("Enter Quantity".rjust(75)))
        q="Select * from {0} where Item_Code='{1}'".format(u,i) 
        try:
            c1.execute(q) 
        except:
            print("No Data Found".center(140)) 
        a=c1.fetchone()
        try:
            p=a[3]-qty 
            if p>0:
                e="Update {0} set Quantity_Available={1} where Item_- code='{2}'".format(u,p,i.strip())
                c1.execute(e)
                conn.commit()
                d[a[0]]=[a[1],a[2],qty]
                j=input("Do you want to continue buying(y/n)".rjust(88) )
                if j.strip()=="y":
                    pass
                else:
                    user()
                    break 
            else:
                print("Not enough Quantity_Available".center(140))
                j=input("Do you want to continue buying(y/ n)".rjust(88) )
                if j.strip()=="y": 
                    pass
                else: 
                    user()
                    break 
        except TypeError :
            print("No Data Found".center(140))
            j=input("Do you want to continue buying(y/n)".rjust(88) ) 
            if j.strip()=="y":
                pass 
            else:
                user()
                break 
        else:
            print("No Data Exists".center(140))
    j=input("Do you want to Search Other Table(y/n)".rjust(90)) 
    if j.strip()=="y":
        user() 
    else:
        open() 
    conn.commit()
d={}

def bill():
    t_date=datetime.date.today()
    t_time=datetime.datetime.now()
    print("="*139)
    txt=["AVINASH HOME STORE","ADDRESS: Sector 20,NOIDA","PHONE NO. :9975465434"] 
    print()
    for i in txt: 
        print(i.center(140)) 
        print()
    print("="*139) 
    print("INVOICE".center(140)) 
    print("="*139)
    print("DATE :".rjust(25),"",t_date,"Time ".rjust(70),t_time.hour,":",t_time.minute,":",t_time.second) 
    print("="*139)
    print("Customer :".rjust(29),u)
    print("="*139)
    l=[]
    for k in d:
        l+=[[k,d[k][0],d[k][1],d[k][2],d[k][2]*d[k][1]]] 
        w=PrettyTable([" ITEM CODE "," NAME ","    COST   ","     QUANTITY      ","   TOTAL   "])
        j=0
        for i in l:
            w.add_row(i) 
            j+=i[4]
        print(w)        
        print()
        print("Total Bill :".rjust(70),j)
        print()
    print("="*139)
    j=input("Do you want to start again(y/n)".rjust(86)) 
    if j.strip()=="y":
        open() 
    else:
        sys.exit()

def owner_intro():
    print("Welcome on the Site of Owner".center(140)) 
    while True:
        i=input("Enter Password".rjust(77)) 
        if i.strip()=="ABCD":
             print("Welcome !!!".center(140)) 
             Table_owner()
             break
        else:
            print("Wrong Input".center(140))
            j=input("Do you want to Try Again(y/n)".rjust(85)) 
            if j.strip()=="y":
                pass 
            else:
                open()
                break

def Table_owner():
    print("1.Electric_items".center(140), "2.Furniture_items".center(140), "3.Food_items".center(140),
    "4.Exit Owner's Site".center(140),sep="\n")
    i=int(input("Which Type of Table you want to see".rjust(88))) 
    if i==1:
       Owner("Electric_items") 
    elif i==2:
        Owner("Furniture_items") 
    elif i==3:
        Owner("Food_items") 
    elif i==4:
        open() 
    else:
        print("Wrong Input".center(140))
        j=input("Do you want to Try Again(y/n)".rjust(85)) 
        if j.strip()=="y":
            pass 
        else:
            open()

def choice():
    j=input('Do you Want to See Other Table(y/n)'.rjust(90)) 
    if j.strip()=="y":
          Table_owner() 
    elif j.strip()=="n":
          open() 
    else:
          print("Wrong Input".center(140))
          j=input("Do you want to Try Again(y/n)".rjust(85)) 
          if j.strip()=="y":
             pass 
          else:
             open()

def Owner(i1):
    while True: 
        print("1.Read".center(140),
        "2.Insert".center(140),
        "3.Update".center(140),
        "4.Delete".center(140),
        "5.Search".center(140),
        "6.Restocking Requirement".center(140),
        "7.Go Back To Owner’s Site".center(140),sep="\n")
        b=int(input("What Do You Want To Do?".rjust(82))) 
        global i
        i=i1
        if b==1:
            Read_Table() 
        elif b==2:
            Insert_Table() 
        elif b==3:
            Update_Table()
            break 
        elif b==4:
            Delete_Table()
            break 
        elif b==5:
            Search_Table()
            break 
        elif b==6:
            Stock_Order() 
        elif b==7:
            Table_owner()
            break 
        else:
            print("Wrong Input".center(140))
            j=input("Do you want to Try Again(y/n)".rjust(85)) 
            if j.strip()=="y":
                pass 
            else:
                Table_owner()
        h=input("Do You Want To Do Any Other Function(y/n)".rjust(92)) 
        if h=="y":
            pass
        elif h=="n":
            choice()
            break 
        else:
            print("Wrong Input".center(140))
            j=input("Do you want to Try Again(y/n)".rjust(85)) 
            if j.strip()=="y":
                pass 
            else:
                Table_owner()

def Read_Table():
    l=[]
    q="Select * from {0}".format(i) 
    try:
       c1.execute(q) 
    except:
       print()
       print("Error Found".center(140)) 
       print("Possible Errors are:".center(140),
       "1.Table Doesn't Exist".center(140),sep="\n") 
       print()
       Owner(i) 
    r=c1.fetchall() 
    for x in r:
        l+=[x] 
        if len(l)!=0:
            print(tabulate(l,headers=[" Item_Code ", " Name ",
            " Cost ",
            " Quantity Available ", " Item_Provider "," Item_Provier_Phone_No"],tablefmt='orgtbl')) 
        else:
            print("No Data Exists".center(140)) 
    conn.commit()

def Insert_Table():
    while True:
        ic=input("Enter Item Code".rjust(77))
        n=input("Enter Name".rjust(74))
        c=int(input("Enter Cost".rjust(74)))
        qta=int(input("Enter Qty Available".rjust(81))) 
        ip=input("Enter Item Provider".rjust(80)) 
        ipp=int(input("Enter Item Provider's Phone No".rjust(85))) 
        q="insert into {0} values('{1}','{2}',{3},{4},'{5}',{6})".format(i,ic,n,c,qta,ip,ipp) 
        try:
           k=c1.execute(q)
           conn.commit() 
        except :
            print()
            print("Error Found".center(140))
            print("Possible Errors are:".center(140), "1.Table doesn't Exist".center(140), "2.Wrong Input".center(140),sep="\n")
            print() 
            Owner(i) 
            break
        if k==1: 
            print()
            print("Inserted".center(140))
            print()
        o=input("Enter Do you want to Continue Inserting(y/n)".rjust(93))
        if o.strip()=="y":
            pass
        elif o.strip()=="n":
            Owner(i)
            break 
        else:
            print("Wrong Input".center(140))
            j=input("Do you want to Try Again(y/n)".rjust(85)) 
            if j.strip()=="y":
                pass 
            else:
                Owner(i)

def Update_Table():
    while True:
        l=input("Enter Item Code for which information is to be up-dated".rjust(100)) 
        print()
        print("Field_Names :".center(140), "1.Name".center(140),
        "2.Cost".center(140), "3.Quantity_Available".center(140) ,"4.Item_Provider".center(140), "5.Item_Provider_Phone_No".center(140),sep="\n")
        j=input("Enter Field Name".rjust(77)) 
        k=input("Enter New Value".rjust(77)) 
        q="update {0} set {1}='{2}' where Item_code='{3}'".format(i,j,k,l)
        try:
            k=c1.execute(q)
        except: 
            print()
            print("Error Found".center(140))
            print("Possible Errors are:".center(140), "1.Item Code Not found".center(140), "2.Table doesn't Exist".center(140), "3.Wrong Input".center(140),sep="\n")
            print()
            break 
        if k==1:
            print("Updated".center(140))
            o=input("Enter Do you want to Continue Updating(y/ n)".rjust(93))
            if o.strip()=="y": 
                pass
            elif o.strip()=="n": 
                Owner(i)
                break
            else:
                print("Wrong Input".center(140))
                j=input("Do you want to Try Again(y/n)".rjust(85)) 
                if j.strip()=="y":
                    pass 
                else:
                    Owner(i) 
        else:
            print("No Data Found".center(140))
            j=input("Do you want to continue updating(y/n)".rjust(90))
            if j.strip()=="y": 
                pass
            elif j.strip()=="n": 
                Owner(i)
                break 
            else:
                print("Wrong Input".center(140))
                j=input("Do you want to Try Again(y/n)".rjust(85)) 
                if j.strip()=="y":
                    pass 
                else:
                    Owner(i) 
    conn.commit()

def Delete_Table():
    while True:
        x=input("Enter Item Code whose record is to be deleted".rjust(94))
        q="delete from {0} where Item_Code='{1}'".format(i,x) 
        try:
            k=c1.execute(q) 
        except:
            print()
            print("Error Found".center(140))
            print("Possible Errors are:".center(140),
            "1.Item Code Not found".center(140),
            "2.Table doesn't Exist".center(140),sep="\n") 
            print()
            break 
        if k==1:
            print("Deleted".center(140))
            o=input("Enter Do you want to Continue Deleting(y/ n)".rjust(93))
            if o.strip()=="y": 
                pass
            elif o.strip()=="n": 
                Owner(i)
                break 
            else:
                print("Wrong Input".center(140)) 
        else:
            print("No Data Found".center(140))
            j=input("Do you want to continue Deleting(y/ n)".rjust(90))
            if j.strip()=="y": 
                pass
            else: 
                Owner(i) 
                break
    conn.commit()

def Search_Table():
    while True:
        x=input("Enter Item Code for which information is to be searched".rjust(100))
        q="Select * from {0} where Item_Code='{1}'".format(i,x) 
        try:
            a=c1.execute(q) 
        except:
            print()
            print("Error Found".center(140)) 
            print("Possible Errors are:".center(140),
            "1.Item Code Not found".center(140),
            "2.Table doesn't Exist".center(140),sep="\n") 
            print()
            break 
        if a==1:
            w=c1.fetchone()
            q=PrettyTable([" Item_Code ", " Name ",
            " Cost ",
            " Quantity Available ",
            " Item_Provider ",
            " Item_Provier_Phone_No "])
            q.add_row(w)
            print(q)
            o=input(" Enter Do you want to Continue Searching(y/n)".rjust(93))
            if o.strip()=="y":
                pass
            elif o.strip()=="n":
                Owner(i)
                break 
            else:
                print("Wrong Input")
        else:
            print("No Data Found".center(140))
            j=input("Do you want to continue Searching(y/n)".rjust(90)) 
            if j.strip()=="y":
                pass
            else:
                Owner(i)
                break 
    conn.commit()

def Stock_Order():
    qty=int(input('Quantity after which Restocking is Required'.rjust(93)) )
    try:
        c1.execute("Select * from {0} whereQuantity_Available<'{1}'".format(i,qty)) 
    except:
        print()
        print("Error Found".center(140))
        print("Possible Errors are:".center(140),
        "1.Item Code Not found".center(140), "2.Table doesn't Exist".center(140),sep="\n")
        print() 
    r=c1.fetchall() 
    l=[]
    for x in r:
        l+=[x]
        if len(l)!=0:
            print(tabulate(l,headers=[" Item_Code "," Name ",
            " Cost ",
            " Quantity Available ",
            " Item_Provider ",
            " Item_Provier_Phone_No "],tablefmt='orgtbl'))

            print()
            print("These Items are Required to Restock".center(140))
        else:
            print("No Data Found".center(140))
    conn.commit()

open()