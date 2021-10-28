#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error

def create_table(conn, create_table_sql):
    """
    Aggiorniamo la quantita di stocks del fornitore 
    togliendo la quantità comprata
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main(conn):

    sql_create_stocks_table = """ CREATE TABLE IF NOT EXISTS stocks (
                                        vendor text PRIMARY KEY,
                                        item text NOT NULL,
                                        time int NOT NULL,
                                        qty int NOT NULL,
                                        price real NOT NULL
                                    ); """

    sql_create_orders_table = """CREATE TABLE IF NOT EXISTS orders (
                                    vendor text NOT NULL,
                                    item text NOT NULL,
                                    time int NOT NULL,
                                    qty int NOT NULL,
                                    tot_price real NOT NULL
                                );"""
                                
    sql_create_discount_table = """CREATE TABLE IF NOT EXISTS discount (
                                    vendor text NOT NULL,
                                    price real,
                                    pice_1 int,
                                    pice_2 int,
                                    month int,
                                    discount_1 int,
                                    discount_2 int
                                );"""


    # create a database connection
    

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_stocks_table)

        # create tasks table
        create_table(conn, sql_create_orders_table)

        # create tasks table
        create_table(conn, sql_create_discount_table)
    else:
        print("Errore! non e possibile creare una connesione con il database.")


if __name__ == '__main__':
    from main import create_connection
    database = r"database.db"
    conn = create_connection(database)
    main(conn)
