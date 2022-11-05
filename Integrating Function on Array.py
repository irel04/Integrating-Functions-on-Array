print(f"\n{'=' * 75}")
print(f"{'|'}{' ': >20}{'Programmed by Irel Kian C. Bacolod'}{' ': >19}{'|'}")
print(f"{'=' * 75}")

try:
    list1 = [40, 32, 24, 12, 20, 28, 4, 36, 16, 8]

    print("\n" + "-" * 50)
    print("|" + " " * 22 + "Menu" + " " * 22 + "|")
    print("-" * 50 + "\n")
    print("[a] Add an element", end="               ")
    print("[b] Insert an element")
    print("[c] Modify an element", end="            ")
    print("[d] Delete an element")
    print("[e] Arrange in ascending order", end="   ")
    print("[f] Arrange in descending order")
    print("[g] Find Length", end="                  ")
    print("[h] Find minimum number")
    print("[i] Find maximum number", end="          ")
    print("[j] Find sum")
    print("\nArray: ", list1)


    option = input("\nChoose from the menu (a-j): ")
    if option.lower() == "a":
        print("\n[a] Add an element")
        new = int(input("Enter a new element: "))
        list1.append(new)
    elif option.lower() == "b":
        print("\n[b] Insert an element")
        indx = int(input("Specify index: "))
        new = int(input("Insert element: "))
        list1.insert(indx, new)
    elif option.lower() == "c":
        print("\n[c] Modify an element")
        indx = int(input("Specify index: "))
        new = int(input("Insert element: "))
        list1.pop(indx)
        list1.insert(indx, new)
    elif option.lower() == "d":
        print("\n[d] Delete an element")
        indx = int(input("Specify index: "))
        list1.pop(indx)
    elif option.lower() == "e":
        print("\n[e] Arrange in ascending order")
        list1.sort()
    elif option.lower() == "f":
        print("[f] Arrange in descending order")
        list1.sort()
        list1.reverse()
    elif option.lower() == "g":
        print("[g] Find Length")
        print("Lenght of Array: ", len(list1))
    elif option.lower() == "h":
        print("[h] Find minimum number")
        print("Minimum number: ", min(list1))
    elif option.lower() == "i":
        print("[h] Find maximum number")
        print("Maximum number: ", max(list1))
    elif option.lower() == "j":
        print("[j] Find sum")
        print("Sum of the elements: ", sum(list1))
    print("Current Array: ", list1)

except ValueError:
    print("Please try again. Invalid Input")