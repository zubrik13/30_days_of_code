from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        super().display()
        # print(f"Title: {self.title}")
        # print(f"Author: {self.author}")
        print(f"Price: {self.price}")


# title=input()
# author=input()
# price=int(input())
title = "The Alchemist"
author = "Paulo Coelho"
price = 248

new_novel = MyBook(title, author, price)
new_novel.display()
