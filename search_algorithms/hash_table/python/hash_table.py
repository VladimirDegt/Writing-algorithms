class HashTable:
    """
    A simple implementation of a hash table with separate chaining for collision resolution.
    """

    def __init__(self, size):
        """
        Initialize the hash table with a given size.

        Parameters:
        size (int): The size of the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        """
        Compute the hash value for a given key.

        Parameters:
        key: The key to hash.

        Returns:
        int: The hash value of the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Parameters:
        key: The key to insert.
        value: The value associated with the key.

        Returns:
        bool: True if the insertion is successful, False otherwise.
        """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def delete(self, key):
        """
        Delete a key-value pair from the hash table.

        Parameters:
        key: The key to delete.

        Returns:
        bool: True if the deletion is successful, False otherwise.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][index]
                    return True
        return False

    def get(self, key):
        """
        Retrieve the value associated with a given key from the hash table.

        Parameters:
        key: The key to search for.

        Returns:
        The value associated with the key if found, None otherwise.
        """
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Знайдене значення:", H.get("apple"))
print("Знайдене значення:", H.get("orange"))
print("Знайдене значення:", H.get("banana"))

H.delete("apple")
print("Знайдене значення:", H.get("apple"))