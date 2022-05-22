# Main array data structure
ARRAY = []

# function to accept data elements and store them in the main array
def acceptArray():
    n = int(input("Enter number of elements: "))
    print("Enter the numbers:")
    for i in range(n):
        x = int(input(f"{i+1}: "))
        ARRAY.append(x)
        n -= 1

# function to display array contents
def displayArray():
    print("Idx : Val")
    for i, x in enumerate(ARRAY):
        print(f"{i} : {x}")

# search for a particular element in the array
# performs linear search
def searchArray(val):
    for i, x in enumerate(ARRAY):
        if x == val:
            print(f"Item {val} found at location {i}.")
            return
    print(f"Item {val} not found!")

# print menu options
def printOptions():
    print("Options:       \n\
          1: Accept Array \n\
          2: Display Array\n\
          3: Search Array \n\
          4: Exit")

# driver code
def main():
    while True:
        printOptions()
        ch = input(":> ")
        if ch == "4":
            break
        elif ch == "1":
            acceptArray()
        elif ch == "2":
            displayArray()
        elif ch == "3":
            x = int(input("Enter the value you want to search for: "))
            searchArray(x)
        else:
            print("Invalid Option! Try again.")
            continue

if __name__ == "__main__":
    main()
