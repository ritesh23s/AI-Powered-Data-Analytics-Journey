# *********************** PRACTICE QUESTION ***********************

# Question: 03).
# A company uses a punching machine to record employee arrival times.
# The punching machine stores the arrival time in the format:

# HH:MM:SS AM/PM

# The program should accept employee arrival times one by one.
# The program should continue accepting records until the user enters
# "STOP".

# Calculate and display:
# 1. Total number of valid attendance records.
# 2. Number of employees who arrived on time.
# 3. Number of employees who were late.
# 4. Number of employees who exceeded the late threshold.
# 5. Earliest arrival time.
# 6. Latest arrival time.

# Input:
# Enter employee arrival time in the format:
# HH:MM:SS AM/PM

# Enter "STOP" to stop entering attendance records.

# Conditions:
# The valid time format is HH:MM:SS AM/PM.

# Hours must be between 01 and 12.
# Minutes must be between 00 and 59.
# Seconds must be between 00 and 59.
# AM/PM must be either AM or PM.

# "STOP" is used only to stop the input.
# Input is case-insensitive, so "stop", "Stop", and "STOP"

# should all stop the program.
# Invalid time entries must not be included in the calculations.

# Attendance Rules:
# - Arrival at or before 09:00:00 AM → On Time.
# - Arrival after 09:00:00 AM and at or before 09:30:00 AM → Late.
# - Arrival after 09:30:00 AM → Late Threshold Exceeded.

# Special Cases:
# - 12:00:00 AM represents midnight.
# - 12:00:00 PM represents noon.
# - The program must correctly handle these cases while comparing times.

# If no valid attendance record is entered, display:
# "No valid attendance records available"

# Output:
# Display the required attendance statistics.

# Example:

# Input:
# 08:47:32 AM
# 09:00:00 AM
# 09:12:45 AM
# 09:30:00 AM
# 09:30:01 AM
# 08:55:20 AM
# STOP

# Output:
# Total attendance records: 6
# On Time: 3
# Late: 2
# Late Threshold Exceeded: 1
# Earliest arrival: 08:47:32 AM
# Most Delayed arrival time: 09:30:01 AM

# Solution:

arrival_records = []

early_arrival_records = []
earliest_arrival_time = ""

exceeded_arrival_records = []
delayed_arrival_time = ""

print("****** Enter employee arrival time in the format: HH:MM:SS AM/PM ******")
print("****** Enter 'STOP' to stop entering attendance records ***************")

while True:
    arrival_time = input("Please enter arrival time: ").strip().lower()
    if arrival_time == "stop":
        break
    elif arrival_time[-2:] == "am" or arrival_time[-2:] == "pm":
        if not (arrival_time == "am" or arrival_time == "pm"):
            time_parts, period = arrival_time.split()
            hours, minutes, seconds = time_parts.split(":")
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)

            if (
                (hours >= 1 and hours <= 12) and 
                (minutes >= 0 and minutes < 60) and 
                (seconds >= 0 and seconds < 60)
            ):
                time_in_second   = ((hours*60*60) + (minutes*60) + (seconds))
                arrival_records.append(time_in_second)

                if time_in_second < 46799 and period == "am":
                    if time_in_second <= 32400:
                        # print("On Time!")
                        if time_in_second < 32400:
                            early_arrival_records.append(time_in_second)
                            earliest = min(early_arrival_records)
                            if time_in_second == earliest:
                                earliest_arrival_time = arrival_time
                        else:
                            pass
                    elif time_in_second > 32400 and time_in_second <= 34200:
                        # print("Late!")
                        pass
                    else:
                        # print("Late Threshold Exceeded!")

                        exceeded_arrival_records.append(time_in_second)
                        delayed = max(exceeded_arrival_records)
                        if time_in_second == delayed:
                            delayed_arrival_time = arrival_time
                else:
                    print("You are too late!")

                    exceeded_arrival_records.append(time_in_second)
                    delayed = max(exceeded_arrival_records)

                    if time_in_second == delayed:
                        delayed_arrival_time = arrival_time
            else:
                print("Please enter time correct format")
                print("Hours must be between 01 and 12")
                print("Minutes must be between 00 and 59")
                print("Seconds must be between 00 and 59")
        else:
            print("Please enter valid time format is HH:MM:SS")
    else:
        print("Please enter valid time format is HH:MM:SS AM/PM: ")


if len(arrival_records) > 0:
    print("Total attendance records: ", len(arrival_records))
    on_time = []
    late_time = []
    exceeded_time = []

    for time in arrival_records:
        if time <= 32400:
            on_time.append(time)
        elif time > 32400 and time <= 34200:
            late_time.append(time)
        else:
            exceeded_time.append(time)
    print("On Time:", len(on_time))
    print("Late:", len(late_time))
    print("Late Threshold Exceeded:", len(exceeded_time))
    print("Earliest arrival:", earliest_arrival_time)
    print("Most Delayed arrival time:", delayed_arrival_time)
else:
    print("No valid attendance records available")

# "In this code multiple bogs i think fix it again after some time"