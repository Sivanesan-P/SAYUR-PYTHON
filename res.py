def AddFood(foodItem):
    itemName=input("Enter the item name:")
    price=int(input("Enter the price:"))
    foodItem[itemName] =  price
    
def viewItem(foodItem):
    print(foodItem)

def bill(foodItem):
    opt=input("Do you want a bill y/n:")
    total=0
    dis=0
    item=[]
    qty=[]
    cst=[]
    amt=[]
    while(opt=="y"):
        n=input("Enter the item :")
        q=int(input("Enter the quantity:"))
        if(n in foodItem):
            m=foodItem [n]
            cost=m*q
            total=total+cost
            for i in range(0,opt=='y'):
                 item.append(n)
                 qty.append(q)
                 cst.append(cost)
                 amt.append(m)
            
        else:
            print("you have entered a wrong item")
        opt=input("have you ordered anything else y/n:")
        
    opt2=input("Did u have any promo code(y/n) :")
    if(opt2=='y'):
        code=input("Enter the promo code for discount:")
        if(code.upper()=='SAYUR10'):
            dis=((total*10)/100)
            total=total-dis
        else:
            print("INVALID PROMO CODE")
    print("-----------------------BILL-------------------")
    print("item   qty   price  total")
    for i in range(0,len(item)):
        print(item[i]," ", qty[i],"   ", amt[i],"   ", cst[i])
    print("DISCOUNT :         ",dis)
    print("TOTAL :            " ,total)
    print("----------------------------------------------")
       


def main():
    foodItem={}
    foodItem={"dosa": 30 ,"idly": 20 ,"pongal": 45 }
    print("1.Add Item in Menu")
    print("2.Display Menu")
    print("3.Calculate Bill")
    print("4.end")
    choice=int(input("Enter your Choice :"))
    while True:
        if (choice==1):
            AddFood(foodItem)
        elif (choice==2):
            viewItem(foodItem)
        elif (choice==3):
            bill(foodItem)
        elif (choice==4):
            print("THANK YOU HAVE A GREAT DAY")
            break
        else:
            print("Please enter a correct option")
        choice=int(input("Enter your Choice :"))
    
main()
