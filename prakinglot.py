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
def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours, minutes

def payment(rowid, columnid, parkingid):
    global cost
    amount=0
    exit_time_str = input("Enter the exit time (HH:MM): ")
    exit_hours, exit_minutes = parse_time(exit_time_str)

    entry_time_str = entry_timelist.get(parkingid)
    entry_hours, entry_minutes = parse_time(entry_time_str)

    exit_total_minutes = exit_hours * 60 + exit_minutes
    entry_total_minutes = entry_hours * 60 + entry_minutes

    total_minutes = exit_total_minutes - entry_total_minutes
   
    stay_timelist[parkingid] = total_minutes
    print("Total stay time:", total_minutes, "min")

    if total_minutes <= 15:
        amount =0
    
    
    total_hours = (total_minutes + 29) / 60
    print(total_hours)

    if total_hours == 1:
         amount = 100
    elif total_hours <= 2:
        amount =100 + 150
    else:
        fee = 100 + 150
        remaining_hours = total_hours - 2
        fee += remaining_hours * 150
        amount =fee
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
                entry_time=input("Enter the entry time (HH:MM): ")
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
