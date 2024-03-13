# User
# Parking fee is 
# If you return within 15 mins, its free
# Rs 100 for the first hr
# Rs 150 for each hr after that. 
# Fee is calculated in 30 min increments. (meaning, if you spent 25 mins, you will be charged for 30 mins
# If you spend 35 mins, you will be charged for one hr)
# Get entry time and exit time from customer as input and display the fee


def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours, minutes

def payment():
    global cost
    amount=0
    entry_time_str =input("Enter the entry time (HH:MM): ")
    exit_time_str = input("Enter the exit time (HH:MM): ")
    exit_hours, exit_minutes = parse_time(exit_time_str)

   
    entry_hours, entry_minutes = parse_time(entry_time_str)

    exit_total_minutes = exit_hours * 60 + exit_minutes
    entry_total_minutes = entry_hours * 60 + entry_minutes

    total_minutes = exit_total_minutes - entry_total_minutes
    total_hrs=total_minutes//60
    extra_min=total_minutes-total_hrs*60
    print("hr : ",total_hrs)
    print("min : ", extra_min)

   
    if extra_min>30:
        extraamt=100
    elif extra_min<=30:
        extraamt=50
    
    if total_hrs==0:
        if extra_min<=15:
            return 0
    elif total_hrs==1:
        amount=100
        if extra_min<=30:
            amount+=50
        else:
            amount+=150
            return amount
        return amount
    elif total_hrs==2:
        amount=100+150
        if extra_min<=30:
            amount+=50
        else:
            amount+=150
            return amount
        return amount
    else:
         amount=100+150*total_hrs-2
         if extra_min<=30:
            amount+=50
         else:
            amount+=150
            return amount
         return amount

    
print(payment())