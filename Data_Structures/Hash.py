'''
Implement Hash table 
linear probing
'''

class HashTable:

    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):
        index = self.hashed_function(key)
        print(index)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return

            index = (index+1) % self.size

        #insert
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):

        index = self.hashed_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1) % self.size
        return None


    def hashed_function(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])

        return sum % self.size

if __name__ == "__main__":

    table = HashTable()

    table.put("apple", 30)
    table.put("orange", 20)
    table.put("log", 10)
    table.put("app", 0)
    table.put("dog", 100)

    print("orange's key value is " + str(table.get("orange")))


