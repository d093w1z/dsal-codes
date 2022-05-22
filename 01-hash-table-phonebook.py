class HashTable:
    def __init__(self, size) -> None:
        self.mSize = size;
        self.mTable = list(0 for i in range(size))
        self.mNOE = 0;  # Number of elements

    def isFull(self):
        if(self.mNOE == self.mSize):
            return True
        else: return False

    def _mHashFunc(self, element):
        return element % self.mSize;

    def insert(self, data):
        if(self.isFull()):
            print("Hash table is Full!!")
            return False
        pos = self._mHashFunc(data)
        if(self.mTable[pos]!=0):
            while(self.mTable[pos]!=0):
                pos+=1
                if(pos>=self.mSize):
                    pos = 0
        self.mTable[pos] = data
        self.mNOE+=1
        return True

    def search(self, data):
        pos = self._mHashFunc(data)
        if(self.mTable[pos]!=0):
            return pos;
        else:
            for i, x in enumerate(self.mTable):
                if x == data:
                    return i;
            return -1;

class TelBook:
    def __init__(self) -> None:
        self.mTable = None;

    def acceptData(self):
        n = int(input("Enter number of elements: "))
        self.mTable = HashTable(n)
        print("Enter the numbers:")
        for i in range(n):
            x = int(input(f"{i+1}: "))
            self.mTable.insert(x);
            n -= 1

    def insertData(self):
        x = int(input("Enter telephone number: "))
        if(self.mTable.insert(x)):
            print("Insertion Successfull!")
        else:
            print("Insertion Failed!")

    def displayData(self):
        print("Index : Telephone number")
        for i, x in enumerate(self.mTable.mTable):
            print(f"{i} : {x}")

    def searchData(self):
        val = int(input("Enter the value you want to search for: "))
        loc = self.mTable.search(val)
        if(loc):
            print(f"Item {val} found at location {loc}.")
        else:
            print(f"Intem {val} not found!")


TBook = TelBook()

def printOptions():
    print("Options:       \n\
          1: Accept Telephone numbers \n\
          2: Display Telephone numbers\n\
          3: Insert Telephone numbers(rehash)\n\
          4: Search Telephone number\n\
          5: Exit")


def main():
    while True:
        printOptions()
        ch = input(":> ")
        if ch == "5":
            break
        elif ch == "1":
            TBook.acceptData()
        elif ch == "2":
            TBook.displayData()
        elif ch == "3":
            TBook.insertData()
        elif ch == "4":
            TBook.searchData()
        else:
            print("Invalid Option! Try again.")
            continue

if __name__ == "__main__":
    main()
