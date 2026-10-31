# ===============================
# Smart ATM & Banking System
# ===============================
account_holder = "Rahul"  
atm_pin = "1234"  
account_balance = 10000.0  
daily_withdrawal_limit = 5000.0  
transaction_count = 0  
is_account_active = True  

print("===== SMART ATM SYSTEM =====")
print(f"Account Holder: {account_holder}")
print(f"Account Balance: ₹{int(account_balance)}")
print(f"Daily Withdrawal Limit: ₹{int(daily_withdrawal_limit)}")
print("============================")

attempts = 3
pin_verified = False

while attempts > 0:
  entered_pin = input("\nEnter your ATM PIN: ")

  if entered_pin == atm_pin:
    print("PIN Verified Successfully!")
    pin_verified = True
    break
  else:
    attempts -= 1
    print(f"Incorrect PIN. Attempts left: {attempts}")

if not pin_verified:
  print(
      "\n3 baar galat PIN enter karne ke karan program access block kar diya"
      " gaya hai."
  )
  exit()


while True:
  print("\n========== ATM MENU ==========")
  print("1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Check Transaction Count")
  print("5. Exit")
  print("==============================\n")

  choice = input("Enter your choice (1-5): ")


  if choice == "1":
    print(f"\nAccount Balance: ₹{account_balance}")


  elif choice == "2":
    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
      print("\nInvalid amount! Amount zero ya negative nahi hona chahiye.")
    else:
      account_balance += amount
      transaction_count += 1
      print("\nDeposit Successful!")
      print(f"New Balance: ₹{account_balance}")


  elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
      print("\nInvalid amount! Amount positive hona chahiye.")
    elif amount > account_balance:
      print("\nWithdrawal Failed! Account mein sufficient balance nahi hai.")
    elif amount > daily_withdrawal_limit:
      print(
          "\nWithdrawal Failed! Ek transaction mein withdrawal ₹5,000 se zyada"
          " nahi ho sakta."
      )
    else:
      account_balance -= amount
      transaction_count += 1
      print("\nWithdrawal Successful!")
      print(f"Remaining Balance: ₹{account_balance}")


  elif choice == "4":
    print(f"\nTotal Successful Transactions: {transaction_count}")


  elif choice == "5":
    print("\nThank you for using Smart ATM!")
    print("Have a nice day.")
    break

  else:
    print("\nInvalid choice! Kripya 1 se 5 ke beech mein option select karein.")
