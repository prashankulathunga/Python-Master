"""
Exercise - 1
    - Find the min of 3 given numbers
"""

# use integer number only
"""
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

if n1 < n2 and n1 < n3:
    print(f'Min number:  {n1}')
elif n2 < n1 and n2 < n3:
    print(f'Min number: {n2}')
else:
    print(f'Min number: {n3} \n')
"""


"""
Exercise - 2
    - ATM Machine Menu

    1 - Pin Change
    2 - Balance check
    3 - Withdraw
    4 - Deposit
    5 - Exit
"""


menu = input(
    """
Hi there! Welcome to ATM
Please choose

1. Enter 1 for Pin Change
2. Enter 2 for Balance Check
3. Enter 3 for Withdrawal
4. Enter 4 for Deposit
5. Enter 5 for Exit

"""
)

# conditional logic

if menu == "1":
    print('Pin Change')
elif menu == "2":
    print("Balance Check")
elif menu == "3":
    print("Withdrawal") 
elif menu == "4":
    print("Deposit")
elif menu == "3":
    print("Exit")
else:
    print("Enter Valid Number for Continue Service")                   