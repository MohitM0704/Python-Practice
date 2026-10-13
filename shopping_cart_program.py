shopping = ["bread", "milk", "butter", "toast", "eggs"]
shopping.remove(input("Selct a item: "))
print(shopping)
print(len(shopping))

choice = input("Do you want to add another item (Yes/No): ")
if choice == "Yes":
    item = input("What item do you want to add: ")
    shopping.append(item)
    print("\n Updated Shopping List")
    print(shopping)
    print(f"Total items: {len(shopping)}")

else:
    print("Thank You")
