#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = ""
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print(f"size must be an integer")

    def cobble(self):
        print(f"Your shoe is as good as new!")
        self.condition = "New"

    
