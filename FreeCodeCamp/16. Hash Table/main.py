class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, value):
        total = 0
        for c in value:
            total += ord(c)
        return total

    def add(self, key, value):
        key_hash = self.hash(key)
        current_dict = {key:value}
        if key_hash in self.collection:
            self.collection[key_hash].update(current_dict)
        else:
            self.collection.update({key_hash:current_dict})

    def remove(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            if key in self.collection[key_hash]:
                self.collection[key_hash].pop(key)

    def lookup(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection:
            if key in self.collection[key_hash]:
                return self.collection[key_hash][key]
        else:
            return None