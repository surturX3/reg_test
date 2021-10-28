#!/usr/bin/env python3

def es_sconti(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM discount ')
    wa_sconti = cur.fetchall()
    return wa_sconti 

def c_sconti(it_sconti,wa_fornitori,date,iv_qty):
    for wa_sconti in it_sconti:
        if(wa_fornitori[0]==wa_sconti[0]):
            if (wa_sconti[1]!=None):
                if(wa_fornitori[4]>wa_sconti[1]):
                    wa_fornitori[4] = float(f'{wa_fornitori[4] - (wa_fornitori[4]/100*wa_sconti[5]):.2f}')
            if (wa_sconti[2]!=None):
                if(wa_sconti[3]!=None):
                    if(iv_qty >= wa_sconti[2] and iv_qty <wa_sconti[3]):
                        wa_fornitori[4] = float(f'{wa_fornitori[4] - (wa_fornitori[4]/100*wa_sconti[5]):.2f}')
                else:
                    if(iv_qty >= wa_sconti[2]):
                        wa_fornitori[4] = float(f'{wa_fornitori[4] - (wa_fornitori[4]/100*wa_sconti[5]):.2f}')
            if (wa_sconti[3]!=None):
                if(iv_qty > wa_sconti[3]):
                    wa_fornitori[4] = float(f'{wa_fornitori[4] - (wa_fornitori[4]/100*wa_sconti[6]):.2f}')
            if (wa_sconti[4]!=None):
                if(date == wa_sconti[4]):
                    wa_fornitori[4] = float(f'{wa_fornitori[4] - (wa_fornitori[4]/100*wa_sconti[6]):.2f}')
    
    return wa_fornitori
