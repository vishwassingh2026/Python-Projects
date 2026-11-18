Python 3.15.2 (tags/v3.15.2, Oct 25 2026, 17:27:3) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... print("===================================")
... print("       WELCOME TO PYTHON ATM")
... print("===================================")
... 
... while True:
... 
...     print("\n========== ATM MENU ==========")
...     print("1. Check Balance")
...     print("2. Deposit Money")
...     print("3. Withdraw Money")
...     print("4. Change PIN")
...     print("5. Transaction History")
...     print("6. Exit")
...     print("==============================")
... 
...     choice = input("Enter your choice (1-6): ")
... 
...     if choice == "1":
...         print("You selected Check Balance")
... 
...     elif choice == "2":
...         print("You selected Deposit Money")
... 
...     elif choice == "3":
...         print("You selected Withdraw Money")
... 
...     elif choice == "4":
...         print("You selected Change PIN")
... 
...     elif choice == "5":
...         print("You 
...         break
... 
...     else:
                  correct_pin="1234"
                  balance=5000
                  pin= input("enter your ATM PIN:")
                  if pin== correct_pin:
                  print("Login Successful !")
                  print("welcom to ATM")
                  else:
                      print("Incorrect PIN!")

