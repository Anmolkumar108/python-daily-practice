while True:
    color = input("Color enter karo (Red/Yellow/Green): ").upper()
    
    if color == "RED":
        print("STOP")
    elif color == "YELLOW":
        print("READY")
    elif color == "GREEN":
        print("GO")
    else:
        print("Invalid color!")
    
    ask = input("\nDobaara? (yes/no): ").lower()
    
    if ask == "yes" or ask == "y":
        continue
    else:
        print("BYE!")
        break
