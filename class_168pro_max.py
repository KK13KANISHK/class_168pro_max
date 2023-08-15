# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 13:02:27 2023

@author: kanis
"""

class Books:
    def __init__(self, name, author, price, published_year):
        self.book_name = name
        self.author_name = author
        self.book_price = price
        self.book_published_year = published_year
        
    def add_book(self):
        print("Name of the book is: " + self.book_name)
        print("Author's name is: " + self.author_name)
        print("Price off the book is: " + str(self.book_price) + " ONLY")
        print("And the book was published in the year: " + str(self.book_published_year))
        print("This is your book, Enjoy")
        
    def yrs_since_pub(self):
        yrs_ago_pub = 2023 - self.book_published_year
        print("This Book Was Published " + str(yrs_ago_pub) + " Years Ago")
        
book_1 = Books("Rich dad, Poor dad", "Robert Kiyosaki", 655, 2011)
book_1.add_book()