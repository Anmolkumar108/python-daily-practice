from datetime import datetime

def convert_to_24_hour(time_str):
    try:
        time_obj = datetime.strptime(time_str, "%I:%M %p")
        
        
        return time_obj.strftime("%H:%M")
    except ValueError:
        return "Invalid format! Please enter the time in 'HH:MM AM/PM' format (e.g., 03:45 PM)"


print(convert_to_24_hour("09:15 AM"))  
print(convert_to_24_hour("03:45 PM"))  
print(convert_to_24_hour("12:00 AM"))  
print(convert_to_24_hour("12:30 PM"))  
