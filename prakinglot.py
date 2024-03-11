parkedid = []
cost = 0
entry_timelist={}
stay_timelist={}

def initialize_parking(row, column):
    global parking_lot  
    parking_lot = [[0 for _ in range(column)] for _ in range(row)]
    return parking_lot

def print_parking_lot():
    global parking_lot  
    for row in parking_lot:
        for spot in row:
            print(spot, end=" ")
        print()
def payment(rowid,columnid,parkingid):

  exit_time=float(input("enter the exit time : "))
  entry_time=entry_timelist.get(parkingid)
  total_Time=exit_time-entry_time
  stay_timelist[parkingid]=total_Time
  userstay=stay_timelist.get(parkingid)
  print(userstay)

  

  amount = 20  
  print("You need to pay $", amount)
  while True:
            payment = int(input("Enter the payment amount: "))
            if payment >= amount:
                parking_lot[rowid][columnid] = 0
                cost += amount
                print("Thank you for payment. Car can leave now.")
                break
            else:
                print("Insufficient payment. Please pay the correct amount.")


def enter_parking():
    global parking_lot 
    for i in range(len(parking_lot)):
        for j in range(len(parking_lot[0])):
            if parking_lot[i][j] == 0:
                parking_lot[i][j] = 1
                id_str = str(chr(65 + i) + str(1 + j))
                parkedid.append(id_str)
                entry_time=float(input("enter the time in float value example 1.15 "))
                entry_timelist[id_str]=entry_time
                print("Car parked successfully with ID:", id_str)
                return
        break
    print("Parking is full.")

def leave_parking():
    global parking_lot 
    global cost
    parking_id = input("Enter the ID of the car leaving: ")
    if parking_id in parkedid:
        row_concat = parking_id[0]
        column_concat = parking_id[1:]
        
        row_id = ord(row_concat) - 65
        column_id = int(column_concat) - 1
        print("Car found at row:", row_id, "column:", column_id)
        payment(row_id,column_id,parking_id)
    else:
        print("Invalid ID. Car not found in parking lot.")

def admin_interface():
    global parking_lot 
    while True:
        print("\n--- Admin Menu ---")
        print("1. Initialize Parking Lot")
        print("2. Print Parking Lot")
        print("3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
            initialize_parking(rows, columns)
            print("Parking lot initialized with size:", rows, "x", columns)
        elif choice == 2:
            print_parking_lot()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter again.")

def user_interface():
    while True:
        print("\n--- User Menu ---")
        print("1. Enter Parking")
        print("2. Leave Parking")
        print("3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            enter_parking()
        elif choice == 2:
            leave_parking()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please enter again.")

while(True):
    interfaceinput=int(input(("enter interface you want to go 1.admin ,2.user,3.exit : ")))
    if(interfaceinput==1):  
        admin_interface()
    elif(interfaceinput==2):
        user_interface()
    elif(interfaceinput==3):
        break
    else:
        print("Invalid input")
