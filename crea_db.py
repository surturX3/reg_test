#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error
import os

from crea import main as crea
from aggiungi import main as add
from main import create_connection

def main():

     database = r"database.db"
     conn = create_connection(database)
     crea(conn)
     add(conn)

     

if __name__ == '__main__':
    main()
