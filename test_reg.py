#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error
import os

from crea import main as crea
from aggiungi import main as add
from main import create_connection
from main import main as inizio

def example1():
     try:
          os.remove("test1.db")
     except:
          pass
     database = r"test1.db"
     conn = create_connection(database)
     crea(conn)
     add(conn)
     print("First Example:")
     print("Oggetto: Philips monitor 17")
     print("Numero Pezzi: 12")
     print("Mese: Settembre")
     inizio(9,12,"Philips monitor 17",conn)

def example2():
     try:
          os.remove("test2.db")
     except:
          pass
     database = r"test2.db"
     conn = create_connection(database)
     crea(conn)
     add(conn)
     print("Second Example:")
     print("Oggetto: Philips monitor 17")
     print("Numero Pezzi: 12")
     print("Mese: Ottobre")
     inizio(10,12,"Philips monitor 17",conn)
     

def main():

     print("Example1------------------------BEGIN")
     example1()
     
     print("Example1------------------------END")

     print("Example2------------------------BEGIN")
     example2()
     
     print("Example2------------------------END")

     

if __name__ == '__main__':
     main()
     os.remove("test1.db")
     os.remove("test2.db")