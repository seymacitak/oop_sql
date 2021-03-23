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


class Library():

    def __init__(self):
        self.make_connect()

    def make_connect(self):

        self.connect = sqlite3.connect("library.sqlite3")

        self.cursor = self.connect.cursor()

        query = "CREATE TABLE IF NOT EXISTS bookcase (Name, Writer, Publisher, Kind, Printing)"

        self.cursor.execute(query)

        self.connect.commit()

    def cut_connect(self):
        self.connect.close()
