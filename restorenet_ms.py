items = {"pizza": 3, "pasta": 2, "rice": 1, "soup": 4}

total_price = 0
count = 0

while count < 1:
    print(
        """
Welcome to our shop :
Today Price List:
 1. pizza: 3
 2. pasta: 2
 3. rice: 1
 4. soup: 4
  """
    )
    food_name = input("Enter the name of the item you want to order: ")
    food_count = input("Enter the count of the items: ")

    if food_name in items:
        category_total = float(items[food_name]) * int(food_count)
        total_price += category_total
        print(f"your total bill is {total_price} and you ordered {food_name} * {food_count}")
        is_continue = input("Is need more food (y/n): ")
        if is_continue.lower() == "y":
            continue
        else:
            print(f"Your total bill : {total_price}, Thank You!")
            break
    else:
        print("Wrong Input, please enter again")
