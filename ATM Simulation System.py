balance = 1000  

while True:
    
    print("\n=== ATM Simulation System ===")
    print("1. Balance Check")
    print("2. Deposit (पैसे जमा करें)")
    print("3. Withdraw (पैसे निकालें)")
    print("4. Exit (बाहर निकलें)")
    
  
    choice = input("\nchoice (1-4): ")
    
    if choice == '1':
        
        print(f"Your current balance : ₹{balance}")
        
    elif choice == '2':
        
        amount = float(input("How much money do you want to deposit? ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} Successfully deposited.")
            print(f"New balance: ₹{balance}")
        else:
            print("Please enter a valid amount!")
            
    elif choice == '3':
        
        amount = float(input("How much money do you want to withdraw? ₹"))
        if amount > balance:
            
            print("Transaction Failed! Insufficient balance.")
            print(f"Your current balance sirf ₹{balance} hai.")
        elif amount <= 0:
            print("Please enter a valid amount!")
        else:
            balance -= amount
            print(f"₹{amount} Successfully withdrawn.")
            print(f"New balance: ₹{balance}")
            
    elif choice == '4':
        
        print("Thank you for using the ATM. Have a nice day!")
        break
        
    else:
        
        print("Invalid choice! Please select a number between 1 and 4.")
