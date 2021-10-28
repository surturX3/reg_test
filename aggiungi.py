#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error

def create_stocks(conn, stocks):
    """
    Crea una tabella per gli oggetti in stock
    
    """
    sql = ''' INSERT INTO stocks(vendor,item,time,qty,price)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, stocks)
    conn.commit()
    return cur.lastrowid

def create_order(conn, order):
    """
    Crea una tabella ordini
    
    """

    sql = ''' INSERT INTO orders(vendor,item,time,qty,tot_price)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, order)
    conn.commit()
    return cur.lastrowid

def create_discount(conn, discount):
    """
    Crea una tabella sconti
    """

    sql = ''' INSERT INTO discount(vendor,price,pice_1,pice_2,month,discount_1,discount_2)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, discount)
    conn.commit()
    return cur.lastrowid

def main(conn):

    with conn:
        # inseriamo i dati di stocks
        stocks_1 = ('Supplier_1','Philips monitor 17',5,8,120)
        stocks_2 = ('Supplier_2','Philips monitor 17',7,15,128)
        stocks_3 = ('Supplier_3','Philips monitor 17',4,23,129)

        # popoliamo la tabella stocks
        create_stocks(conn, stocks_1)
        create_stocks(conn, stocks_2)
        create_stocks(conn, stocks_3)

        #inseriamo i dati degli sconti per venditore
        discount_1 = ('Supplier_1',1000,None,None,None,5,None)
        discount_2 = ('Supplier_2',None,5,10,None,3,5)
        discount_3 = ('Supplier_3',1000,None,None,9,5,2)

        #popoliamo la tabella sconti con gli sconti dei vari venditori
        create_discount(conn, discount_1)
        create_discount(conn, discount_2)
        create_discount(conn, discount_3)


if __name__ == '__main__':
    from main import create_connection
    database = r"database.db"
    conn = create_connection(database)
    main(conn)
