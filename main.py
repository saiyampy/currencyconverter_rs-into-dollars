print("Welcome to rupees into dollar and dollar into rupees converter")
print("press 1 for rupees into dollar:")
print("press 2 for dollar into rupees:")
try:#it will try the code
    choice = int(input("Enter your choice:\n"))
except Exception  as e:#This will only shown when the above code raises error
    print("You have entered a string")

def dollars_into_rupees():
    dollars = int(input("enter the amount of dollar to convert into rupees\n"))
    dollar_input = dollars*73.85
    print(f"{dollars} dollars  converted into rupees resulted  {dollar_input} rupees")

def rs_into_dollar():
       op = int(input("enter the amount of rupees to convert into dollar\n"))
       value = op/73.85
       print(f"{op} Rupees  converted into dollars resulted  {value}$ dollars ")

if choice == 1:
    rs_into_dollar()

if choice == 2:
    dollars_into_rupees()


print("Thanks For Using This Code")
