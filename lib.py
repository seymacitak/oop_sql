import sqlite3
import time

class Book():
    def __init__(self, name, writer, publisher, kind, printing):
        self.name = name 
        self.writer = writer
        self.publisher = publisher 
        self.kind = kind
        self.printing = printing 

    def __str__(self):
        return "Book Name: {}\nWriter: {}\nPublisher: {}\Kind: {}\nPrinting: {}\n".format(self.name,self.writer,self.publisher,self.kind,self.printing)

