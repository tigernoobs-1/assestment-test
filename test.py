def calculate_parking_fee(total_time, weekend_total, weekdays):
    hourly_rate = 1.5  # weekdays per hour rate
    maximun_fee = 20.0 # weekdays maximum charge
    weekend_rate = 2.0
    weekend_maximum_fee = 40.0
    parking_fee = 0
    weekend_fee = 0
    
    
    # Convert total_time to minutes
    total_minutes = total_time.total_seconds() // 60
   
    # Calculate the number of hours
    hours = total_minutes // 60
    
    total_weekend = weekend_total.total_seconds() // 60
    
    weekend_hours = total_weekend // 60
    
    
    weekend_total_days = weekend_total.days
    
    # calculate total days
    total_days = total_time.days

    # Calculate Parking Rate More Than 3 Hours
    if hours > 3 or weekend_hours > 3  :

        if weekdays == True:
            parking_fee = (hours - 3) * hourly_rate
            weekend_fee = weekend_hours * weekend_rate
            
        else :
            
            parking_fee = hours * hourly_rate
            weekend_fee = (weekend_hours - 3) * weekend_rate
            
        #set maximum price for a day
        if parking_fee > maximun_fee :
            parking_fee = maximun_fee
            
        if weekend_fee > weekend_maximum_fee :
            weekend_fee = weekend_maximum_fee
            
        #calculate total after a day 
        if hours > 24 or weekend_hours > 24  :
            parking_fee = (maximun_fee * total_days) + (hours - (24 * total_days)) * hourly_rate
            
            weekend_fee = (weekend_maximum_fee * weekend_total_days) + (weekend_hours - (24 * weekend_total_days)) * weekend_rate
    
    total_parking_fee = parking_fee + weekend_fee
    return total_parking_fee


from datetime import datetime, timedelta

venhicle_no = input("Enter Reg:")
intime = input("In-Time (%Y-%m-%d %H:%M:%S):")
Outtime = input("Out-Time (%Y-%m-%d %H:%M:%S):")
in_time = datetime.strptime(intime, "%Y-%m-%d %H:%M:%S")  # Input in time
out_time = datetime.strptime(Outtime, "%Y-%m-%d %H:%M:%S")  # Input out time

#in_time = datetime(2023, 5, 27, 9, 16)  # Input in time
#out_time = datetime(2023, 5, 27, 13, 16)  # Input out time

#out_time = datetime(2023, 5, 26, 12, 19)  # Input out time

# Calculate total parking time
total_time = out_time - in_time

# Initialize variables for weekdays and weekends
weekdays_time = timedelta()
weekends_time = timedelta()

# Iterate over each day in the parking duration
current_time = in_time

while current_time < out_time:
    # Check if the current day is a weekday (Monday to Friday)
    if current_time.weekday() < 5:
        weekdays_time += min(current_time + timedelta(days=1), out_time) - max(current_time, in_time)
    else:
        weekends_time += min(current_time + timedelta(days=1), out_time) - max(current_time, in_time)
    
    # Move to the next day
    current_time += timedelta(days=1)

total_time = weekdays_time + weekends_time
total_fee = 0

total_minutes = total_time.total_seconds() // 60

 # Calculate the number of hours
hours = total_minutes // 60

# Calculate the remaining minutes
minutes = total_minutes % 60

parking_fee = 0 

if minutes > 15 or hours > 0 :
    # check in time weekend or weekdays
    if in_time.weekday() < 5:
        total_fee = 3.0  # for the first 3 hours
        parking_fee = total_fee
        if hours > 3 :
            weekdays = True
            parking_fee = calculate_parking_fee(weekdays_time, weekends_time, weekdays)
            #weekend_fee = calculate_weekend_parking_fee(weekends_time, weekdays)
            if hours < 24 :
                parking_fee = total_fee + parking_fee
    else:
        total_fee = 5.0
        parking_fee = total_fee
        if hours > 3 :
            weekdays = False
            parking_fee = calculate_parking_fee(weekdays_time, weekends_time, weekdays)
            #weekend_fee = calculate_weekend_parking_fee(weekends_time, weekdays)
            if hours < 24 :
                parking_fee = total_fee + parking_fee
        


# Print the total time for weekdays and weekends
print("Weekdays parking time:", weekdays_time)
print("Weekends parking time:", weekends_time)
print("Reg No:")
print("In:", in_time)
print("Out:", out_time)
print("Duration:", total_time)
print("Amount To Pay $:", parking_fee)

