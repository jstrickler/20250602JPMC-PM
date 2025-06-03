print("Welcome to ticket sales\n")

tickets_sold = 0
while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    print(f"sending {quantity} ticket(s)")
    tickets_sold += quantity

print(f"{tickets_sold} tickets sold")