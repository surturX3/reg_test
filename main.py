#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error
from termcolor import colored

from aggiungi import create_order
from sconti import  es_sconti ,c_sconti

def update_stocks(conn, stocks):
    """
    Aggiorniamo la quantita di stocks del fornitore 
    togliendo la quantità comprata
    """
    sql = ''' UPDATE stocks
              SET qty = ?
              WHERE vendor = ?'''
    cur = conn.cursor()
    cur.execute(sql, stocks)
    conn.commit()

def create_connection(db_file):
    """ 
    creiamo una connesione al database avendo l'indirizzo del db
    dando in ritorno l'oggetto conn
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def es_fornitore(conn,iv_qty,iv_item,date):
    """
    avendo la connessione ,la quantità da ordinare e l'oggetto da ordinare estraiamo i corispondenti fornitori con una querry
    """
    lv_index=0
    et_fornitori =list()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stocks where qty >= {0} AND item == '{1}'".format(str(iv_qty),str(iv_item)))
 
    #mettiamo i vari fornitori nella lista
    wa_fornitori = cur.fetchall()
    #con un ciclo for prendiamo i vari fornitori e calcoliamo il prezzo totale in base alla quantita e al prezzo per ogni pezzo
    for wa_fornitore in wa_fornitori:
        
        et_fornitori.append(list(wa_fornitore))
        et_fornitori[lv_index][4] = float((int(iv_qty) * wa_fornitore[4]))
        
        lv_index=lv_index+1
    #chiamiamo il mettodo per estrare la tabella degli sconti per poi applicare al prezzo totale per fornitore il suo relativo sconto
    it_sconti = es_sconti(conn)
    for wa_fornitore in et_fornitori:
        wa_fornitori.append(c_sconti(it_sconti,wa_fornitore,date,iv_qty))
    return et_fornitori

def main(date,iv_qty,iv_item,conn ):
    
    #iniziliaimo una lista dove veranno messi i vari fornitori
    it_fornitori =list()
    #estraiamo la lista dei fornitori passando la connessione al databse ,la quantita da ordinare ,l'oggetto e la data del mese espressa numericamente
    it_fornitori = es_fornitore(conn,iv_qty,iv_item,date)
    #con un if controlliamo se la lista dei fornitori e vuota
    if (it_fornitori != []):
        #iniziliziamo una lista con il primo fornitore all'interno di it_fornitori per avere un primo dato da confrontare per il prezzo piu basso       
        wa_mon = it_fornitori[0]
        for wa_item in it_fornitori:

            if (wa_mon[4] > wa_item[4]):
                wa_mon = wa_item
            
        #mostriamo a terminale  i vari fornitori colorando quello con il prezzo più basso di colore verde
        lv_index=0
        print("\n")
        for wa_item in it_fornitori:
            if (wa_item[0] != wa_mon[0]):
                print ("Numero selezione {5} \n Venditore: {0} \n Oggetto: {1} \n Tempi di spedizione: {2} \n Quantità: {3} \n Prezzo totale {4}\n".format(wa_item[0],wa_item[1],wa_item[2],wa_item[3],wa_item[4],(lv_index+1)))
            else:
                print (colored("Numero selezione {5} \n Venditore: {0} \n Oggetto: {1} \n Tempi di spedizione: {2} \n Quantità: {3} \n Prezzo totale {4}\n".format(wa_item[0],wa_item[1],wa_item[2],wa_item[3],wa_item[4],(lv_index+1)),'green'))
            lv_index = lv_index + 1
        lv_scelta=int(input("Quale scegli? "))-1

        #aggiornamento della tabella di stocks dopo la scelta 
        
        update_stocks(conn,(it_fornitori[int(lv_scelta)][3]-iv_qty,str(it_fornitori[int(lv_scelta)][0])))

        #manipolazione della lista prima del caricamento nella tabella degli ordini
        
        it_fornitori[int(lv_scelta)][3] = iv_qty
        wa_item =it_fornitori[int(lv_scelta)]
        print (colored("\nSelezionato \n Venditore: {0} \n Oggetto: {1} \n Tempi di spedizione: {2} \n Quantità: {3} \n Prezzo totale {4}\n".format(wa_item[0],wa_item[1],wa_item[2],wa_item[3],wa_item[4],(lv_index+1)),'yellow'))

        #carichiamo la scelta del fornitore nella tabella ordini 
        create_order(conn,(it_fornitori[int(lv_scelta)][0],it_fornitori[int(lv_scelta)][1],it_fornitori[int(lv_scelta)][2],it_fornitori[int(lv_scelta)][3],it_fornitori[int(lv_scelta)][4]))
    else:
        print("Nessun fornitore puo soddisfare la tua richiesta.")

if __name__ == '__main__':
        # iniziliziamo il dabase creando le tabelle se non c'erano e creiamo una connesione con il database
    import datetime
    dt = datetime.datetime.today()
    database = r"database.db"
    conn = create_connection(database)
    date = dt.month
    lv_item = input("Prodotto: ")
    lv_qty = int(input("Quantita?: "))
    main(date,lv_qty,lv_item,conn )
