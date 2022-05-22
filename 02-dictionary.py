# hastable data structure implementation
class HashTable:
    def __init__(self, size) -> None:
        self.mSize = size;
        self.mTable = dict()
        self.mNOE = 0;  # Number of elements

    def isFull(self):
        if(self.mNOE == self.mSize):
            return True
        else: return False

    # hash function
    def _mHashFunc(self, element):
        return int(str(hash(element))[-3:]);

    def insert(self, key, value):
        if(self.isFull()):
            print("Hash table is Full!!")
            return False
        pos = self._mHashFunc(value)
        if(pos in self.mTable.keys()):
            while(pos in self.mTable.keys()):
                pos+=1
                if(pos>=self.mSize):
                    pos = 0
        self.mTable[pos] = (key,value)
        self.mNOE+=1
        return True

    def search(self, skey):
        pos = self._mHashFunc(skey)
        if(pos in self.mTable.keys()):
            return self.mTable[pos];
        else:
            for key in self.mTable.keys():
                if key == skey:
                    return self.mTable[key];
            return -1;

    def delete(self, key):
        if(key in self.mTable.keys()):
            self.mTable.pop(key)
            return True
        return False

class Dict:
    def __init__(self) -> None:
        self.mTable = HashTable(1000)
        self.mSize = 0

    def inputPair(self, message):
        while(True):
            try:
                key, value = input(message).split(":")
                key = key.strip()
                value = value.strip()

                break
            except(ValueError):
                print("Invalid input, try again!")
        key = key.strip()
        value = value.strip()
        return key, value

    def acceptData(self):
        n = int(input("Enter number of elements: "))
        print("Enter key value pairs (\"key : value\") : ")
        for i in range(n):
            key, value = self.inputPair(f"{i} => ")
            self.mTable.insert(key, value);
            n -= 1

    def insert(self):
        key, value = self.inputPair("Enter a key value pair (\"key : value\") : ")
        if(self.mTable.insert(key, value)):
            print("Key-value inserted successfully.")
        else: print("Insertion failed.")

    def find(self):
        key = input("Enter the key you want to find: ")
        value = self.mTable.search(key)[1]
        if(value):
            print(f"Key value pair found: {key} : {value}")
        else:
            print(f"Key value pair not found!")

    def delete(self, key):
        key = input("enter the key you want to delete: ")
        if(self.mTable.delete(key)):
            print("Key-value inserted successfully.")
        else: print("Insertion failed.")

    def displayData(self):
        print("Key : Value")
        for key in self.mTable.mTable.keys():
            print(f"{self.mTable.mTable[key][0]} : {self.mTable.mTable[key][1]}")

dictionary = Dict()

def printOptions():
    print("Options:       \n\
          1: Accept key-value pairs \n\
          2: Display Dictionary contents\n\
          3: Insert key-value pair\n\
          4: Find key-value pair\n\
          5: Exit")


def main():
    while True:
        printOptions()
        ch = input(":> ")
        if ch == "5":
            break
        elif ch == "1":
            dictionary.acceptData()
        elif ch == "2":
            dictionary.displayData()
        elif ch == "3":
            dictionary.insert()
        elif ch == "4":
            dictionary.find()
        else:
            print("Invalid Option! Try again.")
            continue

main()
