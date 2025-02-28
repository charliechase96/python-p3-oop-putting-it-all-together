#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    def turn_page(self):
        print(f"Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print(f"page_count must be an integer")

    