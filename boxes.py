items = int(input("Please enter the number of items: "))
boxes = int(input("Please enter the number of items that will fit into each box: "))
print(f"For {items} and since each box holds only {boxes} you will need {items/boxes:.1f} boxes total")
